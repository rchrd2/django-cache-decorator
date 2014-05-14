# This can be used to cache the results of functions.
# 
# Example:
#   @django_cache_decorator(time=0)
#   def geocodeGooglePlaceTextJson(location):
#       ...
# 
# Built off of code form:
# http://james.lin.net.nz/2011/09/08/python-decorator-caching-your-functions/


from django.core.cache import get_cache
import hashlib

def cache_get_key(*args, **kwargs):
    serialise = []
    for arg in args:
        serialise.append(str(arg))
    for key,arg in kwargs.items():
        serialise.append(str(key))
        serialise.append(str(arg))
    key = hashlib.md5("".join(serialise)).hexdigest()
    return key

# New cache instance reconnect-apparently
cache_factory = {}

def get_cache_factory(cache_type):
    """
    Helper to only return a single instance of a cache
    """
    if cache_type is None:
        cache_type = 'default'
    
    if not cache_type in cache_factory:
        cache_factory[cache_type] = get_cache(cache_type)

    return cache_factory[cache_type]


def django_cache_decorator(time=300, key=None, cache_type=None):
    """
    Easily add caching to a function in django
    """
    if cache_type is None:
        cache_type = 'memcache' 
    
    cache = get_cache_factory(cache_type)

    def decorator(fn):
        def wrapper(*args, **kwargs):
            if key is None:
                key = cache_get_key(fn.__name__, *args, **kwargs)
            result = cache.get(key)
            if not result:
                result = fn(*args, **kwargs)
                cache.set(key, result, time)
            return result
        return wrapper
    return decorator

