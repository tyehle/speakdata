import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

about = dict()
with open("src/speakdata/__about__.py", "r") as fp:
    exec(fp.read(), about)

setuptools.setup(
    name="speakdata",
    version=about["__version__"],
    author="Tobin Yehle",
    author_email="tobinyehle@gmail.com",
    description="How to pronounce binary data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tyehle/speakdata",
    license="MIT",
    packages=["speakdata"],
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        "console_scripts": ["speakdata=speakdata.__main__:console_entry"]
    },
    classifiers=[
        "Development Status :: 4 - Beta",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Operating System :: OS Independent",

        "Environment :: Console",

        "Typing :: Typed",
    ],
)
