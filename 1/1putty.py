from pywinauto.application import Application
import time
import pywinauto

app=Application().start(cmd_line=r"C:\Programs\PuTTY\putty.exe")
time.sleep(2)
app=Application().connect(title="PuTTY Configuration")
window=app.PuTTYConfigBox
window.set_focus()
window[u"Host Name (or IP address):Edit"].type_keys("clxxx@tty.sdf.org")
window[u"Port:Edit"].type_keys("")
window["Open"].click()
