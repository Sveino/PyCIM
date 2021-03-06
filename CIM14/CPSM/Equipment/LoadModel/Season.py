# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM14.CPSM.Equipment.Element import Element

class Season(Element):
    """A specified time period of the year, e.g., Spring, Summer, Fall, Winter-  To specify a relative date as the startDate or endDate for a Season, the year component of the ISO 8601 date format (“YYYY-MM-DD”) can be omitted.  The resulting format would be “MM-DD”.
    """

    def __init__(self, startDate='', endDate='', name="fall", SeasonDayTypeSchedules=None, *args, **kw_args):
        """Initialises a new 'Season' instance.

        @param startDate: Date season starts 
        @param endDate: Date season ends 
        @param name: Name of the Season Values are: "fall", "winter", "spring", "summer"
        @param SeasonDayTypeSchedules: Schedules that use this Season.
        """
        #: Date season starts
        self.startDate = startDate

        #: Date season ends
        self.endDate = endDate

        #: Name of the Season Values are: "fall", "winter", "spring", "summer"
        self.name = name

        self._SeasonDayTypeSchedules = []
        self.SeasonDayTypeSchedules = [] if SeasonDayTypeSchedules is None else SeasonDayTypeSchedules

        super(Season, self).__init__(*args, **kw_args)

    _attrs = ["startDate", "endDate", "name"]
    _attr_types = {"startDate": str, "endDate": str, "name": str}
    _defaults = {"startDate": '', "endDate": '', "name": "fall"}
    _enums = {"name": "SeasonName"}
    _refs = ["SeasonDayTypeSchedules"]
    _many_refs = ["SeasonDayTypeSchedules"]

    def getSeasonDayTypeSchedules(self):
        """Schedules that use this Season.
        """
        return self._SeasonDayTypeSchedules

    def setSeasonDayTypeSchedules(self, value):
        for x in self._SeasonDayTypeSchedules:
            x.Season = None
        for y in value:
            y._Season = self
        self._SeasonDayTypeSchedules = value

    SeasonDayTypeSchedules = property(getSeasonDayTypeSchedules, setSeasonDayTypeSchedules)

    def addSeasonDayTypeSchedules(self, *SeasonDayTypeSchedules):
        for obj in SeasonDayTypeSchedules:
            obj.Season = self

    def removeSeasonDayTypeSchedules(self, *SeasonDayTypeSchedules):
        for obj in SeasonDayTypeSchedules:
            obj.Season = None

