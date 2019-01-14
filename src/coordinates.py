#!/usr/bin/env python

"""
Affine curve equation: y^2 = x^3 + ax + b
The curve equation: y^2
z = x
3 + axz2 + bz3

The relation to the affine: (x : y : z) → (x/z, y/z)
The name: Projective
The curve equation: y
2 = x
3 + axz4 + bz6

The relation to the affine: (x : y : z) → (x/z^2
, y/z^3)
The name: Jacobian

Affine curve equation: y
2 + xy = x
3 + ax2 + b
The curve equation: y
2
z + xyz = x
3 + ax2
z + bz3

The relation to the affine: (x : y : z) → (x/z, y/z)
The name: Projective
The curve equation: y
2 + xyz = x
3 + ax2
z
2 + bz6

The relation to the affine: (x : y : z) → (x/z
2
, y/z
3
)
The name: Jacobian
The curve equation: y^2 + xyz = x^3
z + ax2
z
2 + bz4
The relation to the affine: (x : y : z) → (x/z, y/z
2
)
The name: Lopez-Dahab
"""
class Point(object):
    __slots__ = ['x','y']
    def __init__(self,x,y):
        """

        :param x:
        :param y:
        """
        self.x = x
        self.y = y



    def __add__(self,):
        """

        :return:
        """
        return
    def __mul__(self):
        """

        :return:
        """
        return
    def __sub__(self):
        """

        :return:
        """
        return

class JacobianPoint(Point):
    class affinepoint:
        def __init__(self, x, y, infinity=0):
            self.x = x
            self.y = y
            self.infinity = infinity

        def __str__(self):
            return "affinepoint(x=%s,y=%s,inf=%s)" % (self.x, self.y, self.infinity)

    class JacobianPoint:
        def __init__(self, x, y, z, infinity=0):
            self.X = x
            self.Y = y
            self.Z = z
            self.Infinity = infinity

        def __str__(self):
            return "JacobianPoint(X=%s,Y=%s,Z=%s,inf=%s)" % (self.X, self.Y, self.Z, self.Infinity)

    def point_at_infinity():
        return JacobianPoint(1, 1, 1, 1)

    def negate(p):
        if p.__class__ == affinepoint:
            return affinepoint(p.x, -p.y)
        if p.__class__ == JacobianPoint:
            return JacobianPoint(p.X, -p.Y, p.Z)
        assert (False)

    def on_weierstrass_curve(A, B, p):
        """Return a set of zero-expressions for an affine point to be on the curve"""
        return constraints(zero={p.x ^ 3 + A * p.x + B - p.y ^ 2: 'on_curve'})

    def colinear(p1, p2, p3):
      """Return a set of zero-expressions for ((x1,y1),(x2,y2),(x3,y3)) to be collinear"""
      return constraints(zero={
        (p1.y - p2.y) * (p1.x - p3.x) - (p1.y - p3.y) * (p1.x - p2.x): 'colinear_1',
        (p2.y - p3.y) * (p2.x - p1.x) - (p2.y - p1.y) * (p2.x - p3.x): 'colinear_2',
        (p3.y - p1.y) * (p3.x - p2.x) - (p3.y - p2.y) * (p3.x - p1.x): 'colinear_3'
      })


    def good_affine_point(p):
      return constraints(nonzero={p.x : 'nonzero_x', p.y : 'nonzero_y'})


    def good_jacobian_point(p):
      return constraints(nonzero={p.X : 'nonzero_X', p.Y : 'nonzero_Y', p.Z^6 : 'nonzero_Z'})


    def good_point(p):
      return constraints(nonzero={p.Z^6 : 'nonzero_X'})


    def finite(p, *affine_fns):
      con = good_point(p) + constraints(zero={p.Infinity : 'finite_point'})
      if p.Z != 0:
        return con + reduce(lambda a, b: a + b, (f(affinepoint(p.X / p.Z^2, p.Y / p.Z^3)) for f in affine_fns), con)
      else:
        return con

    def infinite(p):
      return constraints(nonzero={p.Infinity : 'infinite_point'})
class AffineCoordinates(Point):
    pass

class ProjectiveCoordinate(Point):
    """
    Projective coordinates reduce the number of field inversions
    """
    pass

class ProjectiveHomogeneousPoint(Point):
    pass



class  JacobianProjectiveCoordinate(Point):
    """
    P = (x1 : y1 : z1)
    R = (x3 : y3 : z3)
    x3 = M2 − 2S
    y3 = M(S − x3) − 8T
    z3 = 2y1z1
    M = 3x^2 + az^4
    T = y^4
    S = 4x1y^2
    """
    @property
    def __getattribute__(self, item):
    def double(self, P):
        if type(P) == JacobianProjectiveCoordinate:

        else:
            raise Exception

class LopezDahabCoordinates(Point):
    """
    Y 2 + XYZ = X 3Z + aX 2Z 2 + bZ 4
    """
    __slots__ = []
    def __init__(self,x,y):
        #x = X / Z
        #y = Y / Z2