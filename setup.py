from setuptools import setup

setup(
    name='coinify',
    version='3',
    description='The funniest joke in the world',
    url='https://github.com/CoinifySoftware/python-sdk',
    author='CoinifySoftware',
    author_email='support@coinify.com',
    license='MIT',
    packages=['coinify'],
    install_requires=[
        'requests',
    ],
    zip_safe=False,
)