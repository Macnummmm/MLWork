import numpy as np

def innerprod(x, y):
    return np.sum(x.conj() * y)

if __name__ == '__main__':
    v = np.array([3, 4, 5, 6])
    u = np.array([1, -1, 0, 2.5])
    p = innerprod(v, u)
    print('<v|u> =', p)
    p = innerprod(u, v)
    print('<u|v> =', p)
    
    v = np.array([3 + 5j, -4j, 0, 1 - 1j, 6 + 9j])
    u = np.array([2 - 1j, -1.2, 7 + 8j, 3 - 5j, 1.1 + 2j])
    p = innerprod(v, u)
    print('<v|u> =', p)
    p = innerprod(u, v)
    print('<u|v> =', p)

#The innerprod function takes two numpy arrays x and y as arguments.
#It computes the inner product using the formula provided: ALL x(i) * y(i) where is x(i)* omplex conjugate of the number of "i" element of x and y(i) element of y
#x.conj() returns the complex conjugate of the array x 
#np.sum(x.conj() * y) computes the sum of the element-wise product of the complex conjugate of x and y This gives us the inner product.
