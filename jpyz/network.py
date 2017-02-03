#!/usr/bin/env python3
# network.py

"""
...
"""

from jpyz import common
from jpyz.default import Default

import os
import pexpect


def getInterfaceIPAddress(interface=None):
    """
    ...
    :param interface:
    :type interface: str
    :return:
    :rtype: str
    """

    # _cmd_ = "ifconfig"
    # _cmd_ = "ifconfig {}".format(interface)
    # common.trace(value=_cmd_)
    return \
        pexpect.run \
            (
                common.getShellCommand\
                    (
                        "ifconfig {iface} | grep 'inet addr' | cut -d: -f2 | cut -d' ' -f1".format\
                            (
                                iface=\
                                    Default.NETWORK_ETHERNET_INTERFACE if common.isNull(interface) else interface
                            )
                    )
            ) \
            .decode().strip(os.linesep)


def getSSID():
    """
    ...
    :return:
    :rtype: str
    """

    return pexpect.run("iwgetid -r").decode()


def isSSIDHome(homeSSID=None):
    """
    ...
    :param homeSSID:
    :type homeSSID: str
    :return:
    :rtype: bool
    """

    return getSSID().startswith(Default.SSID_HOME if common.isNullOrEmpty(homeSSID) else homeSSID)
