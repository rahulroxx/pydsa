# !/usr/bin/env python
'''
This module automatically checks for pep8 format.
It scans the complete folder, searches for python files
(ignoring the virtual environment python files) and automatially
format it according to pep8 format using a python plugin 'autopep8'.
'''

import os
import autopep8
import sys

BASE_DIR = os.path.abspath(__file__)


def format_file(path):
    '''
    The function, using 'for' loop scans all the directories as well
    as sub-directories of the folder for python file and checks
    for pep8 format.
    '''
    p = ""
    for dirpath, _, filenames in os.walk(path):
        if os.path.exists(os.path.join(dirpath, 'bin/activate')):
            p = dirpath
        for file_ in filenames:
            if file_.endswith('.py'):
                file_ = os.path.abspath(os.path.join(dirpath, file_))
                if (not bool(p)) and os.access(file_, os.W_OK):
                    try:
                        temp_file = open(file_, 'r')
                        source_code = temp_file.read()
                        temp_file.seek(0)
                        temp_file = open(file_, 'w')
                        temp_file.truncate()
                        temp_file.write(autopep8.fix_code(source_code))
                        temp_file.close()
                    except:
                        print(file_)
                        print(sys.exc_info()[0])


if __name__ == "__main__":
    path_of_dir = [
        os.path.dirname(BASE_DIR),
    ]
    for x in path_of_dir:
        format_file(x)
