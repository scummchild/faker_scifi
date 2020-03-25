import unittest

from faker import Faker
from faker_scifi import SciFi

class TestEnUS(unittest.TestCase):
    def setUp(self):
        self.fake = Faker('en_US')
        self.fake.add_provider(SciFi)
        Faker.seed(0)

    def test_babble(self):
        assert self.fake.babble() == 'disengage the external inertial fluctuations'
        assert self.fake.babble() == 'discharge the neutrino log'
        assert self.fake.babble() == 'project the source of the energies'
        assert self.fake.babble() == 'disrupt the anti- fields'
        assert self.fake.babble() == 'experience the upper overloaders'

        self.assertIsInstance(self.fake.babble(), str)
