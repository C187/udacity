import time
import webbrowser

count = 0
while (count < 4):
    time.sleep(1)
    webbrowser.open("http://www.google.com")
    count = count + 1
else:
    print "done"
