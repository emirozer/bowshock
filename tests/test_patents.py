import unittest
import sys
from time import sleep

sys.path.append("../bowshock/")

from bowshock import patents

class patents_UnitTests(unittest.TestCase):
    def test_patents_endpoint_full(self):

        r = patents.patents(query="temperature", concept_tags=True, limit=5)
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_patents_endpoint_notags(self):

        r = patents.patents(query="temperature", limit=5)
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_patents_endpoint_nolimit(self):

        r = patents.patents(query="temperature")
        self.assertEqual(r.status_code, 200)
        sleep(2)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(patents_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
