screen game_menu(title, scroll=None, yinitial=0.0, spacing=0, show_bg=True, show_overlay=True, nav_style_prefix="navigation", show_nav=True, show_title=True, current_screen=""):

    style_prefix "game_menu"

    if show_bg:
        add "resources/images/gui/backgrounds/bg_gradient_primary.png"
        add "resources/images/gui/backgrounds/bg_pattern_sakuraheart_primary.png" at scroll_bg

    frame:
        style "game_menu_outer_frame"
        background ("resources/images/gui/overlay/game_menu.png" if show_overlay else None)

        hbox:

            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        vbox:
                            spacing spacing
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        spacing spacing
                        transclude

                else:
                    transclude

    if show_nav:
        use navigation(nav_style_prefix, current_screen)
    elif nav_style_prefix == "main_menu_nav":
        textbutton _("Return"):
            style "main_menu_nav_button"
            action Return()
            xpos 80
            yalign 0.5
            at main_menu_nav_grow, main_menu_nav_shine, mm_slide_left_back_out(0.1)
    else:
        textbutton _("Return"):
            style "return_button"
            action Return()

    if show_title:
        label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")