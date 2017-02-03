#!/usr/bin/env python3
# important.py

"""
...
"""

import sys

from contextlib import ContextDecorator
from jpyz import common as jpyzCommon
from jpyz.constant import Constant
from jpyz.decorator.context.enter import EnterContextDecorator
from jpyz.decorator.context.exit import ExitContextDecorator


class ImportAnt(ContextDecorator):
    """
    ...
    """

    @EnterContextDecorator()
    def __enter__(self):
        """
        ...
        :return:
        :rtype: ImportAnt
        """

        self._fileDirPath = Constant.EMPTY

        if jpyzCommon.isImport():
            self._fileDirPath = jpyzCommon.getFileDirPathNotInSysPath()

            if not jpyzCommon.isNullOrEmpty(self._fileDirPath):
                sys.path.insert(0, self._fileDirPath)

        return self

    @ExitContextDecorator()
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        ...
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """

        if not jpyzCommon.isNullOrEmpty(self._fileDirPath):
            sys.path.remove(self._fileDirPath)

        return False
