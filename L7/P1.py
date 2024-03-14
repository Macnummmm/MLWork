import numpy as np

def fquad(x, w):
    return w[0] + w[1]*x + w[2]*x**2

def mse(Yp, Y):
    return np.mean((Yp - Y)**2)

if __name__ == "__main__":
    xs = np.array([-4., -2., 0., 2., 4., 6., 8.])
    ys = fquad(xs, [5, 1, 1.5])
    print(ys)

    xt = np.array([-4., -2., 0., 2., 4., 6., 8.])
    yt = np.array([33., 11., 5., 15., 41., 83., 141.])
    yp = fquad(xt, [5, 1, 1.5])
    print(mse(yp, yt))




    """
    Computes quadratic value w0 + w1*x + w2*x^2 given x value and polynomial coefficients.

    Parameters:
        x (numpy.ndarray): Input values.
        w (list): Polynomial coefficients [w0, w1, w2].

    Returns:
        numpy.ndarray: Quadratic values.
    """
    """
    Computes the Mean Squared Error (MSE) between predicted values and ground-truth.

    Parameters:
        Yp (numpy.ndarray): Predicted values.
        Y (numpy.ndarray): Ground-truth values.

    Returns:
        float: Mean squared error.
    """