def simple_poet(p):
  
    f = open(p, "r")
    data = f.read()
  
    a = data.splitlines()

    return a
    
if __name__ == '__main__':
    res = simple_poet('poem.txt')
    print(res)