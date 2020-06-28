import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="ccpp",
    version="1.0",
    author="Davi Sousa",
    packages=["ccpp"],
    author_email="davi.gomes.sousa@ccc.ufcg.edu.br",
    description=(
        "A simple g++ interface, to run easily C/C++ code on Linux and Windows."),
    license="MIT",
    keywords="c++ cpp c h g++ interface",
    url="https://github.com/davigsousa/ccpp",
    long_description=read('README.md'),
    entry_points={
        "console_scripts": ["ccpp=ccpp.__main__:run"]
    }
)
