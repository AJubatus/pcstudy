import re
import glob
import sys
from collections import defaultdict


def constructProcDict():
    procDict = defaultdict(list)
    pidToName = {}
    processes = glob.iglob('/proc/*/status')
    for procStatus in processes:
        with open(procStatus) as status:
            for line in status:
                if line.startswith('Pid:'):
                    pid = int(line.split()[-1])
                if line.startswith('PPid:'):
                    ppid = int(line.split()[-1])
                if line.startswith('Name:'):
                    name = line.split()[-1]
            procDict[ppid].append(pid)
            pidToName[pid] = name
    return procDict, pidToName


def printTree(tree, pidToName, parent=1, indent=''):
    print(parent, pidToName[parent])
    if parent not in tree:
        return
    for child in tree[parent][:-1]:
        # Everything but last child
        sys.stdout.write(indent + '├')
        printTree(tree, pidToName, child, indent + '│ ')
    # Print last child in list with different indent character
    child = tree[parent][-1]
    sys.stdout.write(indent + '└')
    printTree(tree, pidToName, child, indent + ' ')


def pstree():
    procDict, pidToName = constructProcDict()
    printTree(procDict, pidToName)


pstree()
