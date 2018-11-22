from setuptools import setup

setup(
    name='g3kko',
    packages=['g3kko'],
    include_package_data=True,
    install_requires=[
        'flask', 'flask_sqlalchemy',
    ],
)
