
def get(varname):
    try:
        inp = float(input(varname + ' = '))
        return inp
    except:
        return get(varname)


def get_params(lst):
	params = {}
	for p in lst:
		params[p] = get(p)
	print(params)
	return params

sci = lambda x: "{:.4e}".format(x)
def out(desc, val):
    if val > 9999 or val < 0.000999999:
        val = sci(val)
    else: val = "{:.5}".format(val)
    print(desc + ' = ' + val)

def choose_opt(descr, optmap):
    """Only lowcase letter in optmap !"""
    intmap = {i+1:opt for i, opt in enumerate(optmap)}
    opt_txt = ', '.join([e+':'+str(k) for k,e in intmap.items()])
    inp = input('Choose ' + descr + ' ' + opt_txt + ':')
    try:
        inp = int(inp)
        inp = intmap[inp]
    except:
        inp = inp.lower()
    return optmap[inp]()