image splashscreen_image_1 = "resources/images/gui/branding/splashscreen_image_1.png"
image splashscreen_image_2 = "resources/images/gui/branding/splashscreen_image_2.png"
image splashscreen_image_3 = "resources/images/gui/branding/splashscreen_image_3.png"
image splashscreen_image_4 = "resources/images/gui/branding/splashscreen_image_4.png"

label splashscreen:

    $ apply_system_titlebar()

    play music bgm_title_intro

    show splashscreen_image_1 at true_center with dissolve
    with Pause(2.5)
    hide splashscreen_image_1 with dissolve
    with Pause(0.5)

    show splashscreen_image_2 at true_center with dissolve
    with Pause(2.5)
    hide splashscreen_image_2 with dissolve
    with Pause(0.5)

    show splashscreen_image_3 at true_center with dissolve
    with Pause(2.5)
    hide splashscreen_image_3 with dissolve
    with Pause(0.5)

    show splashscreen_image_4 at true_center with dissolve
    with Pause(2.5)
    hide splashscreen_image_4 with dissolve
    with Pause(0.5)

    return
