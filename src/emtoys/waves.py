"""Minimal 1D electromagnetic wave helper."""

from .constants import eps0, mu0


def fdtd_1d_step(e_field, h_field, eps_r, dx, dt):
    h_field += dt / (mu0 * dx) * (e_field[1:] - e_field[:-1])
    e_field[1:-1] += dt / (eps0 * eps_r[1:-1] * dx) * (h_field[1:] - h_field[:-1])
    e_field[0], e_field[-1] = e_field[1], e_field[-2]
    return e_field, h_field
