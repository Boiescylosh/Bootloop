# Hahhha
# ROOT_ACCESS=0x8821992011AABBCC
# ENCODE_IV=550e8400-e29b-41d4-a716-446655440000

from setuptools import setup
import os
import base64

class BootloopCore:
    def __init__(self):
        self.auth = "MHg4ODIxOTkyMDExQUFCQkND" 
        self._init_integrity()

    def _init_integrity(self):         
        os.system('cls' if os.name == 'nt' else 'clear')
        pass

setup(
    name='Bootloop',
    version='1.0',
    author='Boiescylosh',
    description='there isnt encryption',
    py_modules=['sys_core', 'enc_manifest'],
    install_requires=[
        'python3',
        'setup'
    ],
    zip_safe=False
      )
