init python:
    def volume_percent(mixer):
        v = _preferences.volumes.get(mixer, 0.0)
        if not v or v <= 0.0:
            return 0
        return int(round(min(1.0, v) * 100))

    def delete_all_saves():
        for slot in renpy.list_slots():
            renpy.unlink_save(slot)
        renpy.notify(_("All saves deleted."))

    def reset_progress_data():
        persistent._clear(progress=True)
        renpy.notify(_("Progress data has been reset."))

    def reset_all_data():
        delete_all_saves()
        persistent._clear(progress=True)
        new_preferences = renpy.game.preferences.__class__()
        persistent._preferences = new_preferences
        renpy.game.preferences = new_preferences
        renpy.save_persistent()
        renpy.quit(relaunch=True)

    def is_fullscreen():
        return renpy.game.preferences.fullscreen

    def current_renderer_choice():
        if _preferences.renderer in ("gl2", "angle2", "gles2"):
            return _preferences.renderer
        return renpy.get_renderer_info().get("renderer")

    def current_window_size():
        return renpy.get_physical_size()

    def is_window_size(width, height):
        return not is_fullscreen() and current_window_size() == (width, height)

    def set_window_size(width, height):
        renpy.game.preferences.fullscreen = False
        renpy.set_physical_size((width, height))

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

    PREF_DESCRIPTIONS = {
        "display_window": _("Play the game in a resizable window."),
        "display_fullscreen": _("Play the game in fullscreen mode."),
        "renderer_angle2": _("Use the ANGLE2 rendering backend. Recommended for most Windows systems. Renderer changes are applied after a relaunch."),
        "renderer_gl2": _("Use the GL2 rendering backend. Try this if ANGLE2 causes display issues. Renderer changes are applied after a relaunch."),
        "music_volume": _("Adjust the volume of the background music."),
        "sfx_volume": _("Adjust the volume of sound effects, both from menus and in-game."),
        "sfx_test": _("Play a sample sound effect at the current volume."),
        "voice_volume": _("Adjust the volume of character voicelines."),
        "voice_test": _("Play a sample voice line at the current volume."),
        "discord_presence": _("Show your current game activity on your Discord profile."),
        "window_resolution": _("Set the game window to this resolution."),
        "reset_saves": _("Delete every save file. This cannot be undone."),
        "reset_progress": _("Reset tracked progress, such as seen text and images. Save files are not affected."),
        "reset_all": _("Delete every save file and reset all data. The game will restart."),
    }

define pref_window_presets = [
    (_("1920 x 1080"), 1920, 1080),
    (_("1600 x 900"), 1600, 900),
    (_("1366 x 768"), 1366, 768),
    (_("1280 x 720"), 1280, 720),
]

define pref_keybind_actions = [
    (_("Toggle Fullscreen"), "toggle_fullscreen"),
    (_("Advance Dialogue"), "dismiss"),
    (_("Auto-Forward"), "toggle_auto_forward"),
    (_("Quick Save"), "quick_save"),
    (_("Quick Load"), "quick_load"),
    (_("Screenshot"), "screenshot"),
    (_("Open Menu"), "game_menu"),
]

define pref_tab_content_height = 380

style pref_panel_frame is frame:
    background Solid("#ffffffBF")
    padding (30, 24)

style pref_tab_button is button:
    padding (26, 12)
    background None
    hover_background None
    selected_idle_background None
    selected_hover_background None

style pref_tab_button_text is button_text:
    font ds.FONT_DISPLAY
    size ds.SIZE_LABEL
    color ds.COLOR_PRIMARY
    hover_color ds.COLOR_PRIMARY_HOVER
    selected_color ds.COLOR_ACCENT
    outlines ds.OUTLINE_LABEL

