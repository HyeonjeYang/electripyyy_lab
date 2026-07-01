# Security Audit

Date: 2026-07-02

Scope: `biophysics_em_toys.ipynb`, `src/`, `README.md`, `pyproject.toml`, and `dist/`.

Checks performed:

- Secret scan: no API keys, tokens, passwords, or private-key markers found.
- Dangerous-call scan: no `subprocess`, `os.system`, `eval`, `exec`, `pickle`, `requests`, `urllib`, socket use, or recursive-delete calls found in notebook/source files.
- Dependency check: only `numpy`, `scipy`, `matplotlib`, `ipywidgets`, and `IPython` are imported by the notebook/source files.
- Notebook isolation: the notebook does not import `src` or `emtoys`; it remains self-contained for Colab.
- Distribution integrity: `dist/SHA256SUMS.txt` records the SHA-256 checksum for the release zip.
