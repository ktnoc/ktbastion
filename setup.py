import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ktbastion",
    version="0.0.1",
    author="ktnoc",
    author_email="ktnoc@users.noreply.github.com",
    description="KTBastion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ktnoc/ktbastion",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pycryptodome',
        'base58'
    ]
)
