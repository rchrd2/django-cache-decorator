This can be used to cache the results of functions.

Installation:

```
pip install -e git+https://github.com/rchrd2/django-cache-decorator.git#egg=django-cache-decorator
```
 

Example usage:

```
  @django_cache_decorator(time=0)
  def geocodeGooglePlaceTextJson(location):
      ...
```

Built off of code form:
http://james.lin.net.nz/2011/09/08/python-decorator-caching-your-functions/

