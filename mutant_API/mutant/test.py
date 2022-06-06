from django.test import TestCase
from pip import main
import sys
sys.path.append("./mutant")
import models, isMutant

import unittest

class mutantTest(unittest.TestCase):
    
    
    def test_isMutant(self):
        self.assertTrue(isMutant(     
        {"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"] 
        } 
        ))

if __name__ == "__main__":
    unittest.main()
