# pB11FusionSim

A simple Python package for modeling p-B11 aneutronic fusion physics, focusing on bremsstrahlung losses and direct alpha energy capture.

## Installation
```bash
pip install git+https://github.com/duraymontague/pB11FusionSim.git

from pB11fusion.core import loss_fraction
print(loss_fraction(1e20, 1e20, 1e5))  # Example at 100 keV

3. **Commit it**:
   - Scroll to the bottom of the editor.
   - Add a commit message: "Add complete README with installation, usage, and motivation".
   - Click "Commit changes".

### What Each Section Does
- **Title & Description**: Tells people what the package is at a glance.
- **Installation**: Makes it easy for others to install (using your repo URL).
- **Usage**: Shows a quick example so anyone can test it immediately.
- **Motivation**: Explains why you built it (ties back to Type 2 Energy) — this is where you subtly mention the company without it feeling salesy. It's perfect for networking and credibility.

### Next Steps (After Committing README)
1. **Create the other files**:
   - `setup.py` (paste the code from earlier)
   - `requirements.txt` (just `numpy`)
   - `pB11fusion/__init__.py` (empty file — just create it)
   - `pB11fusion/core.py` (paste the core functions)
   - `examples/basic_sim.py` (paste the example script)

Commit each one (or add multiple at once if GitHub lets you).

2. **Test locally** (optional but recommended):
   - Clone the repo: `git clone https://github.com/duraymontague/pB11FusionSim.git`
   - `cd pB11FusionSim`
   - `pip install -e .`
   - `python examples/basic_sim.py` (should print a loss fraction value)


