# python-calc
Automate physics calculations in Python for Numworks calculator.

## About

### Current usage

Formulas about heat & mass transfer. We only implement formulas that are cumbersome to write manually in a calculator (i.e. lots of exponents, fractions, ...).

### Specifications of calculator

https://www.numworks.com/specs/

* Flash ROM: 8MB
* Static RAM: 256KB

https://www.numworks.com/resources/engineering/software/

> #### 3.2 Working with limited memory
> Our device has 256 KB of RAM. That’s very little memory by today’s standards. That being said, by writing code carefuly, a huge lot can be achieved in that space. After all, that’s 64 times more memory than the computer of the Apollo mission!

* Stack memory: 32KB, all local variables + context of code execution
* Heap memory: ??


## Design

The calculator has no file explorer, i.e. cannot use directories. It also have very few memory (-> avoid code redundancy as much as possible).

To avoid loading too much instructions, we separate the formulas in sections:

* Utility functions
* Linear interpolation
* Equations for fins
* Equations for convection (implicitly only free and forced convection)
* Equations for boiling (actually this is convection)
* Equations for condensation (this is also convection)
* ...

The idea is to load only two scripts at once: the utility module and the script of interest.

### User interaction

* User chooses a script in the list of scripts on the calcultor
* Script is running...
* User is asked to choose which formula (of the loaded module) to use
* User is asked to enter the parameters of the formula
* Results are displayed

### Function design

All functions implementing formulas have *no input and no output*. They manage input/output through the utility module. 

### Script format

Every script should follow this architecture:

1. Load the `utility` module
1. Set relevant functions that implement formulas (no input, no return)
    * Use `utility.get_params` to ask the user for the parameters and load them in a python dictionnary
    * Try to use as few memory as possible
    * Output results with `utility.out`
1. Create an option map that will allow the user to choose a formula, the map is a python dictionnary (key = display message, value = reference to the corresponding function)
1. The script ends with `utility.choose_opt(optmap)`

