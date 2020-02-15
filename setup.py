from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='worldgen',
     version='0.1',
     author="Anthony Kallhoff",
     author_email="kallhoffa@gmail.com",
     description="A generator that helps DM's take their worlds to the next level",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/javatechy/dokr",
     package_dir={"": "src"},
     packages=find_packages(
        where="src",
        exclude=["docs"],
     ),
     entry_points={
            "console_scripts": [
                "worldgen=worldgen.cli.main:main"
            ]
     },
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )