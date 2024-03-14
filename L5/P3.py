import numpy as np

def normalize(v):
    norm = np.linalg.norm(v) # norm_squared = np.sum(v**2)
    if norm == 0: # if norm_squared == 0 
        return v # return v
    return v / norm # return v / np.sqrt(norm_squared)

if __name__ == '__main__':
    v = np.array([3, 4])
    u = normalize(v)
    print('u =', u)
    print('u.T @ v =', u.T @ v)
    print('size u=', np.sqrt(u[0]**2 + u[1]**2))
    v = np.array([3, 4, 2])
    u = normalize(v)
    print('u =', u)
    print('u.T @ v =', u.T @ v)
    print('size u=', np.sqrt(u[0]**2 + u[1]**2 + u[2]**2))
    v = np.array([3, 4, 2, 5])
    u = normalize(v)
    print('u =', u)
    print('u.T @ v =', u.T @ v)
    print('size u=', np.sqrt(u[0]**2 + u[1]**2 + u[2]**2 + u[3]**2))