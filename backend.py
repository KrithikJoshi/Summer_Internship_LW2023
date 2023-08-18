#!/usr/bin//python3

import subprocess

print("content-type: text/html")
print()

output = subprocess.getoutput("date")
print(output)
