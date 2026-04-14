init python:
    def volume_percent(mixer):
        v = _preferences.get_volume(mixer)
        if v <= 0.0:
            return 0
        return min(100, int(round(v * 100)))

    def delete_all_saves():
        for slot in renpy.list_slots(None):
            renpy.unlink_save(slot)
        renpy.notify(_("All saves deleted."))

    def is_fullscreen():
        return renpy.game.preferences.fullscreen

    _keybind_defaults = {
        "toggle_fullscreen": "K_f",
        "dismiss": "K_RETURN",
        "toggle_auto_forward": "K_a",
        "quick_save": "K_F5",
        "quick_load": "K_F9",
        "screenshot": "K_s",
        "game_menu": "K_ESCAPE",
    }

    _KEY_NICE_NAMES = {
        "SPACE": "Space", "RETURN": "Enter", "KP_ENTER": "Num Enter",
        "PAGEUP": "PgUp", "PAGEDOWN": "PgDn",
        "ESCAPE": "Esc", "BACKSPACE": "Bksp",
        "DELETE": "Del", "INSERT": "Ins",
        "UP": "↑", "DOWN": "↓", "LEFT": "←", "RIGHT": "→",
        "LCTRL": "Ctrl", "RCTRL": "Ctrl",
        "LSHIFT": "Shift", "RSHIFT": "Shift",
        "LALT": "Alt", "RALT": "Alt",
    }

    def _parse_key_spec(key_spec):
        for prefix in ("any_repeat_", "repeat_", "any_"):
            if not key_spec.startswith(prefix):
                continue
            key_spec = key_spec[len(prefix):]
            break

        parts = key_spec.rsplit("_K_", 1)
        if len(parts) == 2:
            mods_str, key = parts
            mod_parts = [m.capitalize() for m in mods_str.split("_") if m]
            key_label = _KEY_NICE_NAMES.get(key.upper(), key.replace("_", " ").capitalize())
            mod_prefix = " + ".join(mod_parts) + " + " if mod_parts else ""
            return mod_prefix + key_label

        if key_spec.startswith("K_"):
            k = key_spec[2:]
            return _KEY_NICE_NAMES.get(k.upper(), k.replace("_", " ").capitalize())

        return key_spec

    def get_key_display(action_name):
        keys = config.keymap.get(action_name, [])
        for k in keys:
            if k.startswith("K_") or "_K_" in k:
                return _parse_key_spec(k)

        default_spec = _keybind_defaults.get(action_name)
        if default_spec:
            return _parse_key_spec(default_spec)

        return "—"

define pref_keybind_actions = [
    (_("Toggle Fullscreen"), "toggle_fullscreen"),
    (_("Advance Dialogue"), "dismiss"),
    (_("Auto-Forward"), "toggle_auto_forward"),
    (_("Quick Save"), "quick_save"),
    (_("Quick Load"), "quick_load"),
    (_("Screenshot"), "screenshot"),
    (_("Open Menu"), "game_menu"),
]

screen preferences():

    tag menu

    use _menu_bg_secondary

    use game_menu(_("Preferences"), show_bg=False, show_overlay=False, nav_style_prefix="main_menu_nav", show_nav=False, show_title=False):

        vbox:
            spacing 10
            xoffset 10
            yoffset 8

            text _("Preferences") style "pref_screen_title"

            null height 10

            hbox:
                spacing 80

                vbox:
                    xsize 580
                    spacing 0

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window")     action Preference("display", "window")     selected (not is_fullscreen())
                        textbutton _("Fullscreen") action Preference("display", "fullscreen") selected is_fullscreen()

                    null height 20

                    vbox:
                        style_prefix "slider"

                        if config.has_music:
                            label _("Music Volume")
                            hbox:
                                spacing 14
                                bar value Preference("music volume") xsize 380
                                text "{}%".format(volume_percent('music')) style "pref_percent_text" yalign 0.5

                        if config.has_sound:
                            label _("SFX Volume")
                            hbox:
                                spacing 14
                                bar value Preference("sound volume") xsize 380
                                text "{}%".format(volume_percent('sfx')) style "pref_percent_text" yalign 0.5
                                if config.sample_sound:
                                    textbutton _("Test") action Play("sound", config.sample_sound)

                        if config.has_voice:
                            label _("Voice Volume")
                            hbox:
                                spacing 14
                                bar value Preference("voice volume") xsize 380
                                text "{}%".format(volume_percent('voice')) style "pref_percent_text" yalign 0.5
                                if config.sample_voice:
                                    textbutton _("Test") action Play("voice", config.sample_voice)

                    null height 20

                    vbox:
                        style_prefix "check"
                        label _("Miscellaneous")
                        textbutton _("Discord Rich Presence") action discord.TogglePresence()

                vbox:
                    xsize 580
                    spacing 0

                    vbox:
                        style_prefix "pref"
                        label _("Key Bindings")

                    null height 6

                    for bind_label, bind_action in pref_keybind_actions:
                        $ key_disp = get_key_display(bind_action)

                        hbox:
                            style "keybind_row"
                            xfill True
                            spacing 10

                            text _(bind_label) style "keybind_action_text" yalign 0.5 xfill True
                            text key_disp style "keybind_key_text" yalign 0.5 xminimum 120 xalign 1.0