screen preferences():

    tag menu

    default pref_tab = "display"
    default pref_desc = None

    use _menu_bg_secondary

    use game_menu(_("Preferences"), show_bg=False, show_overlay=False, nav_style_prefix="main_menu_nav", show_nav=True, show_title=False, current_screen="preferences"):

        vbox:
            spacing 10
            xoffset 10
            yoffset 8

            text _("Preferences") style "pref_screen_title"

            null height 10

            frame:
                style "pref_panel_frame"
                xsize 1120

                vbox:
                    spacing 0

                    hbox:
                        spacing 10

                        textbutton _("Display")       style "pref_tab_button" action SetScreenVariable("pref_tab", "display")  selected (pref_tab == "display")
                        textbutton _("Audio")         style "pref_tab_button" action SetScreenVariable("pref_tab", "audio")    selected (pref_tab == "audio")
                        textbutton _("Data")          style "pref_tab_button" action SetScreenVariable("pref_tab", "data")     selected (pref_tab == "data")
                        textbutton _("Miscellaneous") style "pref_tab_button" action SetScreenVariable("pref_tab", "misc")     selected (pref_tab == "misc")
                        textbutton _("Keybinds")      style "pref_tab_button" action SetScreenVariable("pref_tab", "keybinds") selected (pref_tab == "keybinds")

                    null height 6
                    frame:
                        background Solid(ds.COLOR_PRIMARY)
                        xfill True
                        ysize 2
                        padding (0, 0)
                    null height 20

                    fixed:
                        xfill True
                        ysize pref_tab_content_height

                        vbox:
                            spacing 0

                            if pref_tab == "display":

                                hbox:
                                    spacing 60

                                    vbox:
                                        style_prefix "radio"
                                        label _("Display")
                                        textbutton _("Window")     action [Preference("display", "window"), Function(renpy.restart_interaction)]     selected (not is_fullscreen()) hovered SetScreenVariable("pref_desc", PREF_DESCRIPTIONS["display_window"]) unhovered SetScreenVariable("pref_desc", None)
                                        textbutton _("Fullscreen") action Preference("display", "fullscreen") selected is_fullscreen() hovered SetScreenVariable("pref_desc", PREF_DESCRIPTIONS["display_fullscreen"]) unhovered SetScreenVariable("pref_desc", None)

                                        null height 10

                                        frame:
                                            style "pref_resolution_frame"

                                            vbox:
                                                style_prefix "radio"
                                                spacing 0

                                                timer 0.3 repeat True action NullAction()

                                                for res_label, res_width, res_height in pref_window_presets:
                                                    textbutton res_label style "pref_resolution_button" action Function(set_window_size, res_width, res_height) selected is_window_size(res_width, res_height) sensitive (not is_fullscreen()) hovered SetScreenVariable("pref_desc", PREF_DESCRIPTIONS["window_resolution"]) unhovered SetScreenVariable("pref_desc", None)

                                    vbox:
                                        style_prefix "check"
                                        label _("Renderer")
                                        textbutton _("ANGLE2 Renderer") action _SetRenderer("angle2") selected (current_renderer_choice() == "angle2") hovered SetScreenVariable("pref_desc", PREF_DESCRIPTIONS["renderer_angle2"]) unhovered SetScreenVariable("pref_desc", None)
                                        textbutton _("GL2 Renderer") action _SetRenderer("gl2") selected (current_renderer_choice() == "gl2") hovered SetScreenVariable("pref_desc", PREF_DESCRIPTIONS["renderer_gl2"]) unhovered SetScreenVariable("pref_desc", None)

                            elif pref_tab == "audio":

                                vbox:
                                    style_prefix "slider"

                                    if config.has_music:
                                        label _("Music Volume")
                                        hbox:
                                            spacing 14
                                            bar value Preference("music volume") xsize 500 hovered SetScreenVariable("pref_desc", PREF_DESCRIPTIONS["music_volume"]) unhovered SetScreenVariable("pref_desc", None)
                                            text "{}%".format(volume_percent('music')) style "pref_percent_text" yalign 0.5

                                    if config.has_sound:
                                        label _("SFX Volume")
                                        hbox:
                                            spacing 14
                                            bar value Preference("sound volume") xsize 500 hovered SetScreenVariable("pref_desc", PREF_DESCRIPTIONS["sfx_volume"]) unhovered SetScreenVariable("pref_desc", None)
                                            text "{}%".format(volume_percent('sfx')) style "pref_percent_text" yalign 0.5
                                            if config.sample_sound:
                                                textbutton _("Test") action Play("sound", config.sample_sound) hovered SetScreenVariable("pref_desc", PREF_DESCRIPTIONS["sfx_test"]) unhovered SetScreenVariable("pref_desc", None)

                                    if config.has_voice:
                                        label _("Voice Volume")
                                        hbox:
                                            spacing 14
                                            bar value Preference("voice volume") xsize 500 hovered SetScreenVariable("pref_desc", PREF_DESCRIPTIONS["voice_volume"]) unhovered SetScreenVariable("pref_desc", None)
                                            text "{}%".format(volume_percent('voice')) style "pref_percent_text" yalign 0.5
                                            if config.sample_voice:
                                                textbutton _("Test") action Play("voice", config.sample_voice) hovered SetScreenVariable("pref_desc", PREF_DESCRIPTIONS["voice_test"]) unhovered SetScreenVariable("pref_desc", None)

                            elif pref_tab == "data":

                                vbox:
                                    style_prefix "check"
                                    label _("Reset Data")

                                    null height 6

                                    textbutton _("Save Files") style "pref_resolution_button" action Confirm(_("Delete every save file? This cannot be undone."), Function(delete_all_saves)) hovered SetScreenVariable("pref_desc", PREF_DESCRIPTIONS["reset_saves"]) unhovered SetScreenVariable("pref_desc", None)
                                    textbutton _("Progress Data") style "pref_resolution_button" action Confirm(_("Reset tracked progress, such as seen text and images? Save files will not be affected."), Function(reset_progress_data)) hovered SetScreenVariable("pref_desc", PREF_DESCRIPTIONS["reset_progress"]) unhovered SetScreenVariable("pref_desc", None)
                                    textbutton _("All Data") style "pref_resolution_button" action Confirm(_("Delete every save file and reset all data? This cannot be undone and the game will restart."), Function(reset_all_data)) hovered SetScreenVariable("pref_desc", PREF_DESCRIPTIONS["reset_all"]) unhovered SetScreenVariable("pref_desc", None)

                            elif pref_tab == "misc":

                                vbox:
                                    style_prefix "check"
                                    textbutton _("Discord Rich Presence") action discord.TogglePresence() hovered SetScreenVariable("pref_desc", PREF_DESCRIPTIONS["discord_presence"]) unhovered SetScreenVariable("pref_desc", None)

                            elif pref_tab == "keybinds":

                                vbox:
                                    style_prefix "pref"
                                    label _("Key Bindings")

                                null height 6

                                for bind_label, bind_action in pref_keybind_actions:
                                    $ key_disp = get_key_display(bind_action)

                                    hbox:
                                        style "keybind_row"
                                        xsize 500
                                        spacing 10

                                        text _(bind_label) style "keybind_action_text" yalign 0.5 xfill True
                                        text key_disp style "keybind_key_text" yalign 0.5 xminimum 120 xalign 1.0

                    if pref_tab != "keybinds":

                        null height 14

                        frame:
                            style "pref_desc_frame"
                            xfill True

                            text (pref_desc or "") style "pref_desc_text"