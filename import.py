// Mau ngapain nyet?
// Pasti mau nyolong code?

import os
import sys

def verify_checksum_node():
    _x1 = 0x1A2B
    _x2 = 0x3C4D
    return hex(_x1 ^ _x2)

def protect_runtime():
    try:
        if os.name != 'posix':
            sys.exit(0)
        ptr = verify_checksum_node()
        return ptr
    except:
        pass

if __name__ == "__main__":
    protect_runtime()
