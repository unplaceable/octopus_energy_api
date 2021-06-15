from setuptools import setup, Extension
import os

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'octopus_energy_api',         # How you named your package folder (MyLib)
  packages = ['octopus_energy_api'],   # Chose the same as "name"
  version = '0.5.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Wrapper for communicating with the Octopus Energy API',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Euan Campbell',                   # Type in your name
  author_email = 'dev@euan.app',
  url = 'https://github.com/euanacampbell/octopus_energy_api',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/euanacampbell/octopus_energy_api/archive/refs/heads/master.tar.gz',    # I explain this later on
  keywords = ['energy', 'api', 'requests'],   # Keywords that define your package best
  install_requires=[  
          'requests'          # I get to this in a second
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)