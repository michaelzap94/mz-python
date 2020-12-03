import os
import time
# os.name -> what platform you are running on.
print(os.name) # eg: posix
# os.environ -> mapping object that returns a dictionary of the user’s environmental variables
# print(os.environ)
# environ(
#     {
#         "TERM_PROGRAM": "vscode",
#         "TERM": "xterm-256color",
#         "SHELL": "/bin/bash",
#         "TMPDIR": "/var/folders/5y/95ks6ynd419f7r4t4kmpmhxm0000gn/T/",
#         "TERM_PROGRAM_VERSION": "1.51.1",
#         "ORIGINAL_XDG_CURRENT_DESKTOP": "undefined",
#         "USER": "michael",
#         "SSH_AUTH_SOCK": "/private/tmp/com.apple.launchd.SY2yHL9sfn/Listeners",
#         "__CF_USER_TEXT_ENCODING": "0x1F5:0x0:0x2",
#         "BASH_SILENCE_DEPRECATION_WARNING": "1\u2029export",
#         "PATH": "/Users/michael/.pyenv/shims:/Users/michael/.poetry/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin",
#         "PWD": "/Users/michael/Personal/mz-python",
#         "LANG": "en_GB.UTF-8",
#         "EMPIRE_API_URL": "https://microservices-empire.lystit.com",
#         "XPC_FLAGS": "0x0",
#         "XPC_SERVICE_NAME": "0",
#         "PYENV_SHELL": "bash",
#         "SHLVL": "1",
#         "HOME": "/Users/michael",
#         "VSCODE_GIT_ASKPASS_MAIN": "/Applications/Visual Studio Code.app/Contents/Resources/app/extensions/git/dist/askpass-main.js",
#         "LOGNAME": "michael",
#         "VSCODE_GIT_IPC_HANDLE": "/var/folders/5y/95ks6ynd419f7r4t4kmpmhxm0000gn/T/vscode-git-4416d9db00.sock",
#         "VSCODE_GIT_ASKPASS_NODE": "/Applications/Visual Studio Code.app/Contents/Frameworks/Code Helper (Renderer).app/Contents/MacOS/Code Helper (Renderer)",
#         "GIT_ASKPASS": "/Applications/Visual Studio Code.app/Contents/Resources/app/extensions/git/dist/askpass.sh",
#         "COLORTERM": "truecolor",
#         "_": "/Users/michael/.pyenv/versions/3.8.5/bin/python",
#     }
# )
# Accessing env variables
print(os.environ["HOME"]) # "/Users/michael" OR KeyError Exception if it doesn't exist
# You could also use the os.getenv function to access this environmental variable:
print(os.getenv("HOME")) # "/Users/michael" OR None if it doesn't exist
# You can also SET an environment variable
# However this code only affects subprocesses that you start using os.system(), os.popen(), etc. 
os.putenv('py_env_test', 'foo')
# If you try to get that environment variable that you just set using os.getenv(), it will return None.
print(os.getenv("py_env_test")) # None

# os.getcwd() -> get current working directory
print(os.getcwd()) # /Users/michael/Personal/mz-python
# os.chdir() -> change the directory that we’re currently running our Python session in
os.chdir("..")
print(os.getcwd()) # /Users/michael/Personal
os.chdir("./mz-python")

# os.mkdir() -> create a single folder. If it exists already -> FileExistsError
os.mkdir("mynewfolder") # create a folder in cwd: /Users/michael/Personal/mz-python
# os.mkdir(r'/usercode/pytest') # will not work as "usercode is not a folder"

# os.makedirs() -> create all the intermediate folders in a path if they don’t already exist
# current_dir = os.path.dirname(__file__)
# FILEPATH = os.path.join(current_dir, r'/usercodes/pytest\2017\02\01')
# os.makedirs(FILEPATH)

open("mynewfolder/test.txt", 'w')
# WINDOWS ONLY
# os.startfile() -> start a files as if you are double clicking using the associated program
# os.startfile("mynewfolder/test.txt")
os.system("open mynewfolder/test.txt")
time.sleep(5)
# os.rename() -> Renames files OR folders
os.rename("mynewfolder/test.txt", "mynewfolder/test2.txt")
time.sleep(5)
# os.remove() -> remove file
os.remove("mynewfolder/test2.txt")
time.sleep(5)
# os.rmdir() -> remove directory
os.rmdir("mynewfolder")
# os.walk() -> iterate over a root level path
for root, dirs, files in os.walk("."):
    print("------ROOT:", root) # the path we pass as a param, in this case: .
    print("------DIRS:")
    for _dir in dirs:
        print(_dir) # all folders
    print("------FILES:")
    for _file in files:
        print(_file)