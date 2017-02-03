#!/usr/bin/env python3
# exit.py

"""
...
"""

from jpyz.decorator.context.configurable import ConfigurableContextDecorator
from jpyz.default import Default


class ExitContextDecorator(ConfigurableContextDecorator):
    """
    ...
    """

    def __init__(self, _exitTag=Default.EXIT_TAG):
        """
        ...
        :param _exitTag:
        :type _exitTag: str
        """

        ConfigurableContextDecorator.__init__(self, _enterTag=None, _exitTag=_exitTag)
