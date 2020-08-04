import time

from ..utils import parse_words_as_integer, delay
from talon.voice import Context, Key, Str, press

ctx = Context("firefox", bundle="org.mozilla.firefox")

# NOTE: run: bind --mode=ignore <Esc> composite unfocus | mode ignore


def focus_address_bar(m=None):
    press("cmd-l")


# Return focus from the devtools to the page
def refocus_page(m=None):
    focus_address_bar()
    time.sleep(0.1)
    # Escape button
    # This leaves the focus on the page at previous tab focused point, not the beginning of the page
    press("tab")


def back(m):
    # refocus_page(None)
    # press("cmd-[")
    press("escape")
    press("cmd-left")
    # refocus_page(None)


def forward(m):
    # refocus_page(None)
    # press("cmd-]")
    press("escape")
    press("cmd-right")
    # refocus_page(None)


def link(m):
    press("cmd-l")
    press("cmd-c")


def command_line(command):
    def function(m):
        refocus_page()
        press("escape", wait=2000)
        press("escape", wait=2000)
        press("escape", wait=2000)
        time.sleep(0.1)
        press(":", wait=2000)
        time.sleep(0.1)
        for character in command:
            press(character, wait=2000)
        # Str(command)(None)
        time.sleep(0.25)
        press("enter", wait=2000)

    return function


ctx.keymap(
    {
        "be bar": focus_address_bar,
        "copy url": Key("escape y y"),
        "go back": back,
        "go forward": forward,
        "refresh": Key("cmd-r"),
        "hard refresh": Key("cmd-shift-r"),
        "(last | prevous)": Key("cmd-shift-g"),
        "(reopen | unclose) tab": Key("cmd-shift-t"),
        # Developer tools
        "show counsel [panel]": Key("cmd-alt-k"),
        "toggle tools": Key("cmd-alt-i"),
        "toggle inspect": Key("shift-cmd-c"),
        "show debugger [panel]": Key("cmd-alt-z"),
        "show network [panel]": Key("cmd-alt-e"),
        # Breakpoints
        "break toggle": Key("cmd-\\"),
        "break step": Key("cmd-'"),
        "(refocus | focus) page": refocus_page,
        "(refocus | focus) page": refocus_page,
        # "[refocus] dev tools": open_focus_devtools,
        # Clipboard
        "cut": Key("cmd-x"),
        # "paste": Key("cmd-v"),
        "paste same style": Key("cmd-alt-shift-v"),
        # extensions
        "copy link": [delay(0.05), Key("cmd-l"), delay(0.05), Key("cmd-c")],
    }
)
