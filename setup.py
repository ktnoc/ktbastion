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
        'pycryptodome>10.1.2',
        'base58'
    ],
    dependency_links=[
        'git+https://github.com/Legrandin/pycryptodome.git@0caeb760e2a56cd8c714b6771c7e09e583482985#egg=pycryptodome-10.1.2.1'
    ]
)
