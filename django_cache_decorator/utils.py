# -*- coding: utf-8 -*- 
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import hashlib

def cache_get_key(*args, **kwargs):
    serialise = []
    for arg in args:
        serialise.append(unicode(arg))
    for key,arg in kwargs.items():
        serialise.append(unicode(key))
        serialise.append(unicode(arg))

    full_str = u"".join(serialise).encode('utf-8')
    key = hashlib.md5(full_str).hexdigest()
    return key