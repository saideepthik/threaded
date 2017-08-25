#    Copyright 2017 Alexey Stepanov aka penguinolog
##
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Python 2 pooled implementation.

Uses backport of concurrent.futures.
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import six

from . import _base_pooled

__all__ = (
    'ThreadPooled',
)


class ThreadPooled(_base_pooled.BasePooled):
    """ThreadPoolExecutor wrapped."""

    __slots__ = ()

    def _get_function_wrapper(self, func):
        """Here should be constructed and returned real decorator.

        :param func: Wrapped function
        :type func: typing.Callable
        :return: wrapped function
        :rtype: typing.Callable
        """
        # pylint: disable=missing-docstring
        # noinspection PyMissingOrEmptyDocstring
        @six.wraps(func)
        def wrapper(*args, **kwargs):
            return self.executor.submit(func, *args, **kwargs)
        # pylint: enable=missing-docstring
        return wrapper