from os import path
from setuptools import setup, find_packages


install_requires = ["wagtail"]

tests_require = ["pytest-django", "wagtail-factories", "pytest"]

with open(
    path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf-8"
) as f:
    long_description = f.read()

setup(
    version="1.0.0",
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
        "Development Status :: 4 - Beta",
        "Environment :: Web Environmen",
        "Framework :: Django",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
    setup_requires=["setuptools_scm", "pytest-runner"],
    python_requires=">=3.6",
)
