import numpy as np
import p4rser
env = p4rser.secrets()

B = np.array([[1, 45],     # private basis
              [45, -1]])
BN = np.linalg.inv(B)      # B inv

U = np.array([[1, 5],
              [8, 41]])    # unimodular matrix to encrypt
UN = np.linalg.inv(U)      # U inv

B1 = np.dot(U, B)          # B` or public basis

m = np.array([68, 69])     # message to encrypt
print(f'message  : hi or {m} in ancii')

c = np.dot(m, B1)          # encrypted nmessage without noize
print(f'encrypted: {c}')

r = np.array([1, -0.1])    # noize

c = c + r                  # noize addition

m1 = np.dot(c, BN)         # decrypted message

m2 = np.dot(m1, UN)        # reconstructed message
m2 = np.round(m2).astype(int)

print(f'decrypted: still hi or {m2}')
