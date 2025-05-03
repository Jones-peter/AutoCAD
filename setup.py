# setup.py
from setuptools import setup, find_packages

setup(
    name="AutoCAD",  # Name of your package
    version="0.1.3",
    packages=find_packages(),  # Automatically finds the 'cadvance' package
    install_requires=[
        'pywin32',
        'psutil',
    ],
    entry_points={
        'console_scripts': [
            'AutoCAD = AutoCAD.__main__:main',  # Registers 'cadvance' as a command-line tool
        ],
    },
    keywords=["autocad", "automation", "activex", "comtypes", "AutoCAD", "AutoCADlib"],
    author="Jones Peter",
    author_email="jonespetersoftware@gmail.com",
    url="https://github.com/Jones-peter",
    description="A professional AutoCAD automation package with many functions.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: Microsoft :: Windows",
    ],
    include_package_data=True,  # Include non-Python files, like the README
)
