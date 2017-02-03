#!/usr/bin/env python3
# configurable.py

"""
...
"""

from contextlib import ContextDecorator
from jpyz import common as jpyzCommon
from jpyz.default import Default


class ConfigurableContextDecorator(ContextDecorator):
    """
    ...
    """

    def __init__(self, _enterTag=Default.ENTER_TAG, _exitTag=Default.EXIT_TAG):
        """
        ...
        :param _enterTag:
        :type _enterTag: str
        :param _exitTag:
        :type _exitTag: str
        """

        self._enterTag = _enterTag
        self._exitTag = _exitTag

    def __enter__(self):
        """
        ...
        :return:
        :rtype: ConfigurableContextDecorator
        """

        if not jpyzCommon.isNullOrEmpty(self._enterTag):
            jpyzCommon.trace(tag=self._enterTag)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        ...
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """

        if not jpyzCommon.isNullOrEmpty(self._exitTag):
            jpyzCommon.trace(tag=self._exitTag)
