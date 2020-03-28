"""
Docker commands
"""

from talon.voice import Context, Key
from ..utils import word

ctx = Context("docker")

DOCKER_PREFIX = "drum"

ctx.keymap(
    {
        DOCKER_PREFIX + "piss": "docker ps",
        DOCKER_PREFIX + "(queue | kill)": "docker kill ",
        DOCKER_PREFIX + "start": "docker start ",
        DOCKER_PREFIX + "exec": ["docker exec -it  /bin/sh"] + [Key('left')] * 8,
        "docker compose [<dgndictation>]": ["docker-compose ", text],
        "docker [<dgndictation>]": ["docker ", text],
    }
)

