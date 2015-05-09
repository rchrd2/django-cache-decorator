Easily add caching to functions within a django project.


## Installation from PyPi

```
pip install django-cache-decorator
```


## Installation from Github

```
pip install -e git+https://github.com/rchrd2/django-cache-decorator.git#egg=django-cache-decorator
```
 

## Example usage

```
@django_cache_decorator(time=0)
def geocodeGooglePlaceTextJson(location):
    ...
```


## Running tests

```
python -m unittest tests
```


## Credits

Built off of example code from:
http://james.lin.net.nz/2011/09/08/python-decorator-caching-your-functions/

Further development and packaging by Richard Caceres (@rchrd2)


## Release log

- 0.4 - Update project for PyPi (pip install django-cache-decorator)!
- 0.3 - another bug fix for unicode params
- 0.2 - bug fix for unicode params
- 0.1 - initial release