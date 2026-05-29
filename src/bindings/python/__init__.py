import os
import platform
import site
import sys


if platform.system() == "Windows":
    module_dir = os.path.dirname(__file__)
    os.add_dll_directory(module_dir)
    print(sys.prefix)
    os.add_dll_directory("C:/hostedtoolcache/windows/Python/3.10.11/x64/Library/bin/")
