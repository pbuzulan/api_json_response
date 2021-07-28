import os
import re, io
from setuptools import setup, find_packages

path = os.path.abspath(os.path.dirname(__file__))

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    io.open('standresponse/__version__.py'
            '', encoding='utf_8_sig').read()
).group(1)


def read_file(filename):
    with open(os.path.join(path, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


setup(
    name="standresponse",
    version=__version__,
    project_urls={
        "Documentation": "/",
        "Code": "/",
        "Issue tracker": "/",
    },
    keywords=["response", "error", "handler", "standardization"],
    description="Response Standardization Library",
    long_description=read_file("README.md"),
    long_description_content_type='text/markdown',
    python_requires=">=3.6.0",
    license="MIT",
    author="Petru Buzulan",
    author_email="buzulan.petru@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    scripts=[],
    zip_safe=False

)
