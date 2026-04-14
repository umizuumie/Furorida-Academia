init offset = -2

init python:
    gui.init(1920, 1080)
    config.ftfont_scale["resources/fonts/sunday_pizza.otf"] = 1.2
    config.ftfont_scale["resources/fonts/sp_marker.otf"] = 0.9
    config.ftfont_vertical_extent_scale["resources/fonts/sunday_pizza.otf"] = 1.0
    config.ftfont_vertical_extent_scale["resources/fonts/sp_marker.otf"] = 1.0

define config.check_conflicting_properties = True

define gui.accent_color = '#2899A4'
define gui.idle_color = '#707070'
define gui.idle_small_color = '#606060'
define gui.hover_color = '#006666'
define gui.selected_color = '#555555'
define gui.insensitive_color = '#7070707f'
define gui.muted_color = '#66a3a3'
define gui.hover_muted_color = '#99c1c1'
define gui.text_color = '#404040'
define gui.interface_text_color = '#404040'

define gui.text_font = "resources/fonts/sunday_pizza.otf"
define gui.name_text_font = "resources/fonts/sp_marker.otf"
define gui.interface_text_font = "resources/fonts/sunday_pizza.otf"

define gui.text_size = 33
define gui.name_text_size = 45
define gui.interface_text_size = 33
define gui.label_text_size = 36
define gui.notify_text_size = 24
define gui.title_text_size = 75

define gui.main_menu_background = "resources/images/gui/backgrounds/main_menu.png"
define gui.game_menu_background = "resources/images/gui/backgrounds/game_menu.png"

define gui.textbox_height = 278
define gui.textbox_yalign = 1.0

define gui.name_xpos = 360
define gui.name_ypos = 10
define gui.name_xalign = 0.0

define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False

define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75
define gui.dialogue_width = 1116
define gui.dialogue_text_xalign = 0.0

define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0

define gui.radio_button_borders = Borders(27, 6, 6, 6)
define gui.check_button_borders = Borders(27, 6, 6, 6)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(15, 6, 15, 6)
define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#707070'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#7070707f'

define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

define config.thumbnail_width = 384
define config.thumbnail_height = 216

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

define gui.navigation_xpos = 60
define gui.skip_ypos = 15
define gui.notify_ypos = 68
define gui.choice_spacing = 33
define gui.navigation_spacing = 6
define gui.pref_spacing = 15
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.slot_spacing = 15
define gui.main_menu_text_xalign = 1.0

define gui.frame_borders = Borders(6, 6, 6, 6)
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.skip_frame_borders = Borders(24, 8, 75, 8)
define gui.notify_frame_borders = Borders(24, 8, 60, 8)
define gui.frame_tile = False

define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)
define gui.unscrollable = "hide"

define gui.language = "unicode"
