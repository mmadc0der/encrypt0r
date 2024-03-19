import numpy as np
from random import randint
from scipy.ndimage import  rotate
import p4rser
import generator
env = p4rser.secrets()


B = np.random.randn(env.ndim, env.ndim)
B[np.diag_indices_from(B)] = np.random.randn(env.ndim) * randint(40, 50)
BN = np.linalg.inv(B)
print(B)

U = np.array(generator.unimod(env.ndim)).astype(int)
print(U, np.linalg.det(U))
UN = np.linalg.inv(U)

B1 = np.dot(U.astype(np.float64), B.astype(np.float64))
print(B1.dtype)

m = 'hello'
mb = np.array(list(m.encode()), dtype=int)
print(f'message  : {m} or {mb} in ancii')

c = np.dot(mb, B1)

r = np.random.rand(env.ndim) - 0.5

c = c + r
print(f'encrypted: {c}')

m1 = np.dot(c, BN)

m2b = np.dot(m1, UN)
m2b = np.round(m2b).astype(int)

m2 = bytes(m2b.tolist()).decode()
print(f'decrypted: still {m2} or {m2b}')
