#!/usr/bin/python

import sys
import subprocess

if len(sys.argv)!=3:
  print("Usage: host-list-file ToAddress")
  sys.exit(0)

hostfile = sys.argv[1]
ToAddress = sys.argv[2]

with open(hostfile) as f:
  for line in f.readlines():
    hs = line.strip()
    cmd = "ssh " + hs + " \"traceroute " + ToAddress + "\""
    print("##############################################")
    print("# " + hs )
    print("##############################################")
    print(cmd)
    print("")

    proc = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    results = proc.communicate()
    ( stdout, stderr ) = results
    stdout = stdout.strip()
    stderr = stderr.strip()

    print(stdout)
    print(stderr)
