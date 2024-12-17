from setuptools import setup, find_packages

setup(
    name="JsonData",                 # Package name
    version="0.1.0",                   # Version
    packages=find_packages(),          # Automatically find packages
    install_requires=[
        'json'
    ],               # Dependencies (if any)
    author="Gemcast",
    description="Make Data using JSON",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",  # Your repository link
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',           # Minimum Python version
)
