"""Compact finite-difference helpers for electrostatic toy problems."""

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as spla

from .constants import eps0


def laplacian_1d(n, dx):
    main = -2 * np.ones(n)
    off = np.ones(n - 1)
    return sparse.diags([off, main, off], [-1, 0, 1], format="csr") / dx**2


def laplacian_2d(nx, ny, dx, dy=None):
    dy = dx if dy is None else dy
    lx = laplacian_1d(nx, dx)
    ly = laplacian_1d(ny, dy)
    return sparse.kron(sparse.eye(ny), lx) + sparse.kron(ly, sparse.eye(nx))


def solve_poisson_1d(rho, dx, eps=eps0, phi_left=0.0, phi_right=0.0):
    rho = np.asarray(rho, dtype=float)
    b = -rho / eps
    b[0] -= phi_left / dx**2
    b[-1] -= phi_right / dx**2
    return spla.spsolve(laplacian_1d(rho.size, dx), b)


def apply_dirichlet_bc(phi, bc):
    if not bc:
        return phi
    if "left" in bc:
        phi[:, 0] = bc["left"]
    if "right" in bc:
        phi[:, -1] = bc["right"]
    if "bottom" in bc:
        phi[0, :] = bc["bottom"]
    if "top" in bc:
        phi[-1, :] = bc["top"]
    return phi


def sor_poisson_2d(rho, dx, dy=None, eps=eps0, bc=None, omega=1.7, tol=1e-5, max_iter=6000):
    dy = dx if dy is None else dy
    rho = np.asarray(rho, dtype=float)
    phi = np.zeros_like(rho)
    apply_dirichlet_bc(phi, bc)
    idx2, idy2 = 1 / dx**2, 1 / dy**2
    denom = 2 * (idx2 + idy2)
    ny, nx = rho.shape
    jj, ii = np.indices((ny - 2, nx - 2))
    masks = ((ii + jj) % 2 == 0, (ii + jj) % 2 == 1)
    for it in range(max_iter):
        max_update = 0.0
        for mask in masks:
            proposal = (
                (phi[1:-1, 2:] + phi[1:-1, :-2]) * idx2
                + (phi[2:, 1:-1] + phi[:-2, 1:-1]) * idy2
                + rho[1:-1, 1:-1] / eps
            ) / denom
            interior = phi[1:-1, 1:-1]
            updated = (1 - omega) * interior + omega * proposal
            max_update = max(max_update, np.max(np.abs(updated[mask] - interior[mask])))
            interior[mask] = updated[mask]
        apply_dirichlet_bc(phi, bc)
        if max_update < tol:
            break
    return phi, it + 1


def electric_field(phi, dx, dy=None):
    dy = dx if dy is None else dy
    dphi_dy, dphi_dx = np.gradient(phi, dy, dx)
    return -dphi_dx, -dphi_dy


def coulomb_phi_grid(x, y, charges, eps=eps0, softening=1e-9):
    phi = np.zeros_like(x, dtype=float)
    for q, x0, y0 in charges:
        r = np.sqrt((x - x0) ** 2 + (y - y0) ** 2 + softening**2)
        phi += q / (4 * np.pi * eps * r)
    return phi
