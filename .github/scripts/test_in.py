import os

try:
    from aether import diagnostics
except ImportError as e:
    print("Import failed:", e)

    import ctypes
    try:
        ctypes.CDLL("C:/hostedtoolcache/windows/Python/3.10.11/x64/lib/site-packages/aether/aether_c.dll")
    except OSError as e:
        print("Manual load failed:", e)
