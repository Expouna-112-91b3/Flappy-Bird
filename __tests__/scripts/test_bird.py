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
        
if __name__ == '__main__':
    unittest.main()
        