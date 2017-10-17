import subprocess
test = subprocess.Popen(["python","-m","http.server","--bind", "localhost", "--cgi", "8008"], stdout=subprocess.PIPE)
output = test.communicate()[0]