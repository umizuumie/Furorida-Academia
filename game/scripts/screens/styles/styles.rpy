init offset = -2

init python:
    class _DesignSystem:

        COLOR_PRIMARY       = "#F28CAB"
        COLOR_PRIMARY_HOVER = "#F9C4D2"
        COLOR_PRIMARY_FADED = "#F28CAB4f"
        COLOR_ACCENT        = "#7DD6DF"
        COLOR_TEXT          = "#FDEEF3"
        COLOR_TEXT_FADED    = "#FDEEF380"

        COLOR_SHADOW_PINK      = "#52153E"
        COLOR_SHADOW_PINK_DEEP = "#290A1F"
        COLOR_SHADOW_BLUE      = "#153352"
        COLOR_SHADOW_BLUE_DEEP = "#0A1929"

        COLOR_SLOT_BASE     = "#4d8a8a"
        COLOR_SLOT_HOVER    = "#5ba3a3"
        COLOR_SLOT_SELECTED = "#3d7070"

        FONT_DISPLAY = "resources/fonts/sp_marker.otf"
        FONT_BODY    = "resources/fonts/sunday_pizza.otf"

        SIZE_SCREEN_TITLE = 72
        SIZE_NAV          = 42
        SIZE_LABEL        = 34
        SIZE_BODY         = 30
        SIZE_SMALL_BODY   = 28
        SIZE_SMALL        = 26

        OUTLINE_TITLE     = [(3, "#52153E", 0, 0), (5, "#290A1F", 2, 2)]
        OUTLINE_LABEL     = [(2, "#52153E", 0, 0), (3, "#290A1F", 1, 1)]
        OUTLINE_BODY      = [(1, "#52153E", 0, 0), (2, "#290A1F", 0, 0)]
        OUTLINE_ACCENT    = [(1, "#153352", 0, 0), (2, "#0A1929", 0, 0)]
        OUTLINE_NAV_HOVER = [(3, "#153352", 0, 0), (5, "#0A1929", 2, 2)]

    ds = _DesignSystem()

