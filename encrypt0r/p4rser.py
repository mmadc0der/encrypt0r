import ast

class secrets:
  def __init__(self):
    secrets = {}
    
    with open('.env') as e:
      for line in e:
        if '=' not in line or line.startswith("#"): continue
        prsd = line.split('=')
        name, value = prsd[0], '='.join(prsd[1:])
        name = name.lower()
        value = value[:-1]
        if value.isnumeric(): value = ast.literal_eval(value)
        self.__dict__[name] = value