#!/usr/bin/env python3
# import.py

"""
...
"""

import os
import sys


def importByName(name):
    """
    Import module by name.  Supports importing module of package.

    :param name:
        Name of the module (or package).
    :type name: str

    :return:
        Module imported.
    :rtype: str
    """

    __import__(name)
    return sys.modules[name]


def importByFilePath(filePath):
    """
    Import module by source file path.

    :param filePath:
        Full file path of source.
    :type filePath: str

    :return:
        Module imported by extracting name from source file path.
    :rtype: module
    """

    filePath, fileName = os.path.split(filePath)
    sysPath = list(sys.path)

    sys.path.insert(0, filePath)

    try:
        return __import__(os.path.splitext(fileName)[0])
    finally:
        sys.path[:] = sysPath
