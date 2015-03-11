#!/usr/bin/env python

"""
Copyright (c) 2014-2015 Miroslav Stampar (@stamparm)
See the file 'LICENSE' for copying permission
"""

import re

from core.common import retrieve_content
from core.enums import TRAIL

__type__ = (TRAIL.IP,)
__url__ = "https://myip.ms/files/blacklist/htaccess/latest_blacklist.txt"
__check__ = "ADDRESSES DATABASE"
__info__ = "spam bot or crawler"
__reference__ = "myip.ms"

def fetch():
    retval = dict((_, {}) for _ in __type__)
    content = retrieve_content(__url__)

    if __check__ in content:
        for match in re.finditer(r"deny from (\d+\.\d+\.\d+\.\d+)", content):
            retval[TRAIL.IP][match.group(1)] = (__info__, __reference__)

    return retval
