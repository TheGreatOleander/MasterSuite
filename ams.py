#!/usr/bin/env python3
"""
Android Master Suite Unified CLI
Version: 6.1.0-CANONICAL
"""

import sys
from control_system import master_control
from kernel_system import kernel_forge
from recovery_system import recoverymanager
from safety_system import flashguard
from device_system import deviceprobe

def main():
    if len(sys.argv) < 2:
        print("Usage: ams <module> [args]")
        print("Modules: control | kernel | recovery | safety | device")
        sys.exit(1)

    module = sys.argv[1]

    if module == "control":
        master_control.main()
    elif module == "kernel":
        kernel_forge.main()
    elif module == "recovery":
        recoverymanager.main()
    elif module == "safety":
        flashguard.main()
    elif module == "device":
        deviceprobe.main()
    else:
        print("Unknown module")

if __name__ == "__main__":
    main()
