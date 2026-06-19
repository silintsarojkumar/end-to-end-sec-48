from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT = '-e .'

def get_req(file_path:str)->List[str]:
    '''
    this function will return list of req
    
    
    '''
    reqs=[]
    with open(file_path) as file_obj:
        reqs = file_obj.readline()
        reqs = [req.replace("\n","") for req in reqs]

        if HYPEN_E_DOT in reqs:
            reqs.remove(HYPEN_E_DOT)


    return reqs





setup(
    name='mlproject',
    version='0.0.1',
    author='Saroj',
    author_email='ersarojiitm@gmaail.com',
    packages=find_packages(),
    install_requires=get_req('req.txt')
)