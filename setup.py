import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name = "Bytes_Converter",
    version = "1.0.0",
    author = "Himangshu De",
    author_email = "dehimangshu2020@gmail.com",
    description = "This library contains digital storage unit converter",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Stark-Corp/Bytes_Converter",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        
    ],
    python_requires = ">= 3.6",
)