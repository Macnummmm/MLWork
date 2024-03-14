import numpy as np
from matplotlib import pyplot as plt

class Sphere:
    
    def __init__(self, C, r, col=(128,128,128)):
        self.C = C
        self.r = r
        self.color = col
    
    def ray(self, O, V):
        # Define parameters for the quadratic equation
        a = np.dot(V - O, V - O)
        b = 2 * np.dot(O - self.C, V - O)
        c = np.dot(O - self.C, O - self.C) - self.r**2
        
        # Compute the discriminant
        discriminant = b**2 - 4 * a * c
        
        if discriminant < 0:
            # No real solutions, ray does not hit the sphere
            return np.inf
        elif discriminant == 0:
            # One solution, ray just touches the sphere
            return -b / (2 * a)
        else:
            # Two solutions, ray hits the sphere, return the smaller solution
            t1 = (-b - np.sqrt(discriminant)) / (2 * a)
            t2 = (-b + np.sqrt(discriminant)) / (2 * a)
            return min(t1, t2)


    def trace_ray(self, O, V, objs, tmin, tmax, BACKGROUND_COLOR=(0,0,0)):

        closest_t = np.inf
        closest_ob = None

        # Loop through all spheres
        for ob in objs:
            t = ob.ray(O, V)

            if (tmin <= t <= tmax) and (t < closest_t):
                closest_t = t
                closest_ob = ob

        if closest_ob is None:
            return BACKGROUND_COLOR

        return closest_ob.color


if __name__ == '__main__':

    s1 = Sphere(np.array((0, 0, 80)), 20, (220, 180, 40))
    s2 = Sphere(np.array((0, 150, 400)), 30, (240, 100, 100))
    s3 = Sphere(np.array((50, 100, 200)), 50, (80, 240, 80))
    s4 = Sphere(np.array((100, 50, 300)), 60, (80, 80, 200))
    Geos = [s1, s2, s3, s4]

    # Viewing
    O = np.array((0, 0, 0))

    VH, VW = 60, 80
    d = 50

    img = np.zeros((VH, VW, 3), dtype='uint8')

    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Before tracing')
    plt.axis('off')

    # Perform ray tracing

    for i in range(VH):
        for j in range(VW):
            V = np.array((i - VW/2, j - VH/2, d))

            col = Sphere.trace_ray(s1, O, V, Geos, 0, 1000)
            img[i, j, :] = col

    plt.subplot(1, 2, 2)
    plt.imshow(img)
    plt.title('After tracing')
    plt.axis('off')

    plt.show()
