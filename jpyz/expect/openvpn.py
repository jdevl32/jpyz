#!/usr/bin/env python3
# openvpn.py

"""
...
"""

from jpyz import common as jpyzCommon, default, network
from jpyz.default import Default
from jpyz.expect import common
from jpyz.expect import _secure_

import os
import pexpect
import sys


def _success(spawn):
    """
    ...
    :param spawn:
    :type spawn SpawnBase
    :return:
    """

    # todo: constant(s)...
    print\
        (
            os.linesep.join
            (
                [
                    "Connected, IP Address={ipaddr}".format \
                    # "{ipaddr}".format \
                        (
                            ipaddr=\
                                network.getInterfaceIPAddress(interface=Default.NETWORK_TUNNEL_INTERFACE)
                        )
                    ,
                    "[SIGINT] to terminate..."
                ]
            )
        )
    # spawn.setecho(False)
    spawn.interact()
    # spawn.setecho(False)


def _timeout(spawn):
    """
    ...
    :param spawn:
    :type spawn SpawnBase
    :return:
    """

    print(Default.CONNECTION_TIMEOUT_MESSAGE)


def main(arg):
    """
    ...
    :param arg:
    :return:
    """

    # todo: constant(s)
    homeSSID = None

    if network.isSSIDHome(homeSSID):
        print("Safe at home!  :)")
        return

    secure = _secure_.get(__file__)
    password = secure.get("password", None)
    passphrase = secure.get("passphrase", None)
    spawn = pexpect.spawnu("su")
    pattern = None # "(?i)Password: "
    value = common.expectSendPassword(spawn=spawn, password=password, pattern=pattern)

    # spawn.sendline("echo {}".format(jpyzCommon.formatTraceString(descriptor="value", value=value)))
    # jpyzCommon.trace(descriptor="value", value=value)
    
    filePath = os.path.join\
        (
            default.getLinuxSystemConfigPath()
            ,
            "openvpn"
            ,
            "client"
            ,
            "Dell-XPS-L702X"
            ,
            "85270B"
            # ,
            # "2016"
            # ,
            # "06"
            # ,
            # "20"
            # ,
            # "1219"
            # ,
            # ".min"
        )
    fileName = "client.ovpn"
    # command = "ls -lA"
    command = "openvpn"

    spawn.sendline("{} \"{}\"".format(command, os.path.join(filePath, fileName)))

    # pattern = "(?i)Enter Private Key Password: "
    pattern = None
    value = common.expectSendPassword(spawn=spawn, password=passphrase, pattern=pattern)
    value = spawn.expect([Default.OPENVPN_SUCCESS_MESSAGE, pexpect.TIMEOUT], timeout=Default.CONNECTION_TIMEOUT)

    {
        0: _success
        ,
        1: _timeout
    }\
        .get(value, lambda spawn: print("<Um, hello?!?!>"))(spawn)

    spawn.sendline("exit")
    spawn.close()


# determine call method...
if jpyzCommon.isScript():
    # run script...
    main(sys.argv)
