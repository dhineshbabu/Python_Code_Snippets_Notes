import unittest
from activities import eat, nap, is_funny,laugh

class ActivityTests(unittest.TestCase):
    def test_eat(self):
        """eat should have a positive message for healthy eating"""
        self.assertEqual(eat("broccoli",is_healthy = True),
                        "I am eating broccoli, because my body is a temple"
                        )
    def test_unhealthy_eat(self):
        """eat should indicate you've given up for eating unhealthy"""
        self.assertEqual(eat("pizza",is_healthy = False),
                        "I am eating pizza, because YOLO"
                        )
        
    def test_eat_healthy_boolean(self):
        """is_healthy must be a boolean"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares?")
        
    def test_short_nap(self):
        """short naps should be refreshing"""
        self.assertEqual(
           nap(1),
            "I am feeling refreshed after 1 hour nap"
                        )
    def test_long_nap(self):
        """long naps should be discouraging"""
        self.assertEqual(
            nap(3),
            "Uggg!!!. I overslept for 3 hours."
                        )
        
    def test_is_funny_tim(self):
        #self.assertEqual(is_funny("kanu"), False) Thi can be re-written as below
        self.assertFalse(is_funny("dhinesh"), "dhinesh should not be funny")
        
    def test_is_funny_anyone_else(self):
        """Anyone else but dhinesh should be funny """
        #self.assertEqual(is_funny("kanu"), False) Thi can be re-written as below
        self.assertTrue(is_funny("kanu"), "dhinesh should be funny")
        self.assertTrue(is_funny("bru"), "dhinesh should be funny")
        self.assertTrue(is_funny("babu"), "dhinesh should be funny")
        
    def test_laugh(self):
        self.assertIn(laugh(), ('lol','ha ha ha', 'thehehe'))
                   
        
# to get the name of the fucntions, we must run the command "python tests.py -v"
if __name__ == "__main__":
    unittest.main()
    
    
