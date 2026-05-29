
import os

try:
  import intel_fortran_rt
  print(os.path.dirname(intel_fortran_rt.__file__))
except ModuleNotFoundError as e:
  print("intel_fortran_rt not found:", e)

try:
  import intel_openmp
  print(os.path.dirname(intel_openmp.__file__))
except ModuleNotFoundError as e:
  print("intel_openmp not found:", e)

try:
  import intel_cmplr_lib_rt
  print(os.path.dirname(intel_cmplr_lib_rt.__file__))
except ModuleNotFoundError as e:
  print("intel_cmplr_lib_rt not found:", e)


print("DLL search dirs:")
for p in os.environ.get("PATH", "").split(";"):
    print("  ", p)
