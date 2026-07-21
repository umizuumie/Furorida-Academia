init python:
    config.quit_callbacks += [discord.close]
    config.after_load_callbacks += [discord.on_load]
    config.interact_callbacks += [discord.rollback_check]
    config.start_callbacks += [discord.reset]

init -950 python in discord:

    def print_important(s):
        global log_important
        if log_important is True:
            print("\n" + s)
    def print_properties(s):
        global log_properties
        if log_properties is True:
            print("\n" + s)
    def print_rollback(s):
        global log_restore
        if log_restore is True:
            print("\n" + s)

    def format_properties(d):
        s = ""
        for key in d:
            s += "\n{}: ".format(key).ljust(14) + " {}".format(d[key])
        return s

    import store
    from store import NoRollback
    from store import Action

    class _PresenceContainer(NoRollback):
        def __init__(self):
            self.obj = None
        def __getstate__(self):
            return {}
        def __setstate__(self, state):
            self.obj = None

    import asyncio
    import sys
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    import sys, os
    sys.path.insert(0, os.path.join(renpy.config.gamedir, "libs"))
    import pypresence

    import time
    import threading
    from copy import deepcopy

    _container = _PresenceContainer()
    _container_lock = threading.Lock()
    _state_lock = threading.Lock()
    _watchdog_stop = threading.Event()

    start_time = time.time()

    class RenPyDiscord(NoRollback):
        def __init__(self):
            self.properties = {}

    no_rollback = RenPyDiscord()

    global original_properties, rollback_properties
    original_properties = deepcopy(main_menu_state)

    if not "start" in original_properties:
        original_properties["start"] = "start_time"

    def _try_connect():
        asyncio.set_event_loop(asyncio.new_event_loop())
        _max_retries = 6
        _retry_delay = 2.0

        for _attempt in range(1, _max_retries + 1):
            try:
                print_important("Attempting to connect to Discord Rich Presence... (attempt {}/{})".format(_attempt, _max_retries))
                obj = pypresence.Presence(application_id)
                obj.connect()
                with _container_lock:
                    _container.obj = obj
                print_important("Successfully connected.")
                return True

            except pypresence.DiscordNotFound:
                print_important("Discord Desktop App not found.")
                return False

            except pypresence.DiscordError as e:
                print_important("Connection attempt {} failed: {}".format(_attempt, e))
                if _attempt < _max_retries:
                    print_important("Retrying in {} seconds...".format(_retry_delay))
                    time.sleep(_retry_delay)
                else:
                    print_important("All {} attempts failed.".format(_max_retries))
                    return False

    def _watchdog_thread():
        global original_properties, rollback_properties

        connected = _try_connect()
        if connected:
            set(**original_properties)

        while not _watchdog_stop.wait(timeout=10.0):

            if not store.persistent.discord_enabled:
                with _container_lock:
                    obj = _container.obj
                if obj is not None:
                    try:
                        obj.clear()
                    except Exception:
                        pass
                continue

            with _container_lock:
                obj = _container.obj

            if obj is not None:
                try:
                    with _state_lock:
                        properties = deepcopy(no_rollback.properties)
                    if properties:
                        obj.update(**clean_properties(properties))
                    continue
                except Exception:
                    print_important("Discord Rich Presence connection lost. Attempting to reconnect...")
                    with _container_lock:
                        _container.obj = None

            try:
                obj = pypresence.Presence(application_id)
                obj.connect()
                with _container_lock:
                    _container.obj = obj
                print_important("Reconnected to Discord Rich Presence.")
                with _state_lock:
                    current = rollback_properties if rollback_properties else original_properties
                set(**current)
            except Exception as e:
                print_important("Reconnect attempt failed: {}".format(e))

    _connection_thread = threading.Thread(target=_watchdog_thread, daemon=True)
    _connection_thread.start()

    import atexit
    def _atexit_close():
        with _container_lock:
            obj = _container.obj
        if obj is None:
            return
        try:
            obj.clear()
            obj.close()
        except Exception:
            pass
    atexit.register(_atexit_close)

    def presence_disabled(func):
        def wrapper(*args, **kwargs):
            with _container_lock:
                obj = _container.obj
            if obj is None:
                return None
            if not store.persistent.discord_enabled:
                return None
            return func(*args, **kwargs)
        wrapper.__name__ = func.__name__
        return wrapper

    def return_none(*_args, **_kwargs): pass

    def record_into_rollback():
        global no_rollback, rollback_properties
        with _state_lock:
            rollback_properties = deepcopy(no_rollback.properties)

    def clean_properties(d):
        d = deepcopy(d)
        global start_time
        if "start" in d:
            if d["start"] == "start_time":
                d["start"] = start_time
        return d

    @presence_disabled
    def set(log=True, **props):
        if "start" in props:
            if props["start"] == "new_time":
                props["start"] = time.time()
        else:
            props["start"] = "start_time"

        global no_rollback
        with _state_lock:
            no_rollback.properties = deepcopy(props)
            snapshot = deepcopy(no_rollback.properties)

        try:
            with _container_lock:
                obj = _container.obj
                if obj is not None:
                    obj.update(**clean_properties(snapshot))
        except Exception as e:
            print_important("Discord Presence lost connection during set: {}".format(e))
            with _container_lock:
                _container.obj = None
            return

        record_into_rollback()

        if log:
            with _state_lock:
                snapshot = deepcopy(rollback_properties)
            print_properties("Discord Presence Set:{}".format(format_properties(snapshot)))

    @presence_disabled
    def update(log=True, **props):
        if "start" in props:
            if props["start"] == "new_time":
                props["start"] = time.time()

        global no_rollback
        with _state_lock:
            for p in props:
                no_rollback.properties[p] = props[p]
            snapshot = deepcopy(no_rollback.properties)

        try:
            with _container_lock:
                obj = _container.obj
                if obj is not None:
                    obj.update(**clean_properties(snapshot))
        except Exception as e:
            print_important("Discord Presence lost connection during update: {}".format(e))
            with _container_lock:
                _container.obj = None
            return

        record_into_rollback()

        if log:
            with _state_lock:
                snapshot = deepcopy(rollback_properties)
            print_properties("Discord Presence Updated:{}".format(format_properties(snapshot)))

    def reset():
        global original_properties
        set(**original_properties)

    @presence_disabled
    def on_load():
        global rollback_properties
        with _state_lock:
            snapshot = deepcopy(rollback_properties)
        print_rollback("Discord Presence has been loaded from a save file:{}".format(format_properties(snapshot)))
        set(log=False, **snapshot)

    @presence_disabled
    def rollback_check():
        global no_rollback, rollback_properties
        with _state_lock:
            mismatch = no_rollback.properties != rollback_properties
            snapshot = deepcopy(rollback_properties)
        if mismatch:
            print_rollback("Discord Presence does not match during this interaction. It is restored from the rollbackable variable:{}".format(format_properties(snapshot)))
            set(log=False, **snapshot)

    @presence_disabled
    def clear():
        global no_rollback
        with _state_lock:
            no_rollback.properties = {}
        record_into_rollback()
        with _container_lock:
            obj = _container.obj
        if obj is not None:
            obj.clear()

    def close():
        _watchdog_stop.set()
        with _container_lock:
            obj = _container.obj
            _container.obj = None
        if obj is None:
            return
        print_important("Closing DRP connection.")
        try:
            obj.clear()
            obj.close()
        except Exception as e:
            print_important("Error during close (connection may have already dropped): {}".format(e))
        print_important("Successfully closed.")

    @renpy.pure
    class Set(Action):

        def __init__(self, **properties):
            self.properties = properties

        def __call__(self):
            set(**self.properties)
            renpy.restart_interaction()

        def get_sensitive(self):
            with _container_lock:
                connected = _container.obj is not None
            return connected and store.persistent.discord_enabled

        def get_selected(self):
            global rollback_properties
            with _state_lock:
                snapshot = deepcopy(rollback_properties)
            if "start" in snapshot:
                a = deepcopy(self.properties)
                if "start" not in self.properties:
                    a["start"] = "start_time"
                return a == snapshot
            return self.properties == snapshot

    @renpy.pure
    class Update(Action):

        def __init__(self, **properties):
            self.properties = properties

        def __call__(self):
            update(**self.properties)
            renpy.restart_interaction()

        def get_sensitive(self):
            with _container_lock:
                connected = _container.obj is not None
            return connected and store.persistent.discord_enabled

        def get_selected(self):
            global rollback_properties
            with _state_lock:
                snapshot = deepcopy(rollback_properties)
            if "start" in snapshot:
                a = deepcopy(self.properties)
                if "start" not in self.properties:
                    a["start"] = "start_time"
                return a == snapshot
            return self.properties == snapshot

    class TogglePresence(Action):

        def __call__(self):
            store.persistent.discord_enabled = not store.persistent.discord_enabled
            if not store.persistent.discord_enabled:
                with _container_lock:
                    obj = _container.obj
                if obj is not None:
                    try:
                        obj.clear()
                    except Exception:
                        pass
            else:
                with _container_lock:
                    obj = _container.obj
                if obj is not None:
                    set(**original_properties)
            renpy.restart_interaction()

        def get_selected(self):
            return bool(store.persistent.discord_enabled)

default discord.rollback_properties = {}