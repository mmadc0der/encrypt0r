import numpy as np
import os.path
import p4rser

env = p4rser.secrets()

class certificate:
  def __init__(self, path: str):
    self.__k_ext = env.key_extention
    self.__s_ext = env.secret_extention
    
    self.key
    self.secret
  
  def __is_exist(self, name: str, path: str = './') -> bool:
    fpk = path + name + self.__k_ext
    fps = path + name + self.__s_ext
    if os.path.exists(fpk) and os.path.exists(fps):
      return os.path.isfile(fpk) and os.path.isfile(fps)
    else: return False
    
  def __to_bytes(self): pass