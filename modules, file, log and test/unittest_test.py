import unittest

"""
《Python编程从入门到实践》习题11-1
"""
def city_coun(city, country):
    full = city + ", " + country
    return  full.title()

class CityCounTest(unittest.TestCase):

   def test_city_country(self):
       formatted = city_coun("santiago", "chile")
       self.assertEqual(formatted, "Santiago, Chile")

unittest.main()