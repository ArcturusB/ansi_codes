import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='ansi_codes',
    py_modules=['ansi_codes'],
    version='2017.3.21',
    author='Gabriel Pelouze',
    author_email='gabriel@pelouze.net',
    description='Format Python terminal output using ANSI escape codes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gpelouze/ansi_codes',
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX',
    ],
)
