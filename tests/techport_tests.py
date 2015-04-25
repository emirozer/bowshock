import unittest
import sys
from time import sleep

sys.path.append("../bowshock/")

from techport import techport


class techport_UnitTests(unittest.TestCase):
    def test_techport_api(self):

        r = techport(Id="4795")
        self.assertEqual(r.status_code, 200)
        sleep(2)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(techport_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
