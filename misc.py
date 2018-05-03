import os
import sys

def get_install_dir():
    return os.path.dirname(os.path.abspath(__file__))

def fail_if(condition, msg, end='\n'):
    if condition:
        fail(msg, end=end)

def fail(msg, end='\n'):
    print(msg, file=sys.stderr, end=end)
    exit(1)
