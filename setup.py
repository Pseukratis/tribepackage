from setuptools import setup, find_packages

setup(
    name='tribepackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA hackathon python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Pseukratis/tribepackage.git',
    author='Tribute Motlhabane',
    author_email='tribute9211@gmail.com'
)
