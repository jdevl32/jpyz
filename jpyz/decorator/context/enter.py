#!/usr/bin/env python3
# enter.py

"""
...
"""

from jpyz.decorator.context.configurable import ConfigurableContextDecorator
from jpyz.default import Default


class EnterContextDecorator(ConfigurableContextDecorator):
    """
    ...
    """

    def __init__(self, _enterTag=Default.ENTER_TAG):
        """
        ...
        :param _enterTag:
        :type _enterTag: str
        """

        ConfigurableContextDecorator.__init__(self, _enterTag=_enterTag, _exitTag=None)
