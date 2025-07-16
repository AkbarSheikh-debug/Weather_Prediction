from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Weather_Prediction",
    version="0.1",
    author="Akbar",
    packages=find_packages(),
    install_requires = requirements,
)