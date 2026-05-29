import os
import platform
import site
import sys


if platform.system() == "Windows":
    module_dir = os.path.dirname(__file__)
    os.add_dll_directory(module_dir)
    print(sys.prefix)
    intel_library_path = os.path.join(sys.prefix, "Library", "bin")
    print("Adding Intel library path:", intel_library_path)
    os.add_dll_directory("C:/hostedtoolcache/windows/Python/3.10.11/x64/Library/bin/")
