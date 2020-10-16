

def interp(T, T1, T2, v1, v2):
    coef = (v2-v1)/(T2-T1)
    return coef * (T - T1) + v1


getfloat = lambda msg: float(input(msg))
T1 = getfloat('Temp 1:')
T2 = getfloat('Temp 2:')
T = getfloat('Temp interp:')

while True:
    v1 = getfloat('v1:')
    v2 = getfloat('v2:')
    print(interp(T, T1, T2, v1, v2))

