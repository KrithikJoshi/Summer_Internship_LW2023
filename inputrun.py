import subprocess
import cgi

print("content-type: text/html")
print()

form = cgi.FieldStorage()
cmd = form.getvalue("c")

if "date" in cmd:
    output = subprocess.getoutput("date")
    print(output)
elif "c" in cmd:
    output = subprocess.getoutput("c")
    print(output)
else:
    print("not found")
