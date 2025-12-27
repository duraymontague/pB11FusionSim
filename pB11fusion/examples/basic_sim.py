from pB11fusion.core import loss_fraction

n_e = 1e20  # m^-3
n_i = 1e20  # m^-3
T_e_ev = 1e5  # 100 keV example

print(f"Loss fraction at {T_e_ev/1000} keV: {loss_fraction(n_e, n_i, T_e_ev):.3f}")
 
