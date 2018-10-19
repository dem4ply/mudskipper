import json
from unittest import TestCase
from unittest.mock import patch, ANY
from mudskipper import Endpoint
from mudskipper.endpoint import GET, POST
import time
import datetime
from mudskipper.timekeeper import Timekeeper


class Test_timekeeper( TestCase ):
    def setUp( self ):
        self.timekeeper = Timekeeper()

    def test_delta_should_be_the_diff_between_start_and_end( self ):
        now = datetime.datetime.now()
        ten_seconds_delta = datetime.timedelta( seconds=10 )
        ten_seconds_in_the_past = now - ten_seconds_delta
        self.timekeeper.start = ten_seconds_in_the_past
        self.timekeeper.end = now
        self.assertEqual( self.timekeeper.delta, ten_seconds_delta )
