from setuptools import setup, find_packages

setup(
    name='pB11FusionSim',
    version='0.1.0',
    description='A simple Python package for modeling p-B11 aneutronic fusion physics',
    author='DuRay Montague',
    author_email='duray@type2realist.com',
    url='https://github.com/duraymontague/pB11FusionSim',
    packages=find_packages(),
    install_requires=[
        'numpy',  # Add any actual dependencies here
    ],
    python_requires='>=3.6',
)
