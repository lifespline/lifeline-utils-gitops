import re
import sys
from util.log import log
from functools import reduce
from subprocess import check_output, STDOUT

def help(msg):
    """Prints help statement.
    """    
    log(msg)

def exec(cmd):
    res = check_output(cmd, stderr=STDOUT, shell=True)
    res = res.decode('utf-8').strip()

    return res

