from setuptools import setup, find_packages

setup(
    name='filex',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'filex = filex.__main__:main'
        ]
    },
    install_requires=[
        # List your package dependencies here
    ],
)
