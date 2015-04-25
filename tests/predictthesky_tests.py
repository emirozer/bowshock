import unittest
import sys
from time import sleep

sys.path.append("../bowshock/")

from predictthesky import space_events


class predictthesky_UnitTests(unittest.TestCase):
        
    def test_spaceevents_endpoint_latlon(self):
        
        r = space_events(lon=100.75, lat=1.5)
        self.assertEqual(r.status_code, 200)
        sleep(2)

if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(predictthesky_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
