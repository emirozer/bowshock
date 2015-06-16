from setuptools import setup, find_packages
import os

setup(
    name='bowshock',
    version='0.0.2',
    author='Emir Ozer',
    author_email='emirozer@yandex.com',
    url='https://github.com/emirozer/bowshock',
    description='An all-in-one library for NASA API\'s',
    long_description=os.path.join(os.path.dirname(__file__), 'README.md'),
    packages=find_packages(exclude=[]),
    install_requires=[
        'requests>=2.6.1',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords='nasa api wrapper',
    )
