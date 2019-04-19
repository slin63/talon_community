from talon.voice import Context, Key

ctx = Context("navigation")

keymap = {
    # scrolling
    "(scroll down | spoon) ": [Key("down")] * 30,
    "(scroll up | spear)": [Key("up")] * 30,
    # NB home and end do not work in all apps
    "(scroll way down | doomway)": Key("cmd-down"),
    "(scroll way up | jeepway)": Key("cmd-up"),
    "(page up | puppy)": [Key("pageup")],
    "(page down | pupper)": [Key("pagedown")],
    "return": Key("cmd-right enter"),
    # searching
    "(search | marco)": Key("cmd-f"),
    "marneck": Key("cmd-g"),
    "marpreev": Key("cmd-shift-g"),
    "marthis": [Key("alt-right"), Key("shift-alt-left"), Key("cmd-f"), Key("enter")],
}

ctx.keymap(keymap)
