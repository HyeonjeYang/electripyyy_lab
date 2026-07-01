"""Transport and electrolyte helpers for teaching-scale simulations."""

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as spla

from .constants import F, R, T, eps0


def gaussian(x, center, width, area=1.0):
    y = np.exp(-0.5 * ((x - center) / width) ** 2)
    return area * y / np.trapz(y, x)


def crank_nicolson_step(u, d_coeff, velocity, dx, dt):
    u = np.asarray(u, dtype=float)
    n = u.size
    main = -2 * d_coeff / dx**2 * np.ones(n)
    lower = (d_coeff / dx**2 + velocity / (2 * dx)) * np.ones(n - 1)
    upper = (d_coeff / dx**2 - velocity / (2 * dx)) * np.ones(n - 1)
    op = sparse.diags([lower, main, upper], [-1, 0, 1], format="csr")
    ident = sparse.eye(n, format="csr")
    return spla.spsolve(ident - 0.5 * dt * op, (ident + 0.5 * dt * op) @ u)


def debye_length(ionic_strength_mM, eps_r=78.5):
    ionic_strength_molm3 = np.asarray(ionic_strength_mM, dtype=float)
    return np.sqrt(eps_r * eps0 * R * T / (2 * F**2 * ionic_strength_molm3))
