
import os
from win32com import client as wmi
from subprocess import call

def main():
    # Initialize WMI object
    wmic = wmi.WMI()

    # Find all processes running on the system
    processes = wmic.ExecQuery('Select * from Win32_Process')

    # Loop through each process and check if it's a valid Windows process
    for p in processes:
        if 'System Idle Process' not in str(p):
            # Kill the process by its name or ID
            call('taskkill /f /im {}'.format(p.Name))

if __name__ == "__main__":
    main()
