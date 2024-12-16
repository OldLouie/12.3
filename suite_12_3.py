import unittest
import tests_12_3

suite_test = unittest.TestSuite()
suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

rr = unittest.TextTestRunner(verbosity=2)

rr.run(suite_test)
