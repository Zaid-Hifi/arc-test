import setuptools
from setuptools import find_packages

setuptools.setup(
    package_dir={"": "src"},
    packages=find_packages(where='src'), 
    include_package_data=True,

    # add the following line if  you have data files that are necessary for your package to run,
    # place the folders in the package directory and list them here as follows.
    # ensure there is an empty __init__.py file inside the data package, as shown in the template. 
    package_data={"testpkg.data": ["*"]},
    python_requires=">=3.8",
)