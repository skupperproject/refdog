from plano import *
from plano.github import *
from transom.planocommands import *

import collections
import commands
import resources

@command
def generate():
    resources.generate()
    commands.generate()
