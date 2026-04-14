screen say(who, what):

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    add SideImage() xalign 0.0 yalign 1.0


init python:
    if 'namebox' not in config.character_id_prefixes:
        config.character_id_prefixes.append('namebox')
