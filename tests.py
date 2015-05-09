# -*- coding: utf-8 -*- 
from __future__ import absolute_import
from __future__ import unicode_literals

import unittest

from django_cache_decorator import utils

class UtilsTestCase(unittest.TestCase):
 
    def setUp(self):
        pass
        

    def test_get_cache_key(self):
        args = [
            'Čakovec, Croatia',
        ],
        kwargs = {
            'test': 'test',
            'test2': 'Čakovec, Croatia',
        }
        
        key = utils.cache_get_key('testFunctionName', *args, **kwargs)

