import re
from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    # noinspection PyRedeclaration
    requirements = f.read().splitlines()

version = ''
with open('osu/__init__.py') as f:
    # noinspection PyRedeclaration
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

readme = ''
with open('README.md') as f:
    # noinspection PyRedeclaration
    readme = f.read()


setup(
    name='osu.py', author='zeroday0619',
    project_urls={
        "Issue tracker": "https://github.com/zeroday0619/osu.py/issues",
    },
    version=version,
    packages=["osu"],
    license='MIT',
    long_description=readme,
    long_description_content_type="text/markdown",
    description="osu-api v2 python wrapper",
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.7.0',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
