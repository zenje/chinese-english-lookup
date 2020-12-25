import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chinese-english-lookup-zenje",
    version="0.0.1",
    author="zenje",
    author_email="jessicaczeng@gmail.com",
    description="look up Chinese words, return English definitions; parses CC-CEDICT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zenje/chinese-english-lookup",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "chinese-english-lookup = chinese-english-lookup.__main__:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
