#!/usr/bin/python3

print("Content-type: text/html")
print()

import subprocess
import cgi

form = cgi.FieldStorage()

#print(form)

image_name = form.getvalue("q")
#image_tag = form.getvalue("tag")

cmd = "sudo docker pull " + image_name
print(cmd)
output =subprocess.getoutput(cmd)

print("<pre>")
print( output)
print("</pre>")
