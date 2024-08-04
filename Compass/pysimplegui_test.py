import PySimpleGUI as sg
import threading
import queue
from berryIMU import *

# Initialize the IMU sensor
imu = BerryIMU()

def get_compass_data(q: queue.Queue):
    while True:
        heading = imu.get_compass_data()
        q.put(heading)
        time.sleep(1)  # Pause for 1 second

layout = [[sg.Text('0', key='-TEXT-')]]
window = sg.Window('Hello Example', layout, finalize=True)

q = queue.Queue()
threading.Thread(target=get_compass_data, args=(q,), daemon=True).start()

while True:
    event, values = window.read(timeout=100)  # Check for events every 100 ms
    if event == sg.WIN_CLOSED:
        break
    if not q.empty():
        heading = q.get()
        window['-TEXT-'].update(heading)

window.close()