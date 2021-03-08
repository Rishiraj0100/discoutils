from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="disoutils",
    version="0.0.1",
    description="Some utilities for discord.py. Making Discord bot development easier.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Rishiraj0100/discoutils",
    author="Rishi Raj",
    author_email="rishi0100raj@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
    install_requires=["discord.py >=1,<2"],
    keywords="discord discord-py discord-bot utils utility",
    packages=find_packages(exclude=["docs", "tests"]),
    data_files=None,
)
