This can be used to cache the results of functions.

Example:
  @django_cache_decorator(time=0)
  def geocodeGooglePlaceTextJson(location):
      ...

Built off of code form:
http://james.lin.net.nz/2011/09/08/python-decorator-caching-your-functions/

