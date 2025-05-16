from setuptools import setup, find_packages

setup(
    name="tradingsuite",
    version="0.1",
    packages=find_packages(where="src/main/python") + find_packages(where="src/test/python"),
    package_dir={
        "": "src/main/python",
        "tests": "src/test/python"
    },
    install_requires=["DateTime"],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
        ],
    },
) 