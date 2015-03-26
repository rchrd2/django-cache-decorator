from setuptools import setup

setup(
    name = 'django-cache-decorator',
    packages = ['django_cache_decorator'],
    license = 'MIT',
    version = '0.3',
    description = 'Easily add caching to functions within a django project.',
    long_description=open('README.md').read(),
    author = 'Richard Caceres',
    author_email = 'me@rchrd.net',
    url = 'https://github.com/rchrd2/django-cache-decorator/',
    keywords = ['django','caching'],
    classifiers = [],
)
