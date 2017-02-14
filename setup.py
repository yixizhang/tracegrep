from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tracegrep',
    version='0.1.1',
    description='Grep to parse Python traceback from plain text',
    long_description=readme,
    author='Yixi Zhang',
    author_email='yixi.zhang.max@gmail.com',
    url='https://github.com/yixizhang/tracegrep',
    license=license,
    packages=find_packages(exclude=('tests',))
)
