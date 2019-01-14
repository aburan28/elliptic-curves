from setuptools import setup, find_packages

setup(
    name = "eccarith",
    version = "0.0.1",
    description = "Comprehensive Elliptic Curve Arithmetic library",
    url="https://github.com/aburan28/elliptic-curves",
    author = "Adam Buran",
    author_email = "contact@aburan.io",
    maintainer = "Adam Buran",
    maintainer_email = "adam.buran@aburan.io",
    license = "GPL v2",
    zip_safe = False,
    packages = find_packages(),
    install_requires = [
        'setuptools',
        'pysnmp'
    ],
)
