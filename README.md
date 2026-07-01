# Introduction to Biophysics EM Toys

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HyeonjeYang/electripyyy_lab/blob/main/biophysics_em_toys.ipynb)

서울대학교 생물물리학입문_5차시: 생물전자기학 - 생체분자의 전기적 성질과 기초 전자기학
강의에 사용될 교육용 시뮬레이션 자료입니다.

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
