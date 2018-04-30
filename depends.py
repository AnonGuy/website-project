import os
from sys import path

depends = [
    step[0] for step in
    os.walk(
        os.path.dirname(os.path.realpath(__file__))
    )
    if len(step[0].split('\\')) == 9
]

for folder in depends:
    path.append(folder)