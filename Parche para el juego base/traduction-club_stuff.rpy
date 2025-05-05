# by Traduction Club!

default persistent.language = None

label splashscreen:
    if persistent.language == None:
        call screen choose_language

screen choose_language():
    default local_lang = _preferences.language
    default chosen_lang = _preferences.language

    modal True
    style_prefix "radio"

    add "gui/overlay/confirm.png"

    frame:
        style "confirm_frame"

        vbox:
            xalign .5
            yalign .5
            xsize 760
            spacing 30

            label _("Please select a language"):
                style "confirm_prompt"
                xalign 0.5

            vbox:
                style_prefix "radio"
                label _("Language")

                # Real languages should go in alphabetical order by English name.
                textbutton "English" text_font "DejaVuSans.ttf" action [
                    Language(None),
                    SetField(persistent, "language", "english"),
                    SetScreenVariable("chosen_lang", "english"),
                    Show("dialog", message="It is recommended to restart to apply the changes.", ok_action=Quit())
                ]
                textbutton "Español" text_font "DejaVuSans.ttf" action [
                    Language("spanish"),
                    SetField(persistent, "language", "spanish"),
                    SetScreenVariable("chosen_lang", "spanish"),
                    Show("dialog", message="Se recomienda reiniciar el juego\npara aplicar los cambios.", ok_action=Quit())
                ]

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action [
                    Language(None),
                    SetField(persistent, "language", "english"),
                    SetScreenVariable("chosen_lang", "english"),
                    Show("dialog", message="It is recommended to restart to apply the changes.", ok_action=[Hide("dialog"), Return()])
                    ] style "ok_button_custom"

# to define the 'OK' buton
style ok_button_custom is button:
    background None
    foreground None
    hover_background None
    hover_foreground None
    insensitive_background None
    insensitive_foreground None

screen dialog(message, ok_action):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action