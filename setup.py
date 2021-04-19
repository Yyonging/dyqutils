import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dyqutils",
    version="0.0.1",
    packages=['dyqutils'],
    author="duanyongqiang",
    author_email="sysuduanyongqiang@163.com",
    description="my super tools for coding life",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yyonging/dyqutils",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pyecharts>=1.9.0",
        "rich>=10.1.0"
    ],
    python_requires='>=3.7',
)
