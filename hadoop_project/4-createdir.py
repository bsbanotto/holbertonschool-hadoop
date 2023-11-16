#!/usr/bin/python2
"""
Utilize Snakebite to create all directories in a list
"""
from snakebite.client import Client


def createdir(l):
    """
    Args:
        l: list of directories to create withing HDFS
    """
    client = Client('localhost', 9000)

    for created_dir in client.mkdir(l, create_parent=True):
        print(created_dir)


if __name__ == "__main__":
    createdir(["/holbies/input"])
