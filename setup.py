from distutils.core import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf8')

setup(
  name = 'termii',         
  packages = ['termii'],  
  long_description= long_description,
  long_description_content_type = 'text/markdown',
  version = '0.1.1',      
  license='MIT',       
  description = 'Termii SDK for Python to allow easy interfacing with the termii API.',   
  author = 'Alaribe Eric & Hebron Praise',                   
  author_email = 'panampraisehebron@gmail.com',      
  url = 'https://github.com/panam-py/termii-python',   
  download_url = 'https://github.com/panam-py/termii-python/archive/refs/tags/v_0.1.0.tar.gz',    
  keywords = ['Termii SDK', 'Python', 'API'],   
  install_requires=[            
    ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)