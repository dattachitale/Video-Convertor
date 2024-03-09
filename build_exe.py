"""
Created on 21st March 2022 by sdesai
An environment file(*.yml) will be created, provided that you are using a conda env.
This File Will generate EXE For You - SpecFile path must be provided.
"""


import subprocess
from datetime import timedelta
from time import time
import os
import shutil

# Using Rich to Override Print
from rich import pretty
from rich import print
from rich import traceback
# Overriding TraceBack
traceback.install()
pretty.install()

ENVNAME = 'videoEditor'
ENVPATH = os.path.normpath('env\\')

if not os.path.exists(ENVPATH):
    os.makedirs(ENVPATH)

ENVFILE  = os.path.join(ENVPATH, f'{ENVNAME}.yml')
SPECFILE = 'video_editor_controller.spec'

def generateEnvFile():
    global ENVNAME
    global ENVPATH
    global SPECFILE

    if not os.path.exists(ENVPATH):
        os.makedirs(ENVPATH)

    # os.popen("pip freeze > requirement_video_editor_2.txt")

    # Generating Environment File
    p = os.popen(f"conda env export --name {ENVNAME} > {ENVFILE}")
    p.close()

    # Removing illegal utf-8 characters
    with open(ENVFILE, 'rb') as file:
        lines = [line.decode('utf-8') for line in file]

    with open(os.path.normpath(ENVFILE), 'w') as file:
        file.writelines(lines[:-1])

    return None


# EXE Formation
def generateEXE():
    global SPECFILE

    t1 = time()
    shutil.rmtree('dist', ignore_errors=True)
    _exe = subprocess.Popen(f"pyinstaller -y {SPECFILE}", universal_newlines=True)

    if _exe.wait() == 0:
        print("Exe is Ready!")
    t2 = time()
    print(f'Time Took : {timedelta(seconds=t2-t1)}')

    return None


if __name__ == '__main__':
    # generateEnvFile()
    generateEXE()
