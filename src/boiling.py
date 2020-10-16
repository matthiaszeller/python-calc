
from utility import *
from math import pi


def forced_ext_cyl():
    pr('Forced convection boiling - External - Cylinder')
    p = get_params(['rho_l', 'rho_v', 'We_D'])
    rho_ratio = p['rho_l'] / p['rho_v']

    low_velocity = (1 + (4 / p['We_D']) ** (1 / 3)) / pi
    out('low-v right-hand side', low_velocity)
    high_velocity = rho_ratio ** (3 / 4) / (169 * pi)
    high_velocity += rho_ratio ** 0.5 / (19.2 * pi * p['We_D'] ** (1 / 3))
    out('high-v right-hand side', high_velocity)

    discriminant = 1 + 0.275 / pi * (rho_ratio) ** 0.5
    out('discriminant', discriminant)

    if low_velocity > discriminant:
        pr('=> Low velocity')
    else:
        pr('=> High velocity')


optmap = {'forced-ext-cyl': forced_ext_cyl}
choose_opt('type', optmap)