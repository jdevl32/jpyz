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

    if jpyzCommon.isNull(pattern):
        spawn.waitnoecho()
    else:
        spawn.expect([pattern, pexpect.EOF, pexpect.TIMEOUT])

    return spawn.sendline(password)
