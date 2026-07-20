define config.name = _("Furorida Academia")
define gui.show_name = True
define config.version = "0.1.0"
define build.name = "FuroridaAcademia"

define config.has_autosave = False
define config.has_quicksave = False
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.main_menu_music = bgm_title_loop

define config.enter_transition = Dissolve(0.1)
define config.exit_transition = Dissolve(0.1)
define config.intra_transition = Dissolve(0.1)
define config.after_load_transition = None
define config.end_game_transition = None

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

define config.image_cache_size = 32
define config.predict_statements = 20

default preferences.text_cps = 35
default preferences.afm_time = 15
default persistent.discord_enabled = True
default preferences.skip_unseen = True

define config.save_directory = "FuroridaAcademia"
define config.window_icon = "resources/images/gui/branding/window_icon.png"

init python:
    config.searchpath += ["resources/images"]
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.documentation('*.html')
    build.documentation('*.txt')
