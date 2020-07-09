def interp(T, T1, T2, v1, v2):
    coef = (v2-v1)/(T2-T1)
    return coef * (T - T1) + v1

def separate():
  print('\n' + '=' * 29 + '\n')

def pr(msg, maxlen=29):
  """Fit msg in the screen"""
  if type(msg) != str:
    msg = str(msg)
  
  if len(msg) <= maxlen:
    print(msg)
    return
  
  i = msg.find(" ")
  lasti = -1
  while i != -1:
    if i >= maxlen:
      if lasti == -1:
        break
      print(msg[:lasti])
      pr(msg[lasti+1:], maxlen)
      break
    #
    lasti = i
    i = msg.find(" ", i+1)
  # Couldn't split 
  if lasti == -1:
    print(msg)
  elif i == -1:
    print(msg[:lasti])
    print(msg[lasti+1:])
    
def get(varname):
    try:
        inp = float(input(varname + ' = '))
        return inp
    except KeyboardInterrupt:
        return
    except Exception as e:
        print(e)
        return get(varname)


def get_params(lst):
  params = {}
  for p in lst:
    params[p] = get(p)
  pr(params)
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
    #opt_txt = ', '.join([str(k)+': '+e for k,e in intmap.items()])
    pr('Choose ' + descr + ': ')
    pr(intmap)
    inp = input('> ')
    try:
        inp = int(inp)
        inp = intmap[inp]
    except:
        inp = inp.lower()
    separate()
    return optmap[inp]()
