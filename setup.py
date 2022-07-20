'''
Function:
    setup the sciogovterminal
Author:
    Charles
微信公众号:
    Charles的皮卡丘
GitHub:
    https://github.com/CharlesPikachu
'''
import sciogovterminal
from setuptools import setup, find_packages


'''readme'''
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


'''setup'''
setup(
    name=sciogovterminal.__title__,
    version=sciogovterminal.__version__,
    description=sciogovterminal.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    author=sciogovterminal.__author__,
    url=sciogovterminal.__url__,
    author_email=sciogovterminal.__email__,
    license=sciogovterminal.__license__,
    include_package_data=True,
    entry_points={'console_scripts': ['sciogov = sciogovterminal.sciogovterminal:main']},
    install_requires=[lab.strip('\n') for lab in list(open('requirements.txt', 'r').readlines())],
    zip_safe=True,
    packages=find_packages()
)