################################################################################
## Base Element Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")
    background "resources/images/gui/button/[prefix_]background.png"
    hover_sound sfx_gui_hover
    activate_sound sfx_gui_press

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar  Frame("resources/images/gui/bar/left.png",   gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("resources/images/gui/bar/right.png",  gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar    Frame("resources/images/gui/bar/top.png",    gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("resources/images/gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("resources/images/gui/scrollbar/horizontal_[prefix_]bar.png",   gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb    Frame("resources/images/gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("resources/images/gui/scrollbar/vertical_[prefix_]bar.png",   gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb    Frame("resources/images/gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("resources/images/gui/slider/horizontal_[prefix_]bar.png",  gui.slider_borders, tile=gui.slider_tile)
    thumb          "resources/images/gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("resources/images/gui/slider/vertical_[prefix_]bar.png",  gui.vslider_borders, tile=gui.slider_tile)
    thumb          "resources/images/gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding    gui.frame_borders.padding
    background Frame("resources/images/gui/game/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## Design System Primitives
################################################################################

style ds_screen_title:
    font ds.FONT_DISPLAY
    size ds.SIZE_SCREEN_TITLE
    color ds.COLOR_PRIMARY
    outlines ds.OUTLINE_TITLE
    xalign 0.0
    bottom_margin 8
    left_padding 8
    right_padding 10
    top_padding 8
    bottom_padding 10

style ds_body_text:
    font ds.FONT_BODY
    size ds.SIZE_BODY
    color ds.COLOR_TEXT
    outlines ds.OUTLINE_BODY

style ds_body_primary_text is ds_body_text:
    color ds.COLOR_PRIMARY

style ds_body_accent_text is ds_body_text:
    color ds.COLOR_ACCENT
    outlines ds.OUTLINE_ACCENT

style ds_body_interactive_text is ds_body_text:
    hover_color      ds.COLOR_PRIMARY_HOVER
    selected_color   ds.COLOR_ACCENT
    insensitive_color ds.COLOR_TEXT_FADED

style ds_nav_button_text:
    font ds.FONT_DISPLAY
    size ds.SIZE_NAV
    xalign 0.0
    color ds.COLOR_PRIMARY
    hover_color ds.COLOR_ACCENT
    insensitive_color ds.COLOR_PRIMARY_FADED
    outlines ds.OUTLINE_TITLE
    hover_outlines ds.OUTLINE_NAV_HOVER

################################################################################
## Say Screen Styles
################################################################################

style window is default:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("resources/images/gui/game/textbox.png", xalign=0.5, yalign=1.0)

style namebox is default:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("resources/images/gui/game/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label is default:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue is default:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    adjust_spacing False

style say_thought is say_dialogue
style namebox_label is say_label

################################################################################
## Input Screen Styles
################################################################################

style input_prompt is default:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

################################################################################
## Choice Screen Styles
################################################################################

style choice_vbox is vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    background "resources/images/gui/button/choice_[prefix_]background.png"

style choice_button_text is default:
    properties gui.text_properties("choice_button")

################################################################################
## Navigation Screen Styles
################################################################################

style navigation_button is gui_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    background "resources/images/gui/button/[prefix_]background.png"

style navigation_button_text is gui_button_text:
    properties gui.text_properties("navigation_button")

################################################################################
## Game Menu Screen Styles
################################################################################

style game_menu_outer_frame is empty:
    bottom_padding 45
    top_padding 180
    background "resources/images/gui/overlay/game_menu.png"

style game_menu_navigation_frame is empty:
    xsize 420
    yfill True

style game_menu_content_frame is empty:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport is gui_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side is gui_side:
    spacing 15

style game_menu_label is gui_label:
    xpos 75
    ysize 180

style game_menu_label_text is gui_label_text:
    font ds.FONT_DISPLAY
    size 75
    color ds.COLOR_ACCENT
    outlines ds.OUTLINE_TITLE
    yalign 0.5

style return_button is navigation_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

style return_button_text is navigation_button_text

################################################################################
## File Slots Screen Styles
################################################################################

style page_label is gui_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text is gui_label_text:
    font ds.FONT_DISPLAY
    size ds.SIZE_LABEL
    color ds.COLOR_PRIMARY
    hover_color ds.COLOR_ACCENT
    outlines ds.OUTLINE_LABEL
    textalign 0.5
    layout "subtitle"

style page_button is gui_button:
    properties gui.button_properties("page_button")
    background "resources/images/gui/button/[prefix_]background.png"

style page_button_text is gui_button_text:
    font ds.FONT_DISPLAY
    size ds.SIZE_SMALL_BODY
    color ds.COLOR_PRIMARY
    hover_color ds.COLOR_ACCENT
    selected_color ds.COLOR_ACCENT
    insensitive_color ds.COLOR_PRIMARY_FADED
    outlines ds.OUTLINE_LABEL
    hover_outlines ds.OUTLINE_NAV_HOVER

style slot_button is gui_button:
    properties gui.button_properties("slot_button")
    background          Solid(ds.COLOR_SLOT_BASE)
    hover_background    Solid(ds.COLOR_SLOT_HOVER)
    selected_background Solid(ds.COLOR_SLOT_SELECTED)

style slot_button_text is ds_body_text:
    xalign 0.5
    textalign 0.5

style slot_time_text is slot_button_text:
    size ds.SIZE_SMALL
    color ds.COLOR_TEXT_FADED

style slot_name_text is slot_button_text:
    size ds.SIZE_SMALL_BODY
    color ds.COLOR_PRIMARY
    outlines ds.OUTLINE_LABEL

################################################################################
## Confirm Screen Styles
################################################################################

style confirm_frame is gui_frame:
    background Frame("resources/images/gui/game/frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign 0.5
    yalign 0.5

style confirm_prompt is gui_prompt

style confirm_prompt_text is gui_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button is gui_medium_button:
    properties gui.button_properties("confirm_button")
    background "resources/images/gui/button/[prefix_]background.png"

style confirm_button_text is gui_medium_button_text:
    properties gui.text_properties("confirm_button")

################################################################################
## Notify Screen Styles
################################################################################

style notify_frame is empty:
    ypos gui.notify_ypos
    background Frame("resources/images/gui/game/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text is gui_text:
    properties gui.text_properties("notify")

################################################################################
## Skip Indicator Screen Styles
################################################################################

style skip_frame is empty:
    ypos gui.skip_ypos
    background Frame("resources/images/gui/game/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text is gui_text:
    size gui.notify_text_size

style skip_triangle is skip_text:
    font "DejaVuSans.ttf"

################################################################################
## Quick Menu Screen Styles
################################################################################

style quick_menu is hbox:
    xalign 0.5
    yalign 0.99

style quick_button is default:
    properties gui.button_properties("quick_button")
    background "resources/images/gui/button/quick_[prefix_]background.png"

style quick_button_text is button_text:
    properties gui.text_properties("quick_button")

################################################################################
## Main Menu Screen Styles
################################################################################

style main_menu_frame is empty:
    xsize 420
    yfill True
    background "resources/images/gui/overlay/main_menu.png"

style main_menu_vbox is vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text is gui_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title is main_menu_text:
    properties gui.text_properties("title")

style main_menu_version is main_menu_text:
    font gui.interface_text_font
    size ds.SIZE_SMALL_BODY
    color ds.COLOR_PRIMARY
    outlines ds.OUTLINE_LABEL
    xalign 1.0
    xoffset -24
    yalign 1.0
    yoffset -24

style main_menu_nav_button is button:
    background None
    hover_background None
    xminimum 280
    padding (0, 4)

style main_menu_nav_button_text is ds_nav_button_text

################################################################################
## Preferences Screen Styles
################################################################################

style pref_screen_title is ds_screen_title

style pref_label is gui_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text is gui_label_text:
    yalign 1.0
    font ds.FONT_DISPLAY
    size ds.SIZE_LABEL
    color ds.COLOR_PRIMARY
    outlines ds.OUTLINE_LABEL
    left_padding 4
    right_padding 6
    top_padding 4
    bottom_padding 6

style pref_body_text is ds_body_text

style pref_percent_text is ds_body_primary_text:
    size ds.SIZE_SMALL
    min_width 54

style pref_desc_frame is frame:
    background Solid("#00000014")
    ysize 130
    padding (20, 12)

style pref_desc_text is ds_body_text:
    size ds.SIZE_SMALL_BODY
    xfill True
    yalign 0.5

style pref_vbox is vbox:
    xsize 338

style radio_label is pref_label
style radio_label_text is pref_label_text

style radio_button is gui_button:
    properties gui.button_properties("radio_button")
    background "resources/images/gui/button/[prefix_]background.png"
    foreground "resources/images/gui/button/radio_[prefix_]foreground.png"

style radio_button_text is ds_body_interactive_text:
    xalign 0.0

style radio_vbox is pref_vbox:
    spacing gui.pref_button_spacing

style pref_resolution_frame is frame:
    background Solid("#00000014")
    padding (14, 10)

style pref_resolution_button is button:
    padding (2, 4)
    background None
    hover_background None
    selected_idle_background None
    selected_hover_background None

style pref_resolution_button_text is ds_body_interactive_text:
    size ds.SIZE_SMALL
    insensitive_color ds.COLOR_PRIMARY_FADED
    xalign 0.0

style check_label is pref_label
style check_label_text is pref_label_text

style check_button is gui_button:
    properties gui.button_properties("check_button")
    background "resources/images/gui/button/[prefix_]background.png"
    foreground "resources/images/gui/button/check_[prefix_]foreground.png"

style check_button_text is ds_body_interactive_text:
    xalign 0.0

style check_vbox is pref_vbox:
    spacing gui.pref_button_spacing

style slider_label is pref_label
style slider_label_text is pref_label_text

style slider_slider is gui_slider:
    xsize 525

style slider_button is gui_button:
    properties gui.button_properties("slider_button")
    background "resources/images/gui/button/[prefix_]background.png"
    yalign 0.5
    left_margin 15

style slider_button_text is gui_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox is pref_vbox:
    xsize 675

style slider_pref_vbox is pref_vbox
style mute_all_button is check_button
style mute_all_button_text is check_button_text

style keybind_row is hbox:
    ypadding 3

style keybind_action_text is ds_body_text:
    size ds.SIZE_SMALL_BODY
    yalign 0.5

style keybind_key_text is ds_body_accent_text:
    size ds.SIZE_SMALL
    xalign 1.0