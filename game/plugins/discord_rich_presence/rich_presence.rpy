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

    import time as _time
    import threading

    _container = _PresenceContainer()
    _watchdog_stop = threading.Event()

    def _try_connect():
        asyncio.set_event_loop(asyncio.new_event_loop())
        _max_retries = 6
        _retry_delay = 2.0

        for _attempt in range(1, _max_retries + 1):
            try:
                print_important("Attempting to connect to Discord Rich Presence... (attempt {}/{})".format(_attempt, _max_retries))
                obj = pypresence.Presence(application_id)
                obj.connect()
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
                    _time.sleep(_retry_delay)
                else:
                    print_important("All {} attempts failed.".format(_max_retries))
                    return False

    def _watchdog_thread():
        global original_properties, rollback_properties

        connected = _try_connect()
        if connected:
            set(**original_properties)

        while not _watchdog_stop.wait(timeout=15.0):

            if not store.persistent.discord_enabled:
                if _container.obj is not None:
                    try:
                        _container.obj.clear()
                    except Exception:
                        pass
                continue

            if _container.obj is not None:
                try:
                    _container.obj.update(**clean_properties(no_rollback.properties)) if no_rollback.properties else None
                    continue
                except Exception:
                    print_important("Discord Rich Presence connection lost. Attempting to reconnect...")
                    _container.obj = None

            try:
                obj = pypresence.Presence(application_id)
                obj.connect()
                _container.obj = obj
                print_important("Reconnected to Discord Rich Presence.")
                current = rollback_properties if rollback_properties else original_properties
                set(**current)
            except Exception as e:
                print_important("Reconnect attempt failed: {}".format(e))

    _connection_thread = threading.Thread(target=_watchdog_thread, daemon=True)
    _connection_thread.start()

    import atexit
    def _atexit_close():
        obj = _container.obj
        if obj is None:
            return
        try:
            obj.clear()
            obj.close()
        except Exception:
            pass
    atexit.register(_atexit_close)

    import time

    start_time = time.time()

    from copy import deepcopy

    def presence_disabled(func):
        def wrapper(*args, **kwargs):
            if _container.obj is None:
                return None
            if not store.persistent.discord_enabled:
                return None
            return func(*args, **kwargs)
        wrapper.__name__ = func.__name__
        return wrapper

    def return_none(*_args, **_kwargs): pass

    def record_into_rollback():
        global no_rollback, rollback_properties
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
        no_rollback.properties = deepcopy(props)

        try:
            _container.obj.update(**clean_properties(no_rollback.properties))
        except Exception as e:
            print_important("Discord Presence lost connection during set: {}".format(e))
            _container.obj = None
            return

        record_into_rollback()

        if log:
            print_properties("Discord Presence Set:{}".format(format_properties(rollback_properties)))

    @presence_disabled
    def update(log=True, **props):
        if "start" in props:
            if props["start"] == "new_time":
                props["start"] = time.time()

        global no_rollback
        for p in props:
            no_rollback.properties[p] = props[p]

        try:
            _container.obj.update(**clean_properties(no_rollback.properties))
        except Exception as e:
            print_important("Discord Presence lost connection during update: {}".format(e))
            _container.obj = None
            return

        record_into_rollback()

        if log:
            print_properties("Discord Presence Updated:{}".format(format_properties(rollback_properties)))

    def reset():
        global original_properties
        set(**original_properties)

    @presence_disabled
    def on_load():
        print_rollback("Discord Presence has been loaded from a save file:{}".format(format_properties(rollback_properties)))
        global rollback_properties
        set(log=False, **rollback_properties)

    @presence_disabled
    def rollback_check():
        global no_rollback, rollback_properties
        if no_rollback.properties != rollback_properties:
            print_rollback("Discord Presence does not match during this interaction. It is restored from the rollbackable variable:{}".format(format_properties(rollback_properties)))
            set(log=False, **rollback_properties)

    @presence_disabled
    def clear():
        global no_rollback
        no_rollback.properties = {}
        record_into_rollback()
        _container.obj.clear()

    def close():
        _watchdog_stop.set()
        if _container.obj is None:
            return
        print_important("Closing DRP connection.")
        try:
            _container.obj.clear()
            _container.obj.close()
        except Exception as e:
            print_important("Error during close (connection may have already dropped): {}".format(e))
        finally:
            _container.obj = None
        print_important("Successfully closed.")

    class RenPyDiscord(NoRollback):
        def __init__(self):
            self.properties = {}

    global original_properties, main_menu_state
    original_properties = deepcopy(main_menu_state)

    if not "start" in original_properties:
        original_properties["start"] = "start_time"

    from store import Action

    @renpy.pure
    class Set(Action):

        def __init__(self, **properties):
            self.properties = properties

        def __call__(self):
            set(**self.properties)
            renpy.restart_interaction()

        def get_sensitive(self):
            return _container.obj is not None

        def get_selected(self):
            global rollback_properties
            if "start" in rollback_properties:
                a = deepcopy(self.properties)
                if "start" not in self.properties:
                    a["start"] = "start_time"
                return a == rollback_properties
            return self.properties == rollback_properties

    @renpy.pure
    class Update(Action):

        def __init__(self, **properties):
            self.properties = properties

        def __call__(self):
            update(**self.properties)
            renpy.restart_interaction()

        def get_sensitive(self):
            return _container.obj is not None

        def get_selected(self):
            global rollback_properties
            if "start" in rollback_properties:
                a = deepcopy(self.properties)
                if "start" not in self.properties:
                    a["start"] = "start_time"
                return a == rollback_properties
            return self.properties == rollback_properties

    class TogglePresence(Action):

        def __call__(self):
            store.persistent.discord_enabled = not store.persistent.discord_enabled
            if not store.persistent.discord_enabled:
                if _container.obj is not None:
                    try:
                        _container.obj.clear()
                    except Exception:
                        pass
            else:
                if _container.obj is not None:
                    set(**original_properties)
            renpy.restart_interaction()

        def get_selected(self):
            return bool(store.persistent.discord_enabled)

define discord.no_rollback = discord.RenPyDiscord()
default discord.rollback_properties = {}
