from setuptools import find_packages,setup

setup(name="e-commerce bot",
       version="0.0.0",
       author="Mahboob Khan",
       author_email="mehboobmeo@gmail.com",
       packages=find_packages(),
       install_requires=['langchain-astradb','langchain'])