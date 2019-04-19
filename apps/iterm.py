from talon.voice import Key, Context

ctx = Context("iterm", bundle="com.googlecode.iterm2")

keymap = {
    "broadcaster": Key("cmd-alt-i"),
    "password": Key("cmd-alt-f"),

    # Pane creation and navigation
    "split horizontal": Key("cmd-d"),
    "split vertical": Key("cmd-shift-d"),
    "pane next": Key("cmd-]"),
    "pane last": Key("cmd-["),
}

ctx.keymap(keymap)
