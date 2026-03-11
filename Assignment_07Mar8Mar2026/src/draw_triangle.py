import matplotlib.pyplot as plt
import math

def draw_triangle(AB, BC, AC, label_A='A', label_B='B', label_C='C'):
    # --- Compute vertex coordinates ---
    A = (0, 0)
    B = (AB, 0)

    # Law of cosines to find angle at A
    cos_A = (AB**2 + AC**2 - BC**2) / (2 * AB * AC)
    angle_A = math.acos(cos_A)

    C = (AC * math.cos(angle_A), AC * math.sin(angle_A))

    # --- Plot triangle ---
    x = [A[0], B[0], C[0], A[0]]
    y = [A[1], B[1], C[1], A[1]]

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, 'b-', linewidth=2)
    plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='red')

    # --- Label vertices ---
    plt.text(A[0] - 0.2, A[1] - 0.2, label_A, fontsize=12, color='darkred')
    plt.text(B[0] + 0.1, B[1] - 0.2, label_B, fontsize=12, color='darkred')
    plt.text(C[0] + 0.1, C[1] + 0.1, label_C, fontsize=12, color='darkred')

    # --- Label side lengths at midpoints ---
    def midpoint(p1, p2):
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

    mid_AB = midpoint(A, B)
    mid_BC = midpoint(B, C)
    mid_AC = midpoint(A, C)

    plt.text(mid_AB[0], mid_AB[1] - 0.2, f"{AB:.2f}", fontsize=10, color='green')
    plt.text(mid_BC[0] + 0.1, mid_BC[1], f"{BC:.2f}", fontsize=10, color='green')
    plt.text(mid_AC[0] - 0.3, mid_AC[1] + 0.1, f"{AC:.2f}", fontsize=10, color='green')

    plt.axis('equal')
    plt.grid(True)
    plt.show()


# Example usage
#raw_triangle(1.1, .6, .7, label_A='Hello', label_B='How are you doing??', label_C='The world is a beautiful place')
