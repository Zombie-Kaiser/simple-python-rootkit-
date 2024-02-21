# simple-python-rootkit-
a simple python rootkit
This script uses Windows Management Instrumentation (WMI) to iterate through all running processes on the system and kill any process that is not 'System Idle Process.' It does this by using `taskkill`, a command-line tool for terminating tasks in Windows. While this example is simple, it demonstrates how one could create a Python rootkit capable of exploiting vulnerabilities within a Windows environment to gain unauthorized access and control over the victim's computer.

Please note that creating or using such scripts without permission is illegal and highly discouraged.
