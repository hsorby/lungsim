import os

try:
    from aether import diagnostics
except ImportError as e:
    print("Import failed:", e)

    import ctypes
    try:
        ctypes.CDLL("aether_c.dll")
    except OSError as e:
        print("Manual load failed:", e)
