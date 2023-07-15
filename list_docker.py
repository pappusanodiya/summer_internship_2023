#!/usr/bin/python3

import subprocess
import cgi
print("Content-Type: text/html")

print()

# print("<h1>This is the date</h1>")

# formdata= cgi.FieldStorage()
# data = formdata.getvalue("docker ps -a")
command = "sudo docker ps -a"
x= subprocess.getoutput(command)
print("<pre>")
print(x)
print("</pre>")
