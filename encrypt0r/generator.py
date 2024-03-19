from random import randint

import numpy as np

import os.path
import unimod
import p4rser

env = p4rser.secrets()

def generate_key(secret: dict) -> np.ndarray: 
  return np.dot(secret['U'].astype(np.float64), secret['B'].astype(np.float64))
  
def generate_secret() -> dict:
  secret = {}

  secret['B'] = np.random.randn(env.ndim, env.ndim)
  secret['B'][np.diag_indices_from(secret['B'])] = np.random.randn(env.ndim) * randint(40, 50)
  secret['BN'] = np.linalg.inv(secret['B'])
    
  secret['U'] = np.array(unimod.unimod(env.ndim)).astype(int)
  secret['UN'] = np.linalg.inv(secret['U'])
  
  return secret