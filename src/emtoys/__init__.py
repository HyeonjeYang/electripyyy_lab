"""Reusable helper mirror for the Biophysics EM Toys notebook.

The notebook remains self-contained for Colab. This package is a convenience
mirror for local reuse and review.
"""

from .constants import F, R, T, c, e, eps0, kB, mu0
from .finite_difference import (
    apply_dirichlet_bc,
    coulomb_phi_grid,
    electric_field,
    laplacian_1d,
    laplacian_2d,
    solve_poisson_1d,
    sor_poisson_2d,
)
from .optics import airy_intensity, fraunhofer_1d
from .transport import crank_nicolson_step, debye_length, gaussian
from .waves import fdtd_1d_step

__all__ = [
    "F",
    "R",
    "T",
    "apply_dirichlet_bc",
    "airy_intensity",
    "c",
    "coulomb_phi_grid",
    "crank_nicolson_step",
    "debye_length",
    "e",
    "electric_field",
    "eps0",
    "fdtd_1d_step",
    "fraunhofer_1d",
    "gaussian",
    "kB",
    "laplacian_1d",
    "laplacian_2d",
    "mu0",
    "solve_poisson_1d",
    "sor_poisson_2d",
]
