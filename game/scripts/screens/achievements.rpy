screen achievements():

    tag menu

    add "resources/images/gui/backgrounds/bg_gradient_secondary.png"
    add "resources/images/gui/backgrounds/bg_pattern_sakuraheart_secondary.png" at scroll_bg

    add "resources/images/gui/backgrounds/bg_overlay_sidebar.png" at mm_slide_left_easeout(0.0)

    use game_menu(_("Achievements"), show_bg=False, show_overlay=False, nav_style_prefix="main_menu_nav", show_nav=True, show_title=False, current_screen="achievements"):

        vbox:
            spacing 10
            xoffset 10
            yoffset 8

            text _("Achievements") style "pref_screen_title"

            null height 10

            null