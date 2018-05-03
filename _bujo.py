#!/usr/bin/env python3

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BOLD_UNDERLINE = BOLD + UNDERLINE
    NORMAL = ''

def cprint(msg, color):
    print (color + msg + colors.ENDC)

import fileinput

def is_todo(line):
    return len(line) >= 3 and line[2] == '.'

def is_done_etc(line):
    return ((len(line) >= 3 and line[2] in '/x>')
         or (len(line) >= 1 and line[0] in '/x>'))

def is_header(line):
    return line == line.upper()

for line in fileinput.input():
    line = line[:-1]  # strip newline
    if is_todo(line):
        cprint(line, colors.NORMAL)
    elif is_done_etc(line):
        cprint(line, colors.HEADER)
    elif is_header(line):
        cprint(line, colors.BOLD_UNDERLINE)
    else:
        cprint(line, colors.NORMAL)
