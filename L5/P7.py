import numpy as np

def plane3d(X, Y, n, k):
    nx, ny, nz = n
    return (k - nx * X - ny * Y) / nz

if __name__ == "__main__":
    # Plane
    n = np.array([0.57735027, 0.57735027, 0.57735027])
    k = 3

    # Point on the plane
    x, y = 0, 0
    z = plane3d(x, y, n, k)
    print(f'p = ({x}, {y}, {z})')

    # Points on a plane
    xs = np.linspace(-2, 2, 3)
    ys = np.linspace(-2, 2, 3)
    X, Y = np.meshgrid(xs, ys)
    Z = plane3d(X, Y, n, k)
    for i in range(3):
        for j in range(3):
            print(f'ps = ({X[i,j]}, {Y[i,j]}, {Z[i,j]})')
#function computes the (z - coordinate of a point on the 3D plane) given its x and y - coordinate of point on the 3D plant, the normal vector be n,  and the distance k
#It uses the formula Z = (k-nx * X - ny * Y) /nz to calculate the z - coordinate
#In the main block, it demonstrates using the function to compute the z - coordinate of a single point (X = 0, Y = 0)  and multiple points(x and y values specified by a meshgrid)
