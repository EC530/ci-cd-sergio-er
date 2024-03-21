from setuptools import setup, find_packages

setup(
    name='MatrixMultPackage',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    scripts=['MatrixMult.py', 'pytest.py'],
)