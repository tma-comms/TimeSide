# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2009 Guillaume Pellerin <yomguy@parisson.com>

# This file is part of TimeSide.

# TimeSide is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# TimeSide is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with TimeSide.  If not, see <http://www.gnu.org/licenses/>.

# Author: Guillaume Pellerin <yomguy@parisson.com>

from timeside.api import IProcessor

class IAnalyzer(IProcessor):
    """Media item analyzer driver interface"""

    @staticmethod
    def id():
        """Return a short id alphanumeric, lower-case string."""

    @staticmethod
    def name():
        """Return the analyzer name, such as "Mean Level", "Max level",
        "Total length, etc..
        """

    @staticmethod
    def unit():
        """Return the unit of the data such as "dB", "seconds", etc...
        """

    def render(self, media, options=None):
        """Return the result data of the process"""

