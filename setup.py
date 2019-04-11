import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Sphynx-HPC-SP-MJL",
    version="0.0.1",
    author="Lauren, Matthieu, Justine",
    author_email="lauren.picard@insa-lyon.fr",
    description="Project of sphynx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lauw04/Sphynx-HPC-SP-MJL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
