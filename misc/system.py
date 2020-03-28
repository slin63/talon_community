from talon.voice import Context, Key
import os

ctx = Context("system")

ctx.keymap(
    {
        "(prefies | preferences)": Key("cmd-,"),
    }
)
