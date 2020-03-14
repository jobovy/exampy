import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="exampy",
    version="0.2",
    author="Jo Bovy",
    author_email="bovy@astro.utoronto.ca",
    description="A small example Python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["exampy","exampy/integrate"],
    install_requires=["numpy"]
)
