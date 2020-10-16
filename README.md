# python-calc

Implementation of Physics formulas and user interface for [NumWorks calculator](https://www.numworks.com/).

This project was motivated by the need to quickly perform redundant calculations
of Heat and Mass transfer problems when solving them with paper, a pen and a calculator.
In particular, the background theory is based on EPFL course [ME-341](https://edu.epfl.ch/coursebook/en/heat-and-mass-transfer-ME-341).
For theoretical details, refer to *Fundamentals of heat and mass transfer. 6th ed, Frank P. Incropera.*

For instance, the [Churchill-Bernstein equation](https://en.wikipedia.org/wiki/Churchill%E2%80%93Bernstein_equation) 
for convective heat transfer is used to approximate the dimensionless Nusselt number and thus estimate the 
convection coefficient between two fluids in cross-flow around a cylinder. The formula is quiet cumbersome to type in a calculator:
is quiet cumbersome to type in a calculator:

<a href="https://www.codecogs.com/eqnedit.php?latex=\overline{&space;\text{Nu}}_D&space;=&space;0.3&space;&plus;&space;\frac{0.62&space;\,&space;\text{Re}_D^\frac{1}{2}&space;\,&space;\text{Pr}^\frac{1}{3}&space;}&space;{&space;\left[1&space;&plus;&space;(0.4/\text{Pr})^\frac{2}{3})&space;\right]^\frac{1}{4}&space;}&space;\left[&space;1&space;&plus;&space;\left(\frac{Re_D}{282000}&space;\right)^\frac{5}{8}&space;\right]&space;^\frac{4}{5}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\overline{&space;\text{Nu}}_D&space;=&space;0.3&space;&plus;&space;\frac{0.62&space;\,&space;\text{Re}_D^\frac{1}{2}&space;\,&space;\text{Pr}^\frac{1}{3}&space;}&space;{&space;\left[1&space;&plus;&space;(0.4/\text{Pr})^\frac{2}{3})&space;\right]^\frac{1}{4}&space;}&space;\left[&space;1&space;&plus;&space;\left(\frac{Re_D}{282000}&space;\right)^\frac{5}{8}&space;\right]&space;^\frac{4}{5}" title="\overline{ \text{Nu}}_D = 0.3 + \frac{0.62 \, \text{Re}_D^\frac{1}{2} \, \text{Pr}^\frac{1}{3} } { \left[1 + (0.4/\text{Pr})^\frac{2}{3}) \right]^\frac{1}{4} } \left[ 1 + \left(\frac{Re_D}{282000} \right)^\frac{5}{8} \right] ^\frac{4}{5}" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=\text{Nu}_D" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\text{Nu}_D" title="\text{Nu}_D" /></a>
 is the Nusselt number, <a href="https://www.codecogs.com/eqnedit.php?latex=\text{Re}_D" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\text{Re}_D" title="\text{Re}_D" /></a>
  the Reynolds number and <a href="https://www.codecogs.com/eqnedit.php?latex=\text{Pr}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\text{Pr}" title="\text{Pr}" /></a>
  the Prandtl number. Designing a script running in the Numworks environment and that prompts the user for input variables
  would make the calculation of such formulas easy. 

## Design

The calculator has no file explorer, i.e. cannot use directories. 
It also have very few memory (see [below](#Specifications-of-calculator))
So we must reduce the amount of code as much as possible by designing an efficent wrapping of mathematical formulas.

To avoid loading too much instructions at once in the calculator, we separate the formulas in sections:

* Utility functions: used by every other script
* Linear interpolation (generic)
* Linear interpolation of thermophysical properties of water (hard-coded data)
* Linear interpolation of thermophysical properties of air (hard-coded data)
* Equations for fins
* Equations for convection (implicitly only free and forced convection)
* Equations for the boiling part of convection
* Equations for the condensation part of convection

The idea is to load only two scripts at once: the utility module and the script of interest.

### User interaction

1. The user chooses a script in the list of scripts on the calcultor
1. The user runs the script
1. The user is asked to choose which formula (of the loaded module) to use
1. The user is prompted to enter values of the formula input variable
1. Results are displayed

### Function design

All functions implementing formulas calculations have *no input and no output* (in the Pythonic sense).
The input/output is handled by the utility module, via the function `pr` (print) `out` and `get_params`.
In particular:

* `pr(msg, maxlen=29)`: print some text that properly fits on screen
* `out(desc, val)`: print value of physical variable, handle scientific notation
* `get_params(lst)`: prompt the user for the values of the formula variables whose names are given in `lst`

In particular, functions that implement formulas should perform in order:

1. Print the name of the equation and the context in which it is used with `pr`
1. Prompt the user for the values of the input variables with `get_param`
1. Perform calculations
1. Output the result


### Script format

Every script should follow this architecture:

1. Load the `utility` module
1. Set relevant functions that implement formulas (no input, no return)
    * Use `utility.get_params` to ask the user for the parameter values and load them in a python dictionnary
    * Try to use as few memory as possible
    * Output (numerical) results with `utility.out`
1. Create an option map that will allow the user to choose a formula, the map is a python dictionnary (key = display message, value = reference to the corresponding function)
1. The script ends with `utility.choose_opt(optmap)`



### Specifications of calculator

https://www.numworks.com/specs/

* Flash ROM: 8MB
* Static RAM: 256KB

https://www.numworks.com/resources/engineering/software/

> #### 3.2 Working with limited memory
> Our device has 256 KB of RAM. That’s very little memory by today’s standards. That being said, by writing code carefuly, a huge lot can be achieved in that space. After all, that’s 64 times more memory than the computer of the Apollo mission!

* Stack memory: 32KB, all local variables + context of code execution
* Heap memory: ??


