import os
from datetime import date, datetime
from os.path import isfile, join, exists

if exists("raport.html"):
    os.remove("raport.html")
now = datetime.now()
fulldate = now.strftime("%d-%m-%Y %H:%M:%S")

outputfile = open("Raport.html", "w")

outputfile.write(f"""

<html>
  <head>
    <title>Raport Kajaki</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
  <h1>Raport {fulldate}</h1>
  <table>
    <tr>
      <th>input</th>
      <th>output</th>
    <tr>
    """)

inputfiles = [file for file in os.listdir("input") if isfile(join("input", file))]
for x in range(len(inputfiles)):
    with open(f"input/in{x}.txt", "r") as f:
        lines = [str(line.rstrip()) for line in f]
    outputfile.write(""" <tr><td>""" + str(lines).replace("'", "")[1:-1])

    outputfile.write("""</td>
          <td>""")
    with open(f"output/out{x}.txt", "r") as f:
        lines = [str(line.rstrip()) for line in f]
    outputfile.write(str(lines).replace("'", "")[1:-1])
    outputfile.write("""</td>
        </tr>""")
outputfile.write("""
  </table>
  </body>
</html>""")

outputfile.close()
