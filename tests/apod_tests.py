import unittest
import sys
from time import sleep

sys.path.append("../bowshock/")

from apod import apod


class apod_UnitTests(unittest.TestCase):
    def test_apod_endpoint_full(self):

        r = apod(date="2015-02-02", concept_tags=True)
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_apod_endpoint_notags(self):

        r = apod(date="2015-02-02")
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_apod_endpoint_noargs(self):
        # no tags should pass , as no date defaults to today
        r = apod()
        self.assertEqual(r.status_code, 200)
        sleep(2)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(apod_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
