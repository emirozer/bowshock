import unittest
import sys
from time import sleep

sys.path.append("../bowshock/")

from helioviewer import getjp2image, getjp2header

class helioviewer_UnitTests(unittest.TestCase):
        
    def test_helioviewer_api_getjp2image(self):
        
        r = getjp2image(date='2014-01-01T23:59:59', sourceId=14)
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_helioviewer_api_getjp2header(self):
        
        r = getjp2header(Id=7654321)
        self.assertEqual(r.status_code, 200)
        sleep(2)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(helioviewer_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
