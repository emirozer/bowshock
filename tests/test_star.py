import unittest
import sys

sys.path.append("../bowshock/")

from time import sleep
from bowshock import star


class star_UnitTests(unittest.TestCase):
    def test_stars(self):

        r = star.stars()
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_search_star(self):

        r = star.search_star("Sun")
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_exoplanets(self):

        r = star.exoplanets()
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_search_exoplanet(self):

        r = star.search_exoplanet("11 Com")
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_local_group_of_galaxies(self):

        r = star.local_group_of_galaxies()
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_search_local_galaxies(self):

        r = star.search_local_galaxies("IC 10")
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_star_clusters(self):

        r = star.star_clusters()
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_search_star_clusters(self):

        r = star.search_star_cluster("Berkeley 59")
        self.assertEqual(r.status_code, 200)
        sleep(2)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(star_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
