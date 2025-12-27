import numpy as np
from scipy.constants import e, k as k_B, epsilon_0

def bremsstrahlung_power(n_e, n_i, T_e_ev, Z_eff=5, volume=1.0):
    """
    Calculate bremsstrahlung power loss in p-B11 plasma (W).
    n_e, n_i: densities (m^-3)
    T_e_ev: electron temperature (eV)
    Z_eff: effective ion charge (5 for B11)
    volume: plasma volume (m^3)
    """
    T_e_keV = T_e_ev / 1000.0
    g_ff = 1.2  # Approximation
    P_brem = 1.69e-38 * Z_eff**2 * n_e * n_i * np.sqrt(T_e_keV) * g_ff * volume
    return P_brem

def alpha_energy_capture(e_alpha=3.76e6, grid_efficiency=0.7):
    """
    Estimate captured energy from alpha particles (J per fusion reaction).
    e_alpha: alpha energy (eV) for p-B11 -> 3.76 MeV per alpha
    grid_efficiency: fraction captured (0-1)
    """
    e_alpha_j = e_alpha * e  # Convert to Joules
    return e_alpha_j * grid_efficiency

def loss_fraction(n_e, n_i, T_e_ev, volume=1.0):
    """
    Rough fraction of fusion power lost to bremsstrahlung.
    Assumes 2 alphas per p-B11 reaction (total fusion energy ~8.7 MeV).
    """
    P_brem = bremsstrahlung_power(n_e, n_i, T_e_ev, volume=volume)
    P_fusion = 2 * alpha_energy_capture(e_alpha=3.76e6, grid_efficiency=1.0) * n_i * volume
    return P_brem / P_fusion if P_fusion > 0 else 0
