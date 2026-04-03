'''
The setup.py is the essential part of packaging and distributing python projects.
It is used by setuptools to define the configuration of the project, like metadata,etc...
'''

from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return a list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the text file
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file is not found")
    
    return requirement_lst


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Guhan",
    author_email="studiesofguhan3821@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
