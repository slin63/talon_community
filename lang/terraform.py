"""
Docker commands
"""

from talon.voice import Context, Key
from ..utils import word, text

ctx = Context("terraform")

TERRAFORM_PREFIX = "terra"

ctx.keymap(
    {
        TERRAFORM_PREFIX + "form [<dgndictation>]": ["terraform ", text],
        TERRAFORM_PREFIX + "form init": "terraform init",
    }
)
