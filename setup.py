from setuptools import setup, Extension
import os

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'boggle_solver',         # How you named your package folder (MyLib)
  packages = ['boggle_solver'],   # Chose the same as "name"
  version = '1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A package for auto-generating the possible combinations of a boggle grid.',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Euan Campbell',                   # Type in your name
  author_email = 'dev@euan.app',
  package_data={
      'boggle_solver': ['*.txt', 'README']
   },
  url = 'https://github.com/euanacampbell/boggle_solver',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/euanacampbell/boggle_solver/archive/refs/heads/master.tar.gz',    # I explain this later on
  keywords = ['boggle', 'puzzle', 'recursive'],   # Keywords that define your package best
  install_requires=[  
          'requests'          # I get to this in a second
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)