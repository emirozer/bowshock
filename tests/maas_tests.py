import unittest
import requests
import sys
from time import sleep

sys.path.append("../bowshock/")

from maas import maas_latest, maas_archive

class maas_UnitTests(unittest.TestCase):
        
    def test_maas_latest_endpoint(self):
        
        r = maas_latest()
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_maas_archive_endpoint_w_dates(self):
        
        r = maas_archive('2012-10-01', '2012-10-31')
        self.assertEqual(r.status_code, 200)
        sleep(2)


        

if __name__ == "__main__":
    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(maas_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
