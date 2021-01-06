# Executing shell commands that incorporate unsanitized input from an untrusted source makes a program vulnerable to shell injection, 
# a serious security flaw which can result in arbitrary command execution. 
# For this reason, the use of shell=True is strongly discouraged in cases where the command string is constructed from external input.

#=================================================
# The subprocess module provides a function named call.
# This function allows you to call another program, wait for the command to complete and then return the return code. 
# It accepts one or more arguments as well as the following keyword arguments (with their defaults): stdin=None, stdout=None, stderr=None, shell=False.
import subprocess
code = subprocess.call("ls")
if code == 0:
    print("Success!")
else:
    print("Error!")

code = subprocess.call(["ping", "-c 4", "www.facebook.com"])
if code == 0:
    print("Success!")
else:
    print("Error!")

#===============================================================

# The Popen class executes a child program in a new process. 
# Unlike the call method, it does not wait for the called process to end unless you tell it to using by using the wait method. 
# Leaves the cmd open

subprocess.Popen("du")
print("processing") # this is printed before or after(random) as Popen does not wait

#----------------------------------------------------------------
process = subprocess.Popen("du")
code = process.wait()
print(code)

#======================================
subprocess.Popen(["ls", "-l"])
#<subprocess.Popen object at 0xb7451001>
#======================================
# we redirect standard out (stdout) to our subprocess so we can communicate with it. 
process = subprocess.Popen(["du"], stdout=subprocess.PIPE)
# using the wait method can cause the child process to deadlock when using the stdout/stderr=PIPE commands when the process generates enough output to block the pipe. 
# You can use the communicate method to alleviate this situation. 
# The communicate method itself allows us to communicate with the process we just spawned.
# communicate will wait for the process to finish and then returns a two-element tuple that contains what was in stdout and stderr
data = process.communicate()
print(data)