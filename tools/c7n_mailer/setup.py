# Copyright 2016 Capital One Services, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import, division, print_function, unicode_literals

from setuptools import setup, find_packages

setup(
    name="c7n_mailer",
    version='0.1',
    description="Cloud Custodian - Reference Mailer",
    classifiers=[
        "Topic :: System :: Systems Administration",
        "Topic :: System :: Distributed Computing"
    ],
    url="https://github.com/capitalone/cloud-custodian",
    license="Apache-2.0",
    packages=find_packages('c7n_mailer'),
    entry_points={
        'console_scripts': [
            'c7n-mailer = c7n_mailer.cli:main',
            'c7n-mailer-replay = c7n_mailer.replay:main'
        ]
    },
    install_requires=["Jinja2", "boto3", "jsonschema"],
)
