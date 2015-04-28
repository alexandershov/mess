from setuptools import find_packages, setup


setup(
    name='mess',
    author='Alexander Ershov',
    author_email='codumentary.com@gmail.com',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['six'],
    url='https://github.com/alexandershov/mess',
    keywords=['utilities', 'iterators'],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
    ],
)

