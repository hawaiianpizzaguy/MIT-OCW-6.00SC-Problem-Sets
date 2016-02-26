# 6.00 Problem Set 2
#
# Successive Approximation
#
# Name          : Connor Wyandt
# Collaborators : <your collaborators>
# Time spent    : 0:45
#

def evaluate_poly(poly, x):

    total = 0.0
    for i in xrange(len(poly)):
        total += poly[i] * (x ** i)
    return total

def compute_deriv(poly):

    poly_deriv = []
    if len(poly) < 2:
        return [0.0]
    for j in xrange(1, len(poly)):
        poly_deriv.append(float(j * poly[j]))
    return poly_deriv

def compute_root(poly, x_0, epsilon):

    root = x_0
    counter = 1.0
    while abs(evaluate_poly(poly, root)) >= epsilon:
        root = (root - evaluate_poly(poly, root) / evaluate_poly(compute_deriv(poly), root))
        counter += 1
    return [root, counter]
