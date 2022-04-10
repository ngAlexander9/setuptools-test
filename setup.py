from setuptools import setup

setup(
    name='tpackage',
    version='0.0.1',
    description='testing how setuptools works',
    author='Alex',
    packages=['tpackage'],
    # ...
    entry_points={
        'console_scripts': [
            'general=tpackage:hello_world',
        ]
    }
)
