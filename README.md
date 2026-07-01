# Biophysics EM Toys

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HyeonjeYang/electripyyy_lab/blob/main/biophysics_em_toys.ipynb)

This repository contains one self-contained Jupyter notebook for Lecture 5 of a graduate biophysics course: electric fields, charged particles, and electromagnetic measurements in biology. The goal is not to build a production solver, but to make the lecture equations visible and modifiable through compact NumPy simulations that run in Google Colab or local Jupyter.

## Notebook Map

| Notebook section | Lecture slides | Governing equation or model |
| --- | --- | --- |
| Fields & potential | 2-4 | Coulomb potential, `E = -grad(phi)` |
| Poisson & Laplace | 5-7 | `nabla^2 phi = -rho / eps`, `nabla^2 phi = 0` |
| Gel electrophoresis | 6 | `nabla^2 phi = 0`, `v = mu_ep E` |
| Charge relaxation | 8 | `d rho / dt = -(sigma / eps) rho`, `tau = eps / sigma` |
| Why EQS is reasonable | 5 | `tau_e = eps / sigma`, `tau_m = mu sigma L^2`, `tau_em = L / c` |
| Nernst-Planck migration | 10-11 | `J = -D dc/dx - z F D c grad(phi)/(R T)` |
| Poisson-Boltzmann & Debye length | 12-13 | `d^2 phi/dx^2 = kappa^2 phi`, `lam_D = 1 / kappa` |
| Virus as a charged sphere | 14-16 | Spherical linearized PB, drift-diffusion transport |
| Donnan equilibrium | 17 | Electroneutral Donnan partition with fixed charge |
| Lorentz & Hall | 18-19 | `F = q(E + v x B)`, `E_H = J_x B_z / (n q)` |
| EM wave in 1D | 20 | Yee FDTD, `v = 1 / sqrt(mu eps)`, `n = c / v` |
| Wave optics & diffraction | 21 | Fraunhofer FFT, `d sin(theta) = m lambda`, Rayleigh and Abbe limits |

## Local Setup

```bash
pip install -r requirements.txt
jupyter lab
```

Open `biophysics_em_toys.ipynb` and run cells from top to bottom. The first setup cell also installs the same minimal dependencies in Colab.

## Pedagogical Notes

All simulations are finite-difference or FFT toys written directly with NumPy, SciPy, Matplotlib, and ipywidgets. They are intentionally small, deterministic, and readable so students can change parameters during lecture. The grids are coarse, boundary conditions are simplified, and the numerical schemes are chosen for clarity rather than benchmark accuracy; use specialized PDE or electromagnetics packages for research-grade modeling.
