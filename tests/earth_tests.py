import unittest
import requests
import sys
from time import sleep

sys.path.append("../bowshock/")

from earth import imagery, assets


class earth_UnitTests(unittest.TestCase):
        
    def test_imagery_endpoint_full(self):
        
        r = imagery(lon=100.75, lat=1.6, dim=0.0025, date="2015-02-02", cloud_score=True)
        sleep(2)

    def test_imagery_endpoint_nodim(self):
        
        r = imagery(lon=100.75, lat=1.6, date="2015-02-02", cloud_score=True)
        sleep(2)

    def test_imagery_endpoint_nocloudscore(self):
        
        r = imagery(lon=100.75, lat=1.6, date="2015-02-02")
        sleep(2)

    def test_imagery_endpoint_nodate(self):
        
        r = imagery(lon=100.75, lat=1.6)
        sleep(2)

    def test_assets_endpoint_noenddate(self):
        
        r = assets(lon=100.75, lat=1.6, begin="2015-02-02")
        sleep(2)

    def test_assets_endpoint_full(self):
        
        r = assets(lon=100.75, lat=1.6, begin="2015-02-02", end="2015-02-10")
        sleep(2)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(earth_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
