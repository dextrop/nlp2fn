import setuptools

__version__ = "0.0.3"
__description__ = 'With the ability to load and read Python functions from any specified location, `nlp2fn` brings all your automation tasks together.'
__author__ = 'Jennie Developers <saurabh@ask-jennie.com>'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='nlp2fn',
     version=__version__,
     author=__author__,
     py_modules=["jennie"],
     install_requires=['requests'],
     entry_points={
        'console_scripts': [
            'nlp2fn=nlp2fn:execute'
        ],
     },
     author_email=__author__,
     description= __description__,
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/dextrop/nlp2fn",
     packages=setuptools.find_packages(),
     classifiers=[
         "License :: OSI Approved :: MIT License",
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.7",
     ],
 )