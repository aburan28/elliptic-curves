



p = 115792089210356248762697446949407573530086143415290314195533631308867097853951


b=0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
b2=41058363725152142129326129780047268409114441015993725554835256314039467401291
G=0x026b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c29
G=0x046b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c2964fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5

p=0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF
a=-3
b=0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B
Gx=0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296
Gy=0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5
n=0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551


p 2**192 2 64 1, p 2 224 2 96 1, p 2 256 2 224 2 192 2 96 1, p 2 384 2 128
2 96 2 32 1, and p 2 521 1


p192 = pow(2,192)-pow(2,64)-1
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
x = 55066263022277343669578718895168534326250603453777594175500187360389116729240
ysquared = ((x*x*x+7) % p)
print "ysquared= %s " % ysquared
y = pow(ysquared, (p+1)/4, p)
print "y1 = %s " % y
print "y2 = %s " % (y * -1 % p)

The
following
procedure is used
to
generate
the
parameters
A and B
of
a
suitable
elliptic
curve
over
GF(p) and a
base
point
G
from a prime

p
of
bit
length
L and a
160 - bit
seed
s.
1.
Set
h = find_integer_2(s).
2.
Convert
h
to
an
integer
A.
3.
If - 3 = A * Z ^ 4
mod
p is not solvable, then
set
s = update_seed(s)
and go
to
Step
1.
4.
Compute
one
solution
Z
of - 3 = A * Z ^ 4
mod
p.
5.
Set
s = update_seed(s).
6.
Set
B = find_integer_2(s).
7.
If
B is a
square
mod
p, then
set
s = update_seed(s) and go
to
Step
6.
8.
If
4 * A ^ 3 + 27 * B ^ 2 = 0
mod
p, then
set
s = update_seed(s) and go
to
Step
1.
9.
Check
that
the
elliptic
curve
E
over
GF(p)
given
by
y ^ 2 = x ^ 3 +
A * x + B
fulfills
all
security and functional
requirements
given
in Section
3.
If
not, then
set
s = update_seed(s) and go
to
Step
1.
10.
Set
s = update_seed(s).
11.
Set
k = find_integer_2(s).
12.
Determine
the
points
Q and -Q
having
the
smallest
x - coordinate in
E(GF(p)).Randomly
select
one
of
them as point
P.