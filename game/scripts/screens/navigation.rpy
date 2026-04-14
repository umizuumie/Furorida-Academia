screen navigation(nav_style_prefix="navigation"):

    vbox:
        style_prefix nav_style_prefix
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if not main_menu:
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")

        if not main_menu:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("Quit") action Quit(confirm=True)
