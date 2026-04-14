## Position Transforms
transform center:
    xalign 0.5
    yalign 0.45

transform true_center:
    xalign 0.5
    yalign 0.5

transform top:
    xalign 0.5
    yalign -0.7

transform bottom:
    xalign 0.5
    yalign 1.7

transform center_left:
    xalign 0.37
    yalign 0.45

transform center_right:
    xalign 0.63
    yalign 0.45

transform left:
    xalign 0.14
    yalign 0.45

transform right:
    xalign 0.88
    yalign 0.45

transform off_left:
    xalign -0.4
    yalign 0.45

transform off_right:
    xalign 1.4
    yalign 0.45

## Animated Position Transforms
transform slide_in_center:
    bottom
    linear 0.2 true_center

transform slide_out_center:
    true_center
    linear 0.2 bottom

transform character_hpunch:
    xoffset -10
    linear 0.05 xoffset 40
    linear 0.05 xoffset -40
    linear 0.05 xoffset 40
    linear 0.05 xoffset -40
    linear 0.05 xoffset 40
    linear 0.05 xoffset -40
    linear 0.05 xoffset 10
    linear 0.05 xoffset 0

## Alpha Transforms
transform fade_in:
    alpha 0.0
    linear 0.3 alpha 1.0

transform fade_out:
    alpha 1.0
    linear 0.3 alpha 0.0