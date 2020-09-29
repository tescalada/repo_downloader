# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='downloader',
    version="1.0",
    packages=find_packages(),
    include_package_data=False,
    install_requires=[],
    entry_points={
        'console_scripts': ['download-starred=downloader.main:download_starred'],
    }
)
