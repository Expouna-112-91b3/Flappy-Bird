import unittest

from scripts.bird import Bird

class TestBird(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.bird = Bird()

    def test_die(self):
        self.assertTrue(self.bird.get_is_alive())
        self.bird.die()
        self.assertFalse(self.bird.get_is_alive())

    def test_gravity(self):
        self.bird.apply_gravity()
        expected_acceleration = 0.1
        self.assertEqual(
            self.bird.get_acceleration(), 
            expected_acceleration
        )

    def test_bird_flap(self):
        self.bird.flap()
        expected_acceleration = .5
        self.assertEqual(
            self.bird.get_acceleration(),
            expected_acceleration
        )
        
if __name__ == '__main__':
    unittest.main()
        