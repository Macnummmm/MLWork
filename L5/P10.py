import numpy as np

class Face:
    def __init__(self, A, B, C, col=(128, 128, 128)):
        self.A = A
        self.B = B
        self.C = C
        self.color = col
        
        # Step 1: Determine the normal vector
        AB = B - A
        AC = C - A
        self.normal = np.cross(AB, AC)
        self.normal = self.normal.astype(float) #The astype() method in NumPy is used to change the data type of an array. It creates a copy of the array with the specified data type. SUM chage numner of normalize from int ot float or can have point
        self.normal /= np.linalg.norm(self.normal)
        
    def ray(self, O, V):
        # Step 2: Formulate the plane equation
        k = np.dot(self.normal, self.A)
        
        # Step 3: Compute the parametric t for the intersection
        n_dot_v = np.dot(self.normal, V)
        if np.abs(n_dot_v) < 1e-6:  # Ray is parallel to the plane
            return np.inf
        
        t = (k - np.dot(self.normal, O)) / n_dot_v
        if t < 0:  # Intersection behind the origin
            return np.inf
        
        # Step 4: Determine if the intersection lies within the face boundaries
        Q = O + t * V
        
        # Test the boundaries
        if np.dot(np.cross(self.B - self.A, Q - self.A), self.normal) >= 0 and \
           np.dot(np.cross(self.C - self.B, Q - self.B), self.normal) >= 0 and \
           np.dot(np.cross(self.A - self.C, Q - self.C), self.normal) >= 0:
            return t
        else:
            return np.inf

if __name__ == '__main__':
    f1 = Face(np.array((0, 20, 80)),
              np.array((-20, -10, 80)),
              np.array((20, -10, 80)),
              (240, 200, 100))
    
    O = np.array((0, 0, 0))
    V1 = np.array((-40, 0, 50))
    t = f1.ray(O, V1)
    print('t = {:.3f}'.format(t))
    
    V2 = np.array((0, 0, 50))
    t = f1.ray(O, V2)
    print('t = {:.3f}'.format(t))
