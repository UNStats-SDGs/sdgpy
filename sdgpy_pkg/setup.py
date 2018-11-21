import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sdgpy_pkg",
    version="0.0.1",
    author="Travis Butcher (esri)",
    author_email="tbutcher@esri.com",
    description="Python Package for working with ArcGIS Online and SDG data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/unsd/sdgpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)