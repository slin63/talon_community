# from https://github.com/talonvoice/examples
# jsc added shift-click, command-click, and voice code compatibility

# import eye
import time
from talon import ctrl, tap
from talon.voice import Context, Key

ctx = Context("mouse")

x, y = ctrl.mouse_pos()
mouse_history = [(x, y, time.time())]
force_move = None


def on_move(typ, e):
    mouse_history.append((e.x, e.y, time.time()))
    if force_move:
        e.x, e.y = force_move
        return True


tap.register(tap.MMOVE, on_move)


def click_pos(m):
    word = m._words[0]
    start = (word.start + min((word.end - word.start) / 2, 0.100)) / 1000.0
    diff, pos = min([(abs(start - pos[2]), pos) for pos in mouse_history])
    return pos[:2]


def delayed_click(m, button=0, times=1):
    # old = eye.config.control_mouse
    # eye.config.control_mouse = False
    # x, y = click_pos(m)
    # ctrl.mouse(x, y)
    ctrl.mouse_click(x, y, button=button, times=times, wait=20)
    # ctrl.mouse_click(x, y, button=button, times=times, wait=2000)
    # time.sleep(0.032)
    # eye.config.control_mouse = old


# jsc added
def press_key_and_click(m, key, button=0, times=1):
    ctrl.key_press(key, down=True)
    ctrl.mouse_click(x, y, button=button, times=times, wait=16000)
    ctrl.key_press(key, up=True)


# jsc added
def shift_click(m, button=0, times=1):
    press_key_and_click(m, "shift", button, times)


def command_click(m, button=0, times=1):
    press_key_and_click(m, "cmd", button, times)


def delayed_right_click(m):
    delayed_click(m, button=1)


def delayed_dubclick(m):
    delayed_click(m, button=0, times=2)


def delayed_tripclick(m):
    delayed_click(m, button=0, times=3)


def mouse_scroll(amount):
    def scroll(m):
        ctrl.mouse_scroll(by_lines=False, y=amount)

    return scroll


def mouse_drag(m):
    x, y = click_pos(m)
    ctrl.mouse_click(x, y, down=True)


def mouse_release(m):
    x, y = click_pos(m)
    ctrl.mouse_click(x, y, up=True)


keymap = {
    # jsc modified with some voice-code compatibility
    "righty": delayed_right_click,
    "(click | joe)": delayed_click,
    "(dubclick | duke)": delayed_dubclick,
    "(sigh duke)": [delayed_dubclick, Key("cmd-c")],
    "(fi duke)": [delayed_dubclick, Key("cmd-v")],
    "drag": mouse_drag,
    "release": mouse_release,
    # jsc added
    "(shift click | shicks)": shift_click,
    "(command click | chom lick)": command_click,
    "(muck )": mouse_scroll(500),
    "(make )": mouse_scroll(-500),
}

ctx.keymap(keymap)
