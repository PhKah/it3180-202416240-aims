import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title

class TestSearch(unittest.TestCase):
    def test_search_case_insensitive(self):
        items = [DigitalVideoDisc("The Lion King", "Animation", cost=19.95)]
        results = search_by_title(items, "lion")
        self.assertEqual(len(results), 1)

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i}", "Category", "Director", 90, 10.0)
            self.assertTrue(cart.add_dvd(dvd))
        
        overflow_dvd = DigitalVideoDisc("DVD 21", "Category", "Director", 90, 10.0)
        self.assertFalse(cart.add_dvd(overflow_dvd))

        def test_total_cost_with_discount(self):
            cart = Cart()
            dvd = DigitalVideoDisc("DVD 1", "Category", "Director", 90, 100.0)
            cart.add_dvd(dvd)
            
            self.assertEqual(cart.total_cost_with_discount(20), 80.0)
            
            with self.assertRaises(ValueError):
                cart.total_cost_with_discount(150)
if __name__ == "__main__":
    unittest.main()
