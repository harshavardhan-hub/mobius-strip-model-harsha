import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MobiusStrip:
    def __init__(self, R=1.0, w=0.3, n=100):
        self.R = R
        self.w = w
        self.n = n
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.X, self.Y, self.Z = self._generate_mesh()

    def _generate_mesh(self):
        U, V = self.U, self.V
        X = (self.R + V * np.cos(U / 2)) * np.cos(U)
        Y = (self.R + V * np.cos(U / 2)) * np.sin(U)
        Z = V * np.sin(U / 2)
        return X, Y, Z

    def surface_area(self):
        # Use finite difference approximation of area element
        du = 2 * np.pi / (self.n - 1)
        dv = self.w / (self.n - 1)

        # Partial derivatives
        Xu = np.gradient(self.X, axis=1) / du
        Yu = np.gradient(self.Y, axis=1) / du
        Zu = np.gradient(self.Z, axis=1) / du

        Xv = np.gradient(self.X, axis=0) / dv
        Yv = np.gradient(self.Y, axis=0) / dv
        Zv = np.gradient(self.Z, axis=0) / dv

        # Cross product of partial derivatives
        cross = np.cross(np.stack((Xu, Yu, Zu), axis=2),
                         np.stack((Xv, Yv, Zv), axis=2))

        dA = np.linalg.norm(cross, axis=2) * du * dv
        return np.sum(dA)

    def edge_length(self):
        # Calculate the edge curves: v = -w/2 and v = w/2
        edge1 = np.array([
            (self.R + (-self.w / 2) * np.cos(self.u / 2)) * np.cos(self.u),
            (self.R + (-self.w / 2) * np.cos(self.u / 2)) * np.sin(self.u),
            (-self.w / 2) * np.sin(self.u / 2)
        ])

        edge2 = np.array([
            (self.R + (self.w / 2) * np.cos(self.u / 2)) * np.cos(self.u),
            (self.R + (self.w / 2) * np.cos(self.u / 2)) * np.sin(self.u),
            (self.w / 2) * np.sin(self.u / 2)
        ])

        def compute_length(edge):
            dx = np.diff(edge[0])
            dy = np.diff(edge[1])
            dz = np.diff(edge[2])
            return np.sum(np.sqrt(dx**2 + dy**2 + dz**2))

        return compute_length(edge1) + compute_length(edge2)

    def plot(self):
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, cmap='viridis', edgecolor='k', linewidth=0.1)
        ax.set_title('Möbius Strip')
        plt.show()


if __name__ == "__main__":
    mobius = MobiusStrip(R=1.0, w=0.3, n=200)
    area = mobius.surface_area()
    length = mobius.edge_length()
    print(f"Estimated Surface Area: {area:.4f}")
    print(f"Estimated Edge Length: {length:.4f}")
    mobius.plot()
