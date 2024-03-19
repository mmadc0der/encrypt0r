from random import randint
import numpy as np
import unimod
import p4rser
env = p4rser.secrets()

def key(secret: dict) -> np.ndarray: 
  return np.dot(secret['U'].astype(np.float64), secret['B'].astype(np.float64))
  
def secret() -> dict:
  secret = {}

  secret['B'] = np.random.randn(env.ndim, env.ndim)
  secret['B'][np.diag_indices_from(secret['B'])] = np.random.randn(env.ndim) * randint(40, 50)
  secret['BN'] = np.linalg.inv(secret['B'])
    
  secret['U'] = np.array(unimod.unimod(env.ndim)).astype(int)
  secret['UN'] = np.linalg.inv(secret['U'])
  
  return secret

def noize(mid: float = 0, div: float = 0.32) -> np.ndarray:
  return (np.random.rand(env.ndim) * 2 - 1) * div + mid