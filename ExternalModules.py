#FROM PYTHON 3.4 pip is installed by default
#python(3) -m pip install NAME_OF_PACKAGE

from termcolor import colored
# help(termcolor) # prints documentation in the terminal
text = colored("HI THERE!", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)

