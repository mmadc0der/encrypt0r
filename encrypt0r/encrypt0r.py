import numpy as np
import generator
import p4rser

env = p4rser.secrets()


secret = generator.generate_secret()
print(secret['B'])
print(secret['U'], np.linalg.det(secret['U']))

key = generator.generate_key(secret)
print(key.dtype)

m = 'hello'
mb = np.array(list(m.encode()), dtype=int)
print(f'message  : {m} or {mb} in ancii')

c = np.dot(mb, key)

r = np.random.rand(env.ndim) - 0.5

c = c + r
print(f'encrypted: {c}')

m1 = np.dot(c, secret['BN'])

m2b = np.dot(m1, secret['UN'])
m2b = np.round(m2b).astype(int)

m2 = bytes(m2b.tolist()).decode()
print(f'decrypted: still {m2} or {m2b}')
