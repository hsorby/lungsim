import os
import platform
import site

if platform.system() == "Windows":
    # Look through all site-packages dirs
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
            candidate = os.path.join(base, pkg, "bin")
            if os.path.isdir(candidate):
                os.add_dll_directory(candidate)
