import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TerminalEmailSender",
    version="1.0.1",
    author="marcoromanelli-github",
    author_email="marcoromane@gmail.com",
    description="Simple package which implements the functionality of a mail service provider usable as a python package and from CMI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcoromanelli-github/TerminalEmailSender",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
