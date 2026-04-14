screen confirm(message, yes_action, no_action):

    modal True

    zorder 200

    style_prefix "confirm"

    add "resources/images/gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    key "game_menu" action no_action
