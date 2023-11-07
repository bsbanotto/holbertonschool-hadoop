#!/usr/bin/python2
"""
Deletes directories from a list
"""


def deletedir(l):
    """
    Args:
        l: list of strings of directories to delete
    """
    from snakebite.client import Client
    client = Client('localhost', 9000)

    try:
        for deleted_dir in client.delete(l, recurse=True):
            print(deleted_dir)
    except Exception:
        pass
