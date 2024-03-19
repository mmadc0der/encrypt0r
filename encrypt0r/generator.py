from sympy import Rational, eye, Matrix
from sympy.ntheory.continued_fraction \
  import continued_fraction_convergents, continued_fraction_iterator, continued_fraction
from random import randint

def unimod(ndim):
  r = Rational(randint(1, 256), randint(1, 128))
  cfr = continued_fraction(r)
  Mlst = [eye(ndim) for k in range(len(cfr))]
  for k, m in enumerate(cfr):
    i, j = randint(0, ndim - 1), randint(0, ndim - 1)
    if i != j: Mlst[k][i, j] = -m
    else: Mlst[k][0, 1] = -m
  alpha = eye(ndim)
  for M in Mlst[::-1]: alpha *= M
  return alpha.tolist()