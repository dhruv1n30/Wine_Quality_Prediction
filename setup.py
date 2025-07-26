# from setuptools import setup, find_packages
import setuptools


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = '0.0.0'

AUTHOR_NAME = 'Dhruvin Vachhani'
SRC_REPO = "mlProject"
AUTHOR_EMAIL = 'dhruvinvachhani25@gmail.com'
AUTHOR_USER_NAME = 'dhruv1n30'
REPO_NAME = 'Wine_Quality_Prediction'


setuptools.setup(
    name=SRC_REPO,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    version=__version__,
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)

