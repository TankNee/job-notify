from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

with open('LICENSE', 'r') as f:
    license = f.read()

setup(
    name='jobpusher',
    version='0.0.2',
    description='Job Pusher',
    author='TankNee',
    author_email='nee@tanknee.cn',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=license,
    packages=find_packages(include=['jobpusher', 'jobpusher.*']),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ],
    keywords='jobpusher notifier pusher',
    include_package_data=True,
)
