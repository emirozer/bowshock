import unittest
import sys
from time import sleep

sys.path.append("../bowshock/")

from skymorph import search_orbit, search_position, search_target_obj


class skymorph_UnitTests(unittest.TestCase):
    def test_skymorph_object_search(self):

        r = search_target_obj("J99TS7A")
        self.assertEqual(r.status_code, 200)
        sleep(2)


if __name__ == "__main__":
    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(skymorph_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
