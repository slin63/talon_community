"""
Docker commands
"""

from talon.voice import Context, Key
from ..utils import word, text, text_padded

ctx = Context("docker")

DOCKER_PREFIX = "dill "

ctx.keymap(
    {
        DOCKER_PREFIX + "(queue | kill)": "docker kill ",
        DOCKER_PREFIX + "start": "docker start ",
        DOCKER_PREFIX + "exec": ["docker exec -it  /bin/sh"] + [Key("left")] * 8,
        DOCKER_PREFIX + " compose [<dgndictation>]": ["docker-compose", text_padded],
        DOCKER_PREFIX + " [<dgndictation>]": ["docker", text_padded],
    }
)
