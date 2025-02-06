from setuptools import setup, find_packages

setup(
    name="arduino-snt",
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        "pyfirmata"
    ],
)