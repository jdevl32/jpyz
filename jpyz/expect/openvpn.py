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
                        (
                            ipaddr=\
                                network.getInterfaceIPAddress(interface=Default.NETWORK_TUNNEL_INTERFACE)
                        )
                    ,
                    "[SIGINT] to terminate..."
                ]
            )
        )
    spawn.interact()


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

    secure = _secure_.get(__file__)
    # todo: constant(s)
    password = secure.get("password", None)
    passphrase = secure.get("passphrase", None)
    spawn = pexpect.spawnu("su")
    pattern = None
    # todo: !!! need to handle bad password/passphrase !!!
    value = common.expectSendPassword(spawn=spawn, password=password, pattern=pattern)
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
        )
    fileName = "client.ovpn"
    command = "openvpn"

    spawn.sendline("{} \"{}\"".format(command, os.path.join(filePath, fileName)))

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
