#!/usr/bin/env python3
# common.py

"""
...
"""

import os
import sys

from jpyz.constant import Constant
from jpyz.default import Default
from pprint import pprint as _pprint


def _getFrame(depth=0):
    """
    ...
    :param depth:
    :type depth: int
    :return:
    :rtype: frameobject, int
    """

    depth += 1

    return sys._getframe(depth), depth


def _getFrameModuleName(depth=0):
    """
    ...
    :param depth:
    :type depth: int
    :return:
    :rtype: str, int
    """

    frame, depth = _getFrame(depth=1 + depth)
    return frame.f_globals["__name__"], depth


def getFileDirPath(filePath=None):
    """
    ...
    :param filePath:
    :type filePath: str
    :return:
    :rtype: str
    """

    if isNullOrEmpty(filePath):
        filePath = __file__

    return os.path.split(filePath)[0]


def getFileDirPathNotInSysPath(filePath=None):
    """
    ...
    :param filePath:
    :type filePath: str
    :return:
    :rtype: str
    """

    filePath = getFileDirPath(filePath)
    return Constant.EMPTY if filePath in sys.path else filePath


def getShellCommand(command):
    """
    ...
    :param command:
    :type command: str
    :return:
    :rtype: str
    """

    return "/bin/sh -c {q}{cmd}{q}".format(cmd=command, q="\"")


def isEmpty(value):
    """
    ...
    :param value:
    :type value: str
    :return:
    :rtype: bool
    """

    return Constant.EMPTY == value


def isNull(value):
    """
    ...
    :param value:
    :type value: object
    :return:
    :rtype: bool
    """

    return value is None


def isNullOrEmpty(value):
    """
    ...
    :param value:
    :type value: str
    :return:
    :rtype: bool
    """

    return isNull(value) or isEmpty(value)


def isScript(depth=0):
    """
    ...
    :param depth:
    :type depth: int
    :return:
    :rtype: bool
    """

    name, depth = _getFrameModuleName(depth=1 + depth)

    # trace(tag="isScript", descriptor="name", value=name)
    # trace(tag="isScript", descriptor="depth", value=depth)

    return Constant.SCRIPT_MODULE_NAME == name


def isImport(depth=0):
    """
    ...
    :param depth:
    :type depth: int
    :return:
    :rtype: bool
    """

    return not isScript(depth=1 + depth)


def formatTraceString(tag=None, descriptor=None, value=None, tds=None, dvs=None):
    """
    ...
    :param tag:
    :type tag: str
    :param descriptor:
    :type descriptor: str
    :param value:
    :type value: str
    :param tds:
    :type tds: str
    :param dvs:
    :type dvs: str
    :return:
    :rtype: str
    """

    if isNull(tag):
        tag = Constant.EMPTY

    if isNull(descriptor):
        descriptor = Constant.EMPTY

    if isNull(value):
        value = Constant.EMPTY

    noDVS = isNullOrEmpty(descriptor)
    noUse = noDVS and isEmpty(value)

    if isNullOrEmpty(tag) or noUse:
        tds = Constant.EMPTY
    elif isNull(tds):
        tds = Default.TAG_DESCRIPTOR_SEPARATOR

    if noDVS:
        dvs = Constant.EMPTY
    elif isNull(dvs):
        dvs = Default.DESCRIPTOR_VALUE_SEPARATOR

    return Default.FORMAT_TRACE.format(tag=tag, an=tds, descriptor=descriptor, nv=dvs, value=value)


def prompt(prompt=None):
    """
    ...
    :param prompt:
    :type prompt: str
    :return:
    :rtype: str
    """

    # return input(Default.PROMPT if isNullOrEmpty(prompt) else prompt)
    return input(Default.PROMPT if isNull(prompt) else prompt)


def ptrace(tag="pTrace", descriptor=Constant.EMPTY, value=None, tds=None, dvs=None):
    """
    ...
    :param tag:
    :type tag: str
    :param descriptor:
    :type descriptor: str
    :param value:
    :type value: str
    :param tds:
    :type tds: str
    :param dvs:
    :type dvs: str
    """

    _pprint(formatTraceString(tag=tag, descriptor=descriptor, value=value, tds=tds, dvs=dvs))


def trace(tag="Trace", descriptor=Constant.EMPTY, value=None, tds=None, dvs=None):
    """
    ...
    :param tag:
    :type tag: str
    :param descriptor:
    :type descriptor: str
    :param value:
    :type value: str
    :param tds:
    :type tds: str
    :param dvs:
    :type dvs: str
    """

    print(formatTraceString(tag=tag, descriptor=descriptor, value=value, tds=tds, dvs=dvs))
