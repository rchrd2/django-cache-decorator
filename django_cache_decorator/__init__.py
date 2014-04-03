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


def django_cache_decorator(time=300, cache_type=None):
    if cache_type is None:
        cache_type = 'memcache' 
    
    cache = get_cache(cache_type)
    
    def decorator(fn):
        def wrapper(*args, **kwargs):
            key = cache_get_key(fn.__name__, *args, **kwargs)
            result = cache.get(key)
            if not result:
                result = fn(*args, **kwargs)
                cache.set(key, result, time)
            return result
        return wrapper
    return decorator

