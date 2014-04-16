#!/usr/bin/env python

import requests

import os


user = os.getlogin()

uid = os.getuid()

uname = os.uname()
# TODO parse out uname results

if uid = 0:
  privs = "root"
else:
  privs = "user"

# TODO generate HTTP POST with pipe-delim system info
# user, privs, uname[]
