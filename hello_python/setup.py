from setuptools import setup, find_packages

setup(
    name='hello_python',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello-python=hello:hello',
        ],
    },
)
