"""Compute heat transfer rates and temperature distribution in fins."""


from utility import *
from math import *


def BC_convection():
    pr('Convection BC')
    p = ['x', 'L', 'm', 'h', 'k', 'M']
    p = get_params(p)
    h_mk = p['h'] / (p['m'] * p['k'])

    # theta / theta_b
    num = cosh(p['m'] * (p['L'] - p['x'])) + h_mk * sinh(p['m'] * (p['L'] - p['x']))
    den = cosh(p['m'] * p['L']) + h_mk * sinh(p['m'] * p['L'])
    out('theta/theta_b', num / den)

    # Qf
    num = sinh(p['m'] * p['L']) + h_mk * cosh(p['m'] * p['L'])
    den = cosh(p['m'] * p['L']) + h_mk * sinh(p['m'] * p['L'])
    coef = num / den
    out('All but M', coef)
    out('Qf', p['M'] * coef)


def BC_adia():
    pr('Adiabatic BC')
    p = get_params(['x', 'L', 'm', 'M'])

    out('theta/theta_b',
        cosh(p['m'] * (p['L'] - p['x'])) / cosh(p['m'] * p['L']))
    coef = tanh(p['m'] * p['L'])

    out('All but M', coef)
    out('Qf', p['M'] * coef)


def BC_temp():
    pr('Temperature BC')
    p = get_params(['x', 'L', 'm', 'M', 'theta_L', 'theta_b'])

    num = p['theta_L'] / p['theta_b'] * sinh(p['m'] * p['x'])
    num += sinh(p['m'] * (p['L'] - p['x']))
    den = sinh(p['m'] * p['L'])
    out("theta/theta_b", num / den)

    num = cosh(p['m'] * p['L']) - p['theta_L'] / p['theta_b']
    # same deno
    coef = num / den
    out("All but M", coef)
    out("Qf", p['M'] * coef)


opt = {'a': BC_convection, 'b': BC_adia, 'c': BC_temp}
choose_opt('boundary condition', opt)

