# Databricks notebook source
# MAGIC %md
# MAGIC This Program prints the Operating System details on the console

# COMMAND ----------

# Script Name		: osinfo.py
# Authors		    : {Amit Dixit after Forking the Git repo from 'geekcomputers'}
# Created		    : 10th August 2025
# Version		    : 1.0
# Usage			    : "python OSInfo.py"
# Dependencies		: platform module
# License		    : GNU General Public License v3.0
# Description		: Displays some information about the OS you are running this script on

import platform as pl

profile = [
    "architecture",
    "linux_distribution",
    "mac_ver",
    "machine",
    "node",
    "platform",
    "processor",
    "python_build",
    "python_compiler",
    "python_version",
    "release",
    "system",
    "uname",
    "version",
]


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


for key in profile:
    if hasattr(pl, key):
        print(key + bcolors.BOLD + ": " + str(getattr(pl, key)()) + bcolors.ENDC)