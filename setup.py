import setuptools

setuptools.setup(
    name="exampy",
    version="0.2",
    author="Jo Bovy",
    author_email="bovy@astro.utoronto.ca",
    description="A small example Python package",
    packages=["exampy","exampy/integrate"],
    install_requires=["numpy"]
)
