from setuptools import setup, find_packages

setup(
    name='rubiks-cube',
    version='0.0.1',
    packages=find_packages(),
    install_requires=["selenium==3.141.0",
                      "tkmacosx==1.0.3",
                      "matplotlib==3.2.2"]
)