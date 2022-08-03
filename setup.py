from setuptools import find_packages
from distutils.core import setup

setup(
    name="pytorch_pwc",
    version="0.0.1",
    author="Jonas Frey",
    author_email="jonfrey@ethz.ch",
    packages=find_packages(),
    python_requires=">=3.6",
    description="Package of pwc_net",
    install_requires=[""],
)