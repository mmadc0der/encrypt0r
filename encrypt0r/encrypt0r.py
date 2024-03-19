import numpy as np
import generate
import p4rser

env = p4rser.secrets()

if __name__ == '__main__':
  secret = generate.secret()
  key = generate.key(secret)
    
  while True:
    m = input('message  : ')                    # input
    m = np.array(list(m.encode()), dtype=int)
    print(f'sourse   : {m}')
    
    c = np.dot(m, key)                          # encrypt
    r = generate.noize()
    c = c + r
    print(f'noize    : {r}')
    print(f'encrypted: {c}')
    
    m = np.dot(c, secret['BN'])                 # decrypt
    m = np.dot(m, secret['UN'])
    m = np.round(m).astype(int)
    print(f'decrypted: {m} or {bytes(m.tolist()).decode()}', end='\n\n')