# The sys module provides system specific parameters and functions
import sys
import subprocess

print(sys.argv)  # ['/Users/michael/Personal/mz-python/OS_Shell/sys.py'] ->, ...]
# because when you run the script you use: python ./sys.py
# run: python sys.py helloworld
print(sys.argv[1])  # helloworld

# absolute path of the python interpreter
print(sys.executable)  # /Users/michael/.pyenv/versions/3.8.5/bin/python

# The sys.exit() function allows the developer to exit from Python.
# The exit function takes an optional argument, typically an integer, that gives an exit status.
# Zero is considered a “successful termination”
# Note that when you call exit, it will raise the SystemExit exception,
# which allows cleanup functions to work in the finally clauses of try / except blocks.
# sys.exit(0)
code = subprocess.call(
    ["python", "/Users/michael/Personal/mz-python/OS_Shell/sys_dummy.py"]
)
print(code)  # 0

# The sys module’s path value is a list of strings that specifies the search path for modules.
# Basically this tells Python what locations to look in when it tries to import a module.print(sys.path)
print(sys.path)
# You can also modify the path.
# Because it’s a list, we can add or delete paths from it.
sys.path.append("/path/to/my/module")
print(sys.path)

# platform identifier
print(sys.platform)  # darwin
os = sys.platform
if os == "win32":
    # use Window-related code here
    import _winreg
elif os.startswith("linux"):
    # do something Linux specific
    import subprocess

    subprocess.Popen(["ls", "-l"])
elif os == "darwin":
    print("mac")

# stdin is used for all input given to the interpreter except for scripts whereas stdout is used for the output of print and expression statements.
# The primary reason I mention this is that you will sometimes need to redirect stdout or stderr or both to a file,
# such as a log or to some kind of display in a custom GUI you have created.
temp = sys.stdout                 # store original stdout(terminal) object for later
sys.stdout = open('OS_Shell/log.txt', 'w') # redirect all prints to this log file
print("testing123")               # nothing appears at interactive prompt
print("another line")             # again nothing appears. it's written to log file instead
sys.stdout.close()                # ordinary file object
sys.stdout = temp                 # restore print commands to interactive prompt
print("back to normal")           # this shows up in the interactive prompt

# Using sys.stdin: sys.stdin can be used to get input from the command line directly. 
# It used is for standard input. It internally calls the input() method. 
# It, also, automatically adds ‘\n’ after each sentence.
for line in sys.stdin: 
	if 'q' == line.rstrip(): 
		break
	print(f'Input : {line}') 

print("Exit") 
