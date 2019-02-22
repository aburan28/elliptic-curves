
from params import curves
import random



class Ecdsa(object):

	def __init__(self,curve):
		self.curve = curve

	def sign(self,message):
		n = self.curve["n"]
		G = self.curve["G"]
		k = random.randint(1,n-1)
        x1,y1 = k * G
#Pick a random integer k [1,n-1]
#Compute (x1, y1) = k·G
#r = x1 mod n
#s = k-1(z + rdS) mod n
#The signature is the pair (r, s)


def sign():




def verify():



