import numpy as np
from matplotlib import pyplot as plt
# from P9 import Sphere
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


def trace_ray(O, V, objs, tmin, tmax, BACKGROUND_COLOR=(0,0,0)):

    closest_t = np.inf
    closest_ob = None

    # Loop through all spheres
    for ob in objs:
        t = ob.ray(O, V)

        # print('t =', t)

        if (tmin <= t <= tmax) and (t < closest_t):
            closest_t = t
            closest_ob = ob

    # end for ob

    if closest_ob == None:
        return BACKGROUND_COLOR

    return closest_ob.color


if __name__ == '__main__':

    # s1 = Sphere(np.array((0, 0, 80)), 20, (220, 180, 40))
    # s3 = Sphere(np.array((50, 100, 200)), 50, (80, 240, 80))
    f1 = Face(np.array((30, 40, 90)), 
            np.array((10, 10, 100)),
            np.array((50, 10, 200)),
            (80, 80, 200))

    f2 = Face(np.array((-40, -40, 90)), 
            np.array((0, 0, 90)),
            np.array((-40, 40, 200)),
            (240, 100, 100))

    f3 = Face(np.array((0, 20, 80)), 
            np.array((-20, -10, 80)),
            np.array((20, -10, 80)),
            (240, 200, 100))

    # Geos = [s1, s3, f1, f2]
    Geos = [f1, f2, f3]


    # Viewing
    O = np.array((0,0,0))

    VH, VW = 60, 80
    d = 50

    img = np.zeros( (VH, VW, 3), dtype='uint')

    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.title('Before tracing')
    plt.axis('off')

    # Perform ray tracing

    for i in range(VW):
        for j in range(VH):
            V = np.array((i - VW/2, j - VH/2, d))

            col = trace_ray(O, V, Geos, 0, 1000)
            # print('Color = ', col)

            img[j, i,:] = col

    plt.subplot(1,2,2)
    plt.imshow(img)
    plt.title('After tracing')
    plt.axis('off')

    plt.show()

