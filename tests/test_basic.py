from nose.plugins.skip import SkipTest
from nose.tools import assert_raises, nottest
from isu.autocomplete import datafile

#@SkipTest


class TestBasic:

    def setUp(self):
        pass

    def test_datafile(self):
        df = datafile("foo")
        print("DF:", df)
        assert df.endswith("foo")

    def tearDown(self):
        pass
