import unittest
from unittest import TestCase


def frozen(func):
    def wrapper(atr):
        if atr.is_frozen == True:
            atr.skipTest('Тесты в этом кейсе заморожены')
        else:
            return func

    return wrapper


import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        for i in range(10):
            runner1 = Runner('Olha')
            runner1.walk()
        self.assertEqual(runner1.distance, 5)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner2 = Runner('Petro')
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner('Olha')
        runner2 = Runner('Petro')
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance == runner2.distance, None)


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.first = Runner('Усэйн', 10)
        self.second = Runner('Андрей', 9)
        self.third = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        tournament_1 = Tournament(90, self.first, self.third)
        result = tournament_1.start()
        self.all_results[1] = result
        self.assertTrue(result[max(result)] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        tournament_2 = Tournament(90, self.second, self.third)
        result = tournament_2.start()
        self.all_results[2] = result
        self.assertTrue(result[max(result)] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        tournament_3 = Tournament(90, self.first, self.second, self.third)
        result = tournament_3.start()
        self.all_results[3] = result
        self.assertTrue(result[max(result)] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for tournament, results in cls.all_results.items():
            print(f'{tournament}: {{{', '.join([f'{place}: {name}' for place, name in results.items()])}}}')


if __name__ == '__main__':
    unittest.main()
if __name__ == '__main__':
    unittest.TestCase()
