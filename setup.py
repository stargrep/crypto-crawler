from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='crypto_crawler',
    version='0.03',
    description='Crypto Crawler for fun',
    long_description=readme,
    author='mike',
    author_email='..',
    url='https://github.com/',
    packages=find_packages(exclude=('tests', 'docs')),
    data_files=[
        ('doc', ['design.md', 'requirements.txt', 'LICENSE'])
    ],
)