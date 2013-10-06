#!/usr/bin/env python
# 

import math
import tfidf
import unittest

DEFAULT_IDF_UNITTEST = 1.0

def get_exected_idf(num_docs_total, num_docs_term):
   return math.log(float(1 + num_docs_total) / (1 + num_docs_term))

class TfIdfTest(unittest.TestCase):

  def testKeywords(self):
    """Test retrieving keywords from a document, ordered by tf-idf."""
    my_tfidf = tfidf.TfIdf("tfidf_testcorpus.txt", DEFAULT_IDF = 0.01)

    # Test retrieving keywords when there is only one keyword.
    keywords = my_tfidf.get_doc_keywords("the spoon and the fork")
    self.assertEqual("the", keywords[0][0])
    print keywords
  

def main():
  unittest.main()

if __name__ == '__main__':
  main()
