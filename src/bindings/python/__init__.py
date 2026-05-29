import os
import platform
import site

if platform.system() == "Windows":
    module_dir = os.path.dirname(__file__)
    os.add_dll_directory(module_dir)
    os.add_dll_directory("C:/hostedtoolcache/windows/Python/3.10.11/x64/Library/bin/")

    for base in site.getsitepackages() + [site.getusersitepackages()]:
        if not base:
            continue

        for pkg in (
            "intel_fortran_rt",
            "intel_openmp",
            "intel_cmplr_lib_rt",
            "intel_cmplr_lic_rt",
            "impi_rt",
        ):
            path = os.path.join(base, pkg, "bin")
            if os.path.isdir(path):
                os.add_dll_directory(path)
