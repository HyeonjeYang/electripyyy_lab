"""Fraunhofer diffraction helpers."""

import numpy as np
from scipy.special import j1


def fraunhofer_1d(aperture, dx, wavelength):
    fft = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(aperture)))
    sin_theta = np.fft.fftshift(np.fft.fftfreq(aperture.size, d=dx)) * wavelength
    intensity = np.abs(fft) ** 2
    return sin_theta, intensity / intensity.max()


def airy_intensity(theta, wavelength, diameter):
    arg = np.pi * diameter * np.sin(theta) / wavelength
    out = np.ones_like(arg, dtype=float)
    mask = arg != 0
    out[mask] = (2 * j1(arg[mask]) / arg[mask]) ** 2
    return out
