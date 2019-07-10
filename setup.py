
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='cintay',  
     version='0.1',
     author="Emre Cintay",
     author_email="emre@cintay.com",
     description="Print CINTAY",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Chinacolt/cintay-pip",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
