screen _menu_bg_secondary(play_intro=True):
    add "resources/images/gui/backgrounds/bg_gradient_secondary.png"
    add "resources/images/gui/backgrounds/bg_pattern_sakuraheart_secondary.png" at scroll_bg
    if play_intro:
        add "resources/images/gui/backgrounds/bg_overlay_sidebar.png" at mm_slide_left_easeout(0.0)
    else:
        add "resources/images/gui/backgrounds/bg_overlay_sidebar.png"

screen save():
    tag menu
    use _menu_bg_secondary
    use file_slots(_("Save"), "save")

screen load():
    tag menu
    use _menu_bg_secondary
    use file_slots(_("Load"), "load")

screen file_slots(title, current_screen=""):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"))

    use game_menu(title, show_bg=False, show_overlay=False, nav_style_prefix="main_menu_nav", show_nav=True, show_title=False, current_screen=current_screen):

        vbox:
            spacing 5
            xoffset 10

            text title style "pref_screen_title"

            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            grid gui.file_slot_cols gui.file_slot_rows:
                xalign 0.5
                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1

                    fixed:
                        xsize gui.slot_button_width
                        ysize gui.slot_button_height

                        button:
                            style "slot_button"
                            xfill True
                            yfill True
                            action FileAction(slot)

                            has vbox

                            add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                        if FileLoadable(slot):
                            imagebutton:
                                xalign 1.0
                                yalign 1.0
                                xoffset -8
                                yoffset -8
                                idle Transform("resources/images/gui/button/icon_delete.png", alpha=0.6)
                                hover Transform("resources/images/gui/button/icon_delete.png", alpha=1.0)
                                action FileDelete(slot)

            hbox:
                style_prefix "page"
                xalign 0.5
                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()
                key "save_page_prev" action FilePagePrevious()

                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()
                key "save_page_next" action FilePageNext()