
from utility import *


def forced_ext_cylinder():
    pr('Churchill-Bernstein - Forced external convection around cyclinder')
    p = get_params(['Re_D', 'Pr'])

    num = .62 * p['Re_D'] ** .5 * p['Pr'] ** (1 / 3)
    den = (1 + (.4 / p['Pr']) ** (2 / 3)) ** (1 / 4)
    factor = (1 + (p['Re_D'] / 282000) ** (5 / 8)) ** (4 / 5)
    res = .3 + num / den * factor
    out('Nu_D', res)


def free_ext_vertical_local():
    pr('Laminar local value - Free external convection - Vertical plate')
    p = get_params(['Gr_x', 'Pr'])

    g = .75 * p['Pr'] ** .5 / (.609 + 1.221 * p['Pr'] ** .5 + 1.238 * p['Pr']) ** (1 / 4)
    Nu_x = (p['Gr_x'] / 4) ** (1 / 4) * g
    out('g(Pr)', g)
    out('Nu_x', Nu_x)


def free_ext_vertical_avg():
    pr('Average value (Churchill&Chu) - Free external convection - Vertical plate')
    p = get_params(['Ra_L', 'Pr'])

    num = 0.387 * p['Ra_L'] ** (1 / 6)
    den = (1 + (.492 / p['Pr']) ** (9 / 16)) ** (8 / 27)
    Nu_L = (0.825 + num / den) ** 2
    out('Nu_L', Nu_L)


def free_ext_infcylinder():
    pr('Infinite cyclinder - Free external convection (la&turb)')
    p = get_params(['Ra_D', 'Pr'])

    num = 0.387 * p['Ra_D'] ** (1 / 6)
    den = (1 + (.559 / p['Pr']) ** (9 / 16)) ** (8 / 27)
    Nu_D = (0.6 + num / den) ** 2
    out('Nu_D', Nu_D)


optmap = {'forced-ext-cyclinder': forced_ext_cylinder, 'free-ext-vert-local': free_ext_vertical_local,
          'free-ext-vert-avg': free_ext_vertical_avg, 'free-ext-infcyl': free_ext_infcylinder}

choose_opt('type', optmap)

