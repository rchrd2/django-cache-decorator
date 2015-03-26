# -*- coding: utf-8 -*- 
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# This can be used to cache the results of functions.
# 
# Example:
#   @django_cache_decorator(time=0)
#   def geocodeGooglePlaceTextJson(location):
#       ...
# 
# Built off of code form:
# http://james.lin.net.nz/2011/09/08/python-decorator-caching-your-functions/



# load logging
#import logging
#logger = logging.getLogger(__name__)

from django_cache_decorator.utils import cache_get_key



# New cache instance reconnect-apparently
cache_factory = {}

def get_cache_factory(cache_type):
    """
    Helper to only return a single instance of a cache
    """
    from django.core.cache import get_cache
    
    if cache_type is None:
        cache_type = 'default'
    
    if not cache_type in cache_factory:
        cache_factory[cache_type] = get_cache(cache_type)

    return cache_factory[cache_type]


def django_cache_decorator(time=300, cache_key='', cache_type=None):
    """
    Easily add caching to a function in django
    """
    
    if cache_type is None:
        cache_type = 'memcache' 
    
    cache = get_cache_factory(cache_type)
    if not cache_key:
        cache_key = None

    def decorator(fn):
        def wrapper(*args, **kwargs):
            #logger.debug([args, kwargs])
            
            # Inner scope variables are read-only so we set a new var
            _cache_key = cache_key
                    
            if not _cache_key:
                _cache_key = cache_get_key(fn.__name__, *args, **kwargs)

            #logger.debug(['_cach_key.......',_cache_key])

            result = cache.get(_cache_key)

            if not result:
                result = fn(*args, **kwargs)
                cache.set(_cache_key, result, time)
            
            return result
        return wrapper
    
    return decorator

