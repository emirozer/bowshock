import unittest
import sys
from time import sleep

sys.path.append("../bowshock/")

from asterank import asterank


class asterank_UnitTests(unittest.TestCase):
    def test_asterank_api_full(self):

        r = asterank(
            query={"e": {"$lt": 0.1},
                   "i": {"$lt": 4},
                   "a": {"$lt": 1.5}},
            limit=1)
        self.assertEqual(r.status_code, 200)
        sleep(2)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(asterank_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
