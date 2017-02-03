#!/usr/bin/env python3
# common.py

"""
...
"""

from jpyz import common as jpyzCommon

import pexpect


def expectSendPassword(spawn, password, pattern=None):
    """
    ...
    :param spawn:
    :type spawn: SpawnBase
    :param password:
    :type password: str
    :param pattern:
    :type pattern: str
    :return:
    :rtype:
    """

    # jpyzCommon.trace(descriptor="len(password)", value=len(password))

    if jpyzCommon.isNull(pattern):
        spawn.waitnoecho()
    else:
        index = spawn.expect([pattern, pexpect.EOF, pexpect.TIMEOUT])

    bytes = spawn.sendline(password)
    # index = spawn.expect([pexpect.EOF, pexpect.TIMEOUT])
    # return index
    # jpyzCommon.trace(descriptor="bytes", value=bytes)
    # return not spawn.waitnoecho(timeout=5)
    return bytes
