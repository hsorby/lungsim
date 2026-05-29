
import os

import intel_fortran_rt
print(os.path.dirname(intel_fortran_rt.__file__))
import intel_openmp
print(os.path.dirname(intel_openmp.__file__))
import intel_cmplr_lib_rt
print(os.path.dirname(intel_cmplr_lib_rt.__file__))


print("DLL search dirs:")
for p in os.environ.get("PATH", "").split(";"):
    print("  ", p)
