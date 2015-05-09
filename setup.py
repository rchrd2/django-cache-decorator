from setuptools import setup

version = '0.4'

setup(
    name = 'django-cache-decorator',
    packages = ['django_cache_decorator'],
    license = 'MIT',
    version = version,
    description = 'Easily add caching to functions within a django project.',
    long_description=open('README.md').read(),
    author = 'Richard Caceres',
    author_email = 'me@rchrd.net',
    url = 'https://github.com/rchrd2/django-cache-decorator/',
    download_url = 'https://github.com/rchrd2/django-cache-decorator/tarball/' + version,
    keywords = ['django','caching','decorator'],
    classifiers = [],
)
