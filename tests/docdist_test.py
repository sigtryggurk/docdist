import os, sys
import unittest
import math

sys.path.insert(0, os.path.abspath('..'))
from docdist.docdist import doc_dist, doc_dist_pairs

class TestDocDistMethods(unittest.TestCase):
  def test_doc_dist(self):
    word_list1 = ["a", "b", "c", "b", "a", "c", "d", "d"]
    word_list2 = ["a", "a"]

    self.assertAlmostEqual(doc_dist(word_list1, word_list2), math.pi/3)

  def test_doc_dist_pairs(self):
    word_list1 = ["a", "b"]
    word_list2 = ["b", "a"]

    self.assertAlmostEqual(doc_dist(word_list1, word_list2), 0)
    self.assertAlmostEqual(doc_dist_pairs(word_list1, word_list2), math.pi/2)

    word_list1 = ["a", "b", "c"]
    word_list2 = ["a", "b", "c"]

    self.assertAlmostEqual(doc_dist_pairs(word_list1, word_list2), 0)

  def test_doc_dist_50(self):
    word_list1 = [chr(i) for i in range(65,123)] * 2 + ["siggi"]
    word_list2 = [chr(i) for i in range(65,123)] * 2 + ["kjartansson"]

    self.assertNotAlmostEqual(doc_dist(word_list1, word_list2), 0)
    self.assertAlmostEqual(doc_dist(word_list1, word_list2, 50), 0)

if __name__ == '__main__':
  unittest.main()
