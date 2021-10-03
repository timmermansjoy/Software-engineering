#!/usr/bin/env python3
# https://godatadriven.com/blog/a-practical-guide-to-using-setup
import os
import setuptools

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(name='CSV_Parser',
                 version='0.0.1',
                 description='A csv parsing tool.',
                 author='Joy Timmermans, Nikki Bruls, Stijn Jacobs, Karel Sajdak, Wiktor Kosinski',
                 license='MIT',
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 package_dir={"": "src"},
                 packages=setuptools.find_packages(where="src"),
                 platforms=['any'],
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ],
                 install_requires=["pandas", "flask"],
                 python_requires='>=3.6',
                 extras_require={
                     'development': ["pytest", "pytest-xdist", "pytest-cov", "autopep8"],
                     'azure': ["pytest", "pytest-xdist", "pylint", "pytest-cov", "pytest-azurepipelines"]
                 },
                 include_package_data=True)
