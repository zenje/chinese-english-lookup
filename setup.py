import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chinese-english-lookup",
    version="0.0.2",
    author="zenje",
    author_email="jessicaczeng@gmail.com",
    description="Allows look-up of Chinese words, returning English definitions; parses CC-CEDICT; provides HSK3.0 and HSK2.0 utilities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zenje/chinese-english-lookup",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "chinese-english-lookup=chinese_english_lookup.__main__:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
