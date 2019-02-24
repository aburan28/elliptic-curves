#!/usr/bin/env python

class Curve:


class EllipticCurve(object):

    def __init__(self, a1,a2,a3,a4,a5,a6):

#        y^2 + xy = x3 + 1 or y2 + xy = x3 + x2 + 1









"""
Genus-1 curves over large-characteristic fields

Doubling-oriented Doche–Icart–Kohel curves: y2=x3+a*x2+16*a*x
Tripling-oriented Doche–Icart–Kohel curves: y2=x3+3*a*(x+1)2
Edwards curves: x2+y2=c2*(1+d*x2*y2)
Hessian curves: x3+y3+1=3*d*x*y
Jacobi intersections: s2+c2=1, a*s2+d2=1
Jacobi quartics: y2=x4+2*a*x2+1
Montgomery curves: b*y2=x3+a*x2+x
Short Weierstrass curves: y2=x3+a*x+b
Twisted Edwards curves: a*x2+y2=1+d*x2*y2
Twisted Hessian curves: a*x3+y3+1=d*x*y

Ordinary genus-1 curves over binary fields
Binary Edwards curves: d1*(x+y)+d2*(x2+y2)=(x+x2)*(y+y2)
Hessian curves: x3+y3+1=3*d*x*y
Short Weierstrass curves: y2+x*y=x3+a2*x2+a6
"""

#SmallWeierstrassCurveFp
y ** 2 == x ** 3 + a * x + b
#KoblitzCurveFp
y ** 2 == x ** 3 + b
#TwistedEdwardsCurveFp
a * x ** 2 + y ** 2 == 1 + d * x ** 2 * y ** 2
#EdwardsCurveFp
x ** 2 + y ** 2 == c * (1 + d * x ** 2 * y ** 2)
#MontgomeryCurveFp
y ** 2 == x ** 3 + a * x ** 2 + x

#Twisted Hessian curves
ax**3 + y**3 + 1 = dxy