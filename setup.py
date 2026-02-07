"""Setup configuration for CommandPro"""

from setuptools import setup, find_packages

setup(
    name="cmdpro",
    version="0.1.0",
    description="Command line error helper - analyzes errors and provides solutions",
    author="Developer",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "cmdpro=cli:main",
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)
