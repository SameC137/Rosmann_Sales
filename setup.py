#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['pandas>=1.1.0', 'numpy>=1.19.0', 'sklearn', 'seaborn', 'matplotlib', 'scipy', 'dvc', 'mlflow','tesnsorflow','kearas']

test_requirements = ['pytest>=3', ]

setup(
    author="Same Michael",
    email="samemichael1415@gmail.com",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Sales Predictions using regression models and deep learning",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='scripts, predictions, predictive models, deep learning predictions',
    name='ab_test_machine_same',
    packages=find_packages(include=['scripts', 'scripts.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/SameC137/Rosmann_Sales',
    version='0.1.0',
    zip_safe=False,
)