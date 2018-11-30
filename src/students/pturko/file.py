from datetime import datetime
now = datetime.now()
f = open("filename", "a+")
f.write("Time: {}\n".format(now))
f.seek(0)

