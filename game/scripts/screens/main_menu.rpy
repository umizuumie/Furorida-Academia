transform main_menu_nav_grow:
    on hover:
        easein_expo 0.15 zoom 1.18
    on idle:
        easeout_expo 0.1 zoom 1.0
    on insensitive:
        easeout_expo 0.1 zoom 1.0

transform main_menu_nav_shine:
    on hover:
        matrixcolor BrightnessMatrix(0.18)
        easein_expo 2 matrixcolor BrightnessMatrix(0.0)
    on idle:
        easein_expo 2 matrixcolor BrightnessMatrix(0.0)
    on insensitive:
        easein_expo 2 matrixcolor BrightnessMatrix(0.0)

transform mm_slide_left_easeout(delay=0.0):
    subpixel True
    xoffset -1000
    pause delay
    easein_expo 0.55 xoffset 0

transform mm_slide_right_easeout(delay=0.0):
    subpixel True
    xoffset 1000
    pause delay
    easein_expo 0.9 xoffset 0

transform mm_slide_left_back_out(delay=0.0):
    subpixel True
    xoffset -1280
    pause delay
    easein_expo 0.65 xoffset 0

transform mm_logo_anim_1(delay=0.0):
    subpixel True
    rotate_pad False
    xanchor 0.5
    yanchor 0.5
    xpos 0.5
    ypos 0.5
    yoffset -1080
    pause delay
    easein_expo 0.8 yoffset 0
    block:
        ease 3.0 rotate 1.5
        ease 6.0 rotate -1.5
        ease 3.0 rotate 0.0
        repeat

transform mm_logo_anim_2(delay=0.0):
    subpixel True
    rotate_pad False
    xanchor 0.5
    yanchor 0.5
    xpos 0.5
    ypos 0.5
    yoffset -1080
    pause delay
    easein_expo 0.8 yoffset 0
    block:
        ease 3.5 rotate 1.5
        ease 6.5 rotate -1.5
        ease 3.5 rotate 0.0
        repeat

transform mm_logo_anim_3(delay=0.0):
    subpixel True
    rotate_pad False
    xanchor 0.5
    yanchor 0.5
    xpos 0.5
    ypos 0.5
    yoffset -1080
    pause delay
    easein_expo 0.8 yoffset 0
    block:
        ease 4.0 rotate 1.5
        ease 7.0 rotate -1.5
        ease 4.0 rotate 0.0
        repeat

init python:
    def scroll_bg_func(trans, st, at):
        cycle = 65.0
        t = st % cycle
        trans.xpos = -1920 + int(1920.0 * t / cycle)
        trans.ypos = -1080 + int(1080.0 * t / cycle)
        return 0

transform scroll_bg:
    xanchor 0
    yanchor 0
    function scroll_bg_func

transform mm_fade_in:
    alpha 0
    linear 0.1 alpha 1.0

transform mm_nav_faded:
    alpha 0.35

screen main_menu():

    tag menu

    add "resources/images/gui/backgrounds/bg_gradient_primary.png" at mm_fade_in
    add "resources/images/gui/backgrounds/bg_pattern_sakuraheart_primary.png" at scroll_bg, mm_fade_in

    add "resources/images/gui/backgrounds/bg_overlay_sidebar.png" at mm_slide_left_easeout(0.0)
    add "resources/images/gui/backgrounds/bg_overlay_paper_small.png" at mm_slide_left_back_out(0.5)
    add "resources/images/gui/backgrounds/bg_overlay_paper_medium.png" at mm_slide_left_back_out(0.35)
    add "resources/images/gui/backgrounds/bg_overlay_paper_large.png" at mm_slide_left_easeout(0.2)
    add "resources/images/gui/backgrounds/bg_overlay_logo_sakuraheart.png" at mm_logo_anim_1(0.4)
    add "resources/images/gui/backgrounds/bg_overlay_logo_floridabadge.png" at mm_logo_anim_3(0.45)
    add "resources/images/gui/backgrounds/bg_overlay_logo_text.png" at mm_logo_anim_2(0.35)

    vbox:
        style_prefix "main_menu_nav"
        xpos 80
        yalign 0.75
        spacing 4

        textbutton _("New Game") action Start() at main_menu_nav_grow, main_menu_nav_shine, mm_slide_left_back_out(0.1)

        if renpy.list_slots():
            textbutton _("Load Game") action ShowMenu("load") at main_menu_nav_grow, main_menu_nav_shine, mm_slide_left_back_out(0.2)
        else:
            textbutton _("Load Game") action None at mm_slide_left_back_out(0.2), mm_nav_faded

        textbutton _("Achievements") action ShowMenu("achievements") at main_menu_nav_grow, main_menu_nav_shine, mm_slide_left_back_out(0.3)
        textbutton _("Preferences") action ShowMenu("preferences") at main_menu_nav_grow, main_menu_nav_shine, mm_slide_left_back_out(0.4)
        textbutton _("Quit") action Quit(confirm=True) at main_menu_nav_grow, main_menu_nav_shine, mm_slide_left_back_out(0.5)

    text "{b}v" + config.version + "{/b}\n{size=22}{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]{/size}" at mm_slide_right_easeout:
        style "main_menu_version"
