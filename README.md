# Biophysics EM Toys

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HyeonjeYang/electripyyy_lab/blob/main/biophysics_em_toys.ipynb)

One self-contained Jupyter notebook for a graduate biophysics lecture on electric fields, charged particles, and electromagnetic measurements in biology. No external EM repositories are imported; all reusable code lives in the notebook setup cell.

## Sections

| Section | Core model |
| --- | --- |
| Fields, Poisson/Laplace, gels, relaxation, EQS | Coulomb, `E=-grad(phi)`, `nabla^2 phi`, `tau=eps/sigma` |
| Ions, Debye screening, viruses, Donnan | Nernst-Planck, Poisson-Boltzmann, drift-diffusion, partitioning |
| Lorentz/Hall, 1D EM waves, diffraction | `q(E+v x B)`, FDTD, Fraunhofer FFT |

## Local

```bash
pip install -r requirements.txt
jupyter lab
```

Open `biophysics_em_toys.ipynb` and run top to bottom. These are finite-difference/FFT teaching toys, not solver benchmarks.
