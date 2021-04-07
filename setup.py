from setuptools import setup, find_packages


setup(
    name='devopswiki',
    version='1.0.1',
    install_requires=[
        'flask',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            ''
        ]
    }
)
