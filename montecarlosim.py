import random
import matplotlib.pyplot as plt

def monte_carlo_pi(num_points):
    inside_circle = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Berechne den Abstand zum Ursprung (0, 0)
        if x**2 + y**2 <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    # Schätze Pi
    estimated_pi = 4 * inside_circle / num_points

    # Visualisierung
    plt.figure(figsize=(6,6))
    plt.scatter(x_inside, y_inside, color='blue', s=1)
    plt.scatter(x_outside, y_outside, color='red', s=1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Monte Carlo Simulation: Schätzung für Pi = {estimated_pi}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    return estimated_pi

num_points = 100
estimated_pi = monte_carlo_pi(num_points)
print(f"Geschätzter Wert für Pi: {estimated_pi}")
