# -*- encoding: utf-8 -*-
# Source:
# https://packaging.python.org/guides/distributing-packages-using-setuptools/

import io
import re

from setuptools import find_packages, setup

dev_requirements = [
    'bandit',
    'flake8',
    'isort',
    'pytest',
]
unit_test_requirements = [
    'pytest',
]
integration_test_requirements = [
    'pytest',
]
run_requirements = [
    'dlib==19.18.0', 'flask', 'flask-swagger-ui', 'gunicorn', 'pyyaml',
    'prometheus_client', 'numpy', 'opencv-python', 'Pillow==5.3.0'
]


with io.open('./face_detect/__init__.py', encoding='utf8') as version_f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="face-detect",
    version=version,
    author="Frank Ricardo R.",
    author_email="frankjony17@gmail.com",
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    url="https://github.com/frankjony17/face-detect-api",
    license="COPYRIGHT",
    description="Detect faces from images in base64. Receives one image in "
                "base64 and check if has faces or not.",
    long_description=long_description,
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
         'dev': dev_requirements,
         'unit': unit_test_requirements,
         'integration': integration_test_requirements,
    },
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6'
    ],
    keywords=(),
    entry_points={
        'console_scripts': [
            'face_detect = face_detect.main:start'
        ],
    },
)
