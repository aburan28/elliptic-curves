


def EEA():
    return

def fermat_method():
    return

def euler_phi():
    return
def eulers_method():
    return
def binary_exponentiation_method():
    return


def is_smooth(px, B):
    gx = px
    exponent_list = []
    for fx in B:
        exponent = 0
        while ((gx / fx) < (gx)):
            gx = gx / fx
            exponent = exponent + 1
        exponent_list = exponent_list + [exponent]
    if gx > 1:
        return False
    return exponent_list
def fermat(N):
n = ceil(sqrt(N))
while True:
M = n*n-N
m = floor(sqrt(M))
if m == sqrt(M):
return [n+m,n-m]
n = n+1



rithm.
def pollard rho(N):
n = floor(sqrt(sqrt(N))) # adjust this value
ai = randint(1,N-1)
a2i = ai
for k in range(1,n):
ai = (ai*ai + 1) % N
a2i = (a2i*a2i + 1) % N
a2i = (a2i*a2i + 1) % N
d = gcd(abs(ai-a2i),N)
if not (d in [1,N]):
return [d,floor(N/d)]
return ’fail’