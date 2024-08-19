from setuptools import setup, find_packages

setup(
    name="wrappit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer[all]",
        "gitignore-parser",  # Add the gitignore-parser library here
    ],
    entry_points={
        "console_scripts": [
            "wrappit=wrappit.cli:app",
        ],
    },
)
