import time

from .. import utils
from .web import browser

from talon import ui
from talon.voice import Context, Key, Str, press

# It is recommended to use this script in tandem with Vimium, a Google Chrome plugin for controlling the browser via keyboard
# https://vimium.github.io/

context = Context("QuickTime", bundle="com.apple.QuickTimePlayerX")


context.keymap(
    {
        "new recording": Key("ctrl-cmd-n"),
    }
)
