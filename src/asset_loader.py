from os import path
import sys

def asset_path(file_name):
    if hasattr(sys, '_MEIPASS'):
        root = sys._MEIPASS
    else:
        root = '.'
    return path.abspath(path.join(root, 'assets', file_name))