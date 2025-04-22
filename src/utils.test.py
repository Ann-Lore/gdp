import unittest

from utils import calculer_moyenne

class TestMain(unittest.TestCase):
    def test_calculer_moyenne(self):
      liste1 = [1,2,3]
      self.assertEqual(calculer_moyenne(liste1), 2)
      liste2 = []
      self.assertIsNone(calculer_moyenne(liste2))
      liste3 = [2,2.2,1.8]
      self.assertEqual(calculer_moyenne(liste3), 2)
      liste4 = [1,2,"3"]
      self.assertEqual(calculer_moyenne(liste4), 2)
      liste5 = [1, "trois"]
      with self.assertRaises(TypeError):
            calculer_moyenne(liste5)


if __name__ == '__main__':
    unittest.main()
