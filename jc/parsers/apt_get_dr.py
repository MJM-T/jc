"""jc - JSON Convert `apt-get --dry-run` command output parser

Usage (cli):

    $ ...

or

    $ jc ...

Usage (module):

    import jc
    ...

Schema:


"""

from typing import List, Dict
from jc.jc_types import JSONDictType
import jc.utils

class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '0.1'
    description = '`apt-get --dry-run` command parser'
    author = 'Matthias Mitchell'
    author_email = 'i.am.matthias@outlook.com'
    compatible = ['linux']
    magic_commands = ['apt-get --dry-run']
    tags = ['command']


__version__ = info.version

def _process(proc_data):
    #TODO
    return proc_data

def parse(data, raw=False, quiet=False):
    #TODO
    return None