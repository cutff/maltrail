#!/usr/bin/env python

"""
Copyright (c) 2014-2015 Miroslav Stampar (@stamparm)
See the file 'LICENSE' for copying permission
"""

import re

from core.common import retrieve_content
from core.enums import TRAIL

__type__ = (TRAIL.URL,)
__url__ = "http://malc0de.com/rss/"
__check__ = "Malc0de Database Feed"
__info__ = "malware"
__reference__ = "malc0de.com"

def fetch():
    retval = dict((_, {}) for _ in __type__)
    content = retrieve_content(__url__)

    if __check__ in content:
        for match in re.finditer(r"<description>URL: ([^,\s]+)", content):
            retval[TRAIL.URL][match.group(1)] = (__info__, __reference__)

    return retval
