import os

from setuptools import find_packages, setup


def requirements(fname):
    """Return a list of requirements from a file."""
    return [
        line.strip()
        for line in open(
            os.path.join(os.path.dirname(__file__), fname), encoding="utf-8"
        )
    ]


reqs = requirements("requirements.txt")


setup(
    name="my_package",
    description=(
        "self-assess is a python package for self-revive the output of LLMs "
        "to improve the quality of the generated text."
    ),
    version="0.1",
    author="Thanh Nguyen",
    packages=find_packages(),
    install_requires=reqs,  # set to `reqs` variable or []
)
