from os import path
import sys

def _is_bundled():
    return hasattr(sys, '_MEIPASS')
def asset_path(file_name):
    if _is_bundled():
        root = sys._MEIPASS
    else:
        root = '.'
    return path.abspath(path.join(root, 'assets', file_name))

def sibling_path(file_name):
    if _is_bundled():
        root = path.dirname(sys.executable)
    else:
        root = '.'
    return path.abspath(path.join(root, file_name))
