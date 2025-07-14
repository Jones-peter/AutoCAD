from setuptools import setup, find_packages
import sys

requirements = ['psutil']
# Add Windows-specific requirements only when on Windows
if sys.platform == 'win32':
    requirements.append('pywin32')

setup(
    name="AutoCAD",
    version="0.1.8",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'AutoCAD = AutoCAD.__main__:main',
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
    include_package_data=True,
    project_urls={
        "Homepage": "https://github.com/Jones-peter/AutoCAD",
        "Documentation": "https://autocad-automation.readthedocs.io/",
        "Bug Tracker": "https://github.com/Jones-peter/AutoCAD/issues",
    },
)
