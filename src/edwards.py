
from gmpy2 import is_prime

class Point(object):
    __slots__ = ('x','y','z')
    def __init__(self,x=None,y=None):
        self.x = x
        self.y = y


class FiniteField(object):
    __slots__ = ('p')

    def __init__(self,p=None):

        assert is_prime(p)
class EdwardsCurve(FiniteField):
    """
    x^2 + y^2 = 1 + d*x^2*y^2
    char(k)
    k != 2
    d = k - 0||1

    """


    def __add__(self, p, q, d):
        x1,y1 = p[0],p[1]
        x2,y2 = q[0],q[1]
        x3 = (y1*y2+y1*x2)/(1 + d*x1*x2*y1*y2)
        y3 = (y1*y2 - x1*x2)/(1 - d*x1*x2*y1*y2())
        return Point(x3,y3)


    """
 Return a new Weierstrass model of self under the standard
   transformation (u,r,s,t)

      (x,y)  |-->  (x',y') = (u^2x + r , u^3y + su^2x + t).

   EXAMPLES:

      sage: E = EllipticCurve('15a')
      sage: F1 = E.change_weierstrass_model([1/2,0,0,0]); F1
      Elliptic Curve defined by y^2 + 2*x*y + 8*y = x^3 + 4*x^2 - 160*x - 640 over Rational Field
      sage: F2 = E.change_weierstrass_model([7,2,1/3,5]); F2
      Elliptic Curve defined by y^2 + 5/21*x*y + 13/343*y = x^3 + 59/441*x^2 - 10/7203*x - 58/117649 over Rational Field
      sage: F1.is_isomorphic(F2)
      True
    """