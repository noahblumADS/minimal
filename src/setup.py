# Determine the base
import os
import sys
from cx_Freeze import Executable, setup, __version__

base = 'Win32GUI' if sys.platform == 'win32' else None

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [Executable(script='main.py',
                          base=base,
                          target_name="TestApp.exe")]

options = {'build_exe': {'build_exe': f"../Executable ({__version__})",
                         'include_files': ["../src",
                                           "config_default.yaml",
                                           "__init__.py"]}}

setup(options=options,
      name="TestApp",
      version=1.0,
      description="TestApp",
      packages=['modules'],
      executables=executables)
