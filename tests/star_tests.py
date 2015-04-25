import unittest
import sys
from time import sleep

sys.path.append("../bowshock/")

from star import stars, search_star, exoplanets, search_exoplanet, local_group_of_galaxies, search_local_galaxies, star_clusters, search_star_cluster


class star_UnitTests(unittest.TestCase):
    def test_stars(self):

        r = stars()
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_search_star(self):

        r = search_star("Sun")
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_exoplanets(self):

        r = exoplanets()
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_search_exoplanet(self):

        r = search_exoplanet("11 Com")
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_local_group_of_galaxies(self):

        r = local_group_of_galaxies()
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_search_local_galaxies(self):

        r = search_local_galaxies("IC 10")
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_star_clusters(self):

        r = star_clusters()
        self.assertEqual(r.status_code, 200)
        sleep(2)

    def test_search_star_clusters(self):

        r = search_star_cluster("Berkeley 59")
        self.assertEqual(r.status_code, 200)
        sleep(2)


if __name__ == "__main__":

    # Build the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(star_UnitTests))

    # Execute the test suite
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
