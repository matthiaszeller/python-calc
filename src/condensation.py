
from utility import *


def Re_delta():
    pr('Special Reynolds number for condensation (avg values)')
    p = get_params(['k_l', 'L', 'mu_l', "h'_fg", 'nu_l', 'g', 'Pr_l', 'deltaT'])
    common = p['k_l'] * p['L'] * p['deltaT']
    common /= (p['mu_l'] * p["h'_fg"] * (p['nu_l'] ** 2 / p['g']) ** (1 / 3))

    res = 3.78 * common ** (3 / 4)
    out('Laminar', res)

    res = (3.7 * common + 4.8) ** 0.82
    out('Wavy', res)

    res = (0.069 * common * p['Pr_l'] ** 0.5 - 151 * p['Pr_l'] ** 0.5 + 253) ** (4 / 3)
    out('Turbulent', res)


optmap = {"vertplate-Re-delta": Re_delta}
choose_opt('type', optmap)

