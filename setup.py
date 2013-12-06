from setuptools import setup, find_packages
import os

setup(
    name = "cmsplugin-resume",
    packages = find_packages(),
    version = "0.1",
    description = "A resume plugin for django-cms",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author = "Antoine Nguyen",
    author_email = "tonio@ngyn.org",
    url = "http://github.com/tonioo/cmsplugin-resume",
    license = "BSD",
    keywords = ["django", "django-cms", "resume"],
    classifiers = [
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django"
        ],
    include_package_data = True,
    install_requires = ['setuptools', 'django-cms', 'south'],
)
