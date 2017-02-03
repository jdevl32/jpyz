#!/usr/bin/env python3
# default.py

"""
...
"""

import inspect
import os
import platform

from jpyz import common
from jpyz.constant import Constant


class Default:
    """
    ...
    """

    CONNECTION_TIMEOUT = 20

    CONNECTION_TIMEOUT_MESSAGE = "Connection timeout"

    DESCRIPTOR_VALUE_SEPARATOR = Constant.EQUAL_SIGN

    DEVELOPMENT_DIR_NAME = "Development"

    DOCUMENT_DIR_NAME = "Document"

    DOCUMENTS_DIR_NAME = "{}s".format(DOCUMENT_DIR_NAME)

    DOWNLOAD_DIR_NAME = "Download"

    DOWNLOADS_DIR_NAME = "{}s".format(DOWNLOAD_DIR_NAME)

    ENTER_TAG = "~~~> ENTER ~~~>"

    EXIT_TAG = "<~~~ EXIT <~~~"

    FORMAT_TRACE = "[{tag}{an}{descriptor}{nv}{value}]"

    IMAGE_DIR_NAME = "Image"

    LINUX_DATA_DIR_NAME = "data"

    LINUX_MOUNT_DIR_NAME = "mnt"

    LINUX_SYSTEM_CONFIG_DIR_NAME = "etc"

    MEDIA_DIR_NAME = "Media"

    MUSIC_DIR_NAME = "Music"

    NETWORK_ETHERNET_INTERFACE = "eth0"

    NETWORK_TUNNEL_INTERFACE = "tun0"

    OPENVPN_SUCCESS_MESSAGE = "Initialization Sequence Completed"

    PHOTO_DIR_NAME = "Photo"

    PICTURE_DIR_NAME = "Picture"

    PICTURES_DIR_NAME = "{}s".format(PICTURE_DIR_NAME)

    PLATFORM_SYSTEM_JAVA = Constant.JAVA

    PLATFORM_SYSTEM_LINUX = Constant.LINUX

    PLATFORM_SYSTEM_WINDOWS = Constant.WINDOWS

    PROJECT_DIR_NAME = "Project"

    PROJECTS_DIR_NAME = "{}s".format(PROJECT_DIR_NAME)

    PROMPT = "[Enter] to continue..."

    SCAN_DIR_NAME = "Scan"

    SHARE_STORAGE_DIR_NAME = "[Storage]"

    SSID_HOME = "1030 E Avery Ct NW"

    TAG_DESCRIPTOR_SEPARATOR = Constant.COLON

    USER_PROFILE_DIR_EXP = Constant.TILDE

    VIDEO_DIR_NAME = "Video"

    VIDEOS_DIR_NAME = "{}s".format(VIDEO_DIR_NAME)

    WINDOWS_ROOT_DRIVE_LETTER = "C"

    WINDOWS_DATA_DRIVE_LETTER = "D"

    WINDOWS_DATA_DIR_NAME = "[{} {}]".format(WINDOWS_DATA_DRIVE_LETTER, Constant.DRIVE)

    WINDOWS_OFFLINE_DIR_NAME = "Offline"

    WINDOWS_ROOT_DRIVE = "{}{}".format(WINDOWS_ROOT_DRIVE_LETTER, Constant.COLON)


def _getPlatformPath(platformPathFunctionMap, system, default):
    return \
        platformPathFunctionMap.get \
            (
                platform.system() if common.isNullOrEmpty(system) else system
                ,
                default
                if inspect.isfunction(default)
                else lambda value: value if common.isNull(value) else str(value)
            )()


def getLinuxDataPath():
    return os.path.join(getLinuxMountPath(), Default.LINUX_DATA_DIR_NAME)


def getLinuxMountPath():
    return os.path.join(getLinuxRootPath(), Default.LINUX_MOUNT_DIR_NAME)


def getLinuxRootPath():
    return os.sep


def getLinuxStoragePath():
    return os.path.join(getLinuxDataPath(), Default.SHARE_STORAGE_DIR_NAME)


def getLinuxSystemConfigPath():
    return os.path.join(getLinuxRootPath(), Default.LINUX_SYSTEM_CONFIG_DIR_NAME)


def getWindowsDataPath():
    return os.path.join(getWindowsRootPath(), Default.WINDOWS_OFFLINE_DIR_NAME, Default.WINDOWS_DATA_DIR_NAME)


def getWindowsRootPath_00(drive=None):
    return \
        "{}{}".format\
            (
                Default.WINDOWS_ROOT_DRIVE_LETTER if common.isNull(drive) else drive
                ,
                Constant.COLON
            )


def getWindowsRootPath(drive=None):
    return \
        "{}{}{}".format\
            (
                Default.WINDOWS_ROOT_DRIVE_LETTER if common.isNull(drive) else drive
                ,
                Constant.COLON
                ,
                os.sep
            )


def getWindowsStoragePath():
    return os.path.join(getWindowsDataPath(), Default.SHARE_STORAGE_DIR_NAME)


def getPlatformDataPath(system=None, default=None):
    """
    ...
    :param system:
    :type system: str
    :param default:
    :type default: object
    :return:
    :rtype: str
    """

    return \
        _getPlatformPath \
            (
                {
                    Default.PLATFORM_SYSTEM_LINUX: getLinuxDataPath
                    ,
                    Default.PLATFORM_SYSTEM_WINDOWS: getWindowsDataPath
                }
                ,
                system
                ,
                default
            )


def getPlatformRootPath(system=None, default=None):
    """
    ...
    :param system:
    :type system: str
    :param default:
    :type default: object
    :return:
    :rtype: str
    """

    return \
        _getPlatformPath \
            (
                {
                    Default.PLATFORM_SYSTEM_LINUX: getLinuxRootPath
                    ,
                    Default.PLATFORM_SYSTEM_WINDOWS: getWindowsRootPath
                }
                ,
                system
                ,
                default
            )


def getPlatformStoragePath(system=None, default=None):
    """
    ...
    :param system:
    :type system: str
    :param default:
    :type default: object
    :return:
    :rtype: str
    """

    return \
        _getPlatformPath \
            (
                {
                    Default.PLATFORM_SYSTEM_LINUX: getLinuxStoragePath
                    ,
                    Default.PLATFORM_SYSTEM_WINDOWS: getWindowsStoragePath
                }
                ,
                system
                ,
                default
            )
