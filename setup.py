# @Time : 2019/11/7 00:29 
# @Author : Lu Ning 
# @File : setup.py.py
# @Email: jiangxiluning@gmail.com
# @Description: say something informative
import os
import io
import re
from setuptools import setup, find_packages


def parse_req(req_file):
    with open(req_file) as f:
        req_file = [line.strip() for line in f.readlines()]
    return req_file


def read(*args, **kwargs):
    with open(os.path.join(os.path.dirname(__file__), *args),
              encoding=kwargs.get('encoding', 'utf8')) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


readme = read('README.md')

VERSION = find_version('ocr_e2e_infer', '__init__.py')

req = parse_req('./requirements.txt')

setup(
    name='ocr_e2e_infer',
    version=VERSION,
    author='Lu Ning',
    author_email='jiangxiluning@gmail.com',
    desciption='A OCR End to End Inference Framework.',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=('tests', 'tests.*',)),
    zip_safe=True,
    install_requires=req,
    python_requires='>=3.5'
)