#!/usr/bin/env python3

# Author ID: asallese2

import subprocess

def free_space():
    p = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    output, _ = p.communicate()
    
    stdout = output.decode('utf-8').strip()
    return stdout

if __name__ == "__main__":
    result = free_space()
    print(result)

