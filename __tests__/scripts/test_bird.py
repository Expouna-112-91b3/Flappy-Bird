import unittest

from scripts.bird import Bird

class TestBird(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bird = Bird()
    
    def test_die(self):
        self.bird.die()
        self.assertFalse(self.bird.get_is_alive())
        
if __name__ == '__main__':
    unittest.main()
        