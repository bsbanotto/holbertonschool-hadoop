#!/usr/bin/python2
"""
Retrieve from HDFS the files listed in L and store them in /tmp
"""


def download(l):
    """
    Args:
        l: list of strings of filed to download to /tmp
    """
    from snakebite.client import Client
    client = Client('localhost', 9000)

    for file in client.copyToLocal(l, '/tmp'):
        print(file)
