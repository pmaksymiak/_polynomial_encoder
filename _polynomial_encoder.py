import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

def points_from_string(string):
    points = []
    for i, char in enumerate(string):
        points.append((i, ord(char), char))
    return points

def ascii_values(s):
    return [ord(c) for c in s]

def evaluate_poly_at_positions(p, positions):
    return [round(p(x)) for x in positions]

def ascii_values_to_string(values):
    return ''.join(chr(int(round(v))) for v in values)

def plot_lagrange_interpolation(points, ax):
    x, y = zip(*[(point[0], point[1]) for point in points])
    interpolator = lagrange(x, y)
    x_plot = np.linspace(min(x), max(x), 1000)
    y_plot = interpolator(x_plot)
    ax.plot(x_plot, y_plot, label='Interpolated polynomial')
    ax.scatter(x, y, color='red', label='Data points')
    
    formatted_poly = format_poly(interpolator)
    ax.set_title('Lagrange Interpolation for "{}"'.format(string), fontsize=10, y=1.1, pad=10)
    
    ax.set_xticks(x)
    ax.set_xticklabels(['{}\n{} ({})'.format(point[0], point[1], point[2]) for point in points])
    
    ax.legend()

    return interpolator, formatted_poly

def format_poly(p):
    terms = []
    for i, coef in enumerate(p.coefficients):
        power = len(p.coefficients) - i - 1
        if coef == 0:
            continue
        term = "{:.2f}x^{}".format(coef, power) if power > 1 else "{:.2f}x".format(coef) if power == 1 else "{:.2f}".format(coef)
        if coef > 0 and i > 0:
            term = "+ " + term
        terms.append(term)
    return ' '.join(terms)


string = "112W55-3"
points = list(enumerate(ascii_values(string)))

fig, ax = plt.subplots()
points = points_from_string(string)
interpolator, formatted_poly = plot_lagrange_interpolation(points, ax)
plt.xlabel('Position')
plt.ylabel('ASCII value')
plt.title('Lagrange Interpolation for "{}"'.format(string))
formatted_poly = format_poly(interpolator)
fig.suptitle('P(x) = {}'.format(formatted_poly), fontsize=10, y=0.98)
plt.show()

formatted_poly = format_poly(interpolator)
print("Lagrange interpolation formula:")
print("P(x) =", formatted_poly)

# Evaluate the polynomial at the positions of the characters in the original string
ascii_values_reconstructed = evaluate_poly_at_positions(interpolator, range(len(string)))

# Convert the ASCII values back to the original characters
string_reconstructed = ascii_values_to_string(ascii_values_reconstructed)
print("Reconstructed string:", string_reconstructed)
