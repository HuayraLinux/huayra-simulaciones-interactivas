# -*- encoding: utf-8 -*-

import os

"""
Config class
"""
class Config:
	DEV = os.path.realpath(__file__) != '/usr/bin/huayra-simulaciones-interactivas'
