import subprocess
test = subprocess.Popen(["python","-mwebbrowser","http://localhost:8008/cgi-bin/dilettante.py"], stdout=subprocess.PIPE)
output = test.communicate()[0]