import io
import os
import re
import sys
from pathlib import Path

from setuptools import find_packages, setup

install_requires = ["wagtail>=2.13"]

tests_require = ["pytest-django", "wagtail-factories", "pytest"]

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

version = ""
with io.open("wagtail_color_panel/__init__.py", "r", encoding="utf8") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

setup(
    version=version,
    name="wagtail-color-panel",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Martin Sandström",
    author_email="martin@marteinn.se",
    url="https://github.com/marteinn/wagtail-color-panel",
    packages=find_packages(
        exclude=("*.tests", "*.tests.*", "tests.*", "tests", "example*")
    ),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
    tests_require=tests_require,
    extras_require={"test": tests_require},
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
    ],
    setup_requires=["setuptools_scm", "pytest-runner"],
    python_requires=">=3.7",
)
