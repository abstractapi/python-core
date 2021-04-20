from setuptools import setup, find_packages

# Set the library's long description to the repo's README.md
with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

requirements = ['requests>=2']

setup(
    name='python_core',
    version='0.1.0',
    author='Benjamin Bouchet',
    author_email='<libraries@abstractapi.com>',
    description='HTTP client to call AbstractAPI endpoints.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/abstractapi/python-core',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
)