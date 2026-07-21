screen navigation(nav_style_prefix="navigation", current_screen=""):

    if main_menu:
        $ _nav_items = [(_("Return"), Return(), "")]
    else:
        $ _nav_items = [
            (_("Return"), Return(), ""),
            (_("Save"), ShowMenu("save"), "save"),
            (_("Load"), ShowMenu("load"), "load"),
            (_("Achievements"), ShowMenu("achievements"), "achievements"),
            (_("Preferences"), ShowMenu("preferences"), "preferences"),
            (_("Main Menu"), MainMenu(), ""),
        ]

    vbox:
        style_prefix nav_style_prefix
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        for _nav_index, (_nav_label, _nav_action, _nav_screen) in enumerate(_nav_items):
            if nav_style_prefix == "main_menu_nav":
                textbutton _nav_label action _nav_action selected (_nav_screen == current_screen) at main_menu_nav_grow, main_menu_nav_shine, mm_slide_left_back_out(0.1 * (_nav_index + 1))
            else:
                textbutton _nav_label action _nav_action selected (_nav_screen == current_screen)