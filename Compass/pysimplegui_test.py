import PySimpleGUI as sg
import threading
from berryIMU import *

# Initialize the IMU sensor
imu = BerryIMU()

def get_compass_data(window: sg.Window):
    while True:
        heading = imu.get_compass_data()
        window.write_event_value('-UPDATE-', heading)
        time.sleep(1)  # Pause for 1 second

layout = [[sg.Text('0', key='-TEXT-')]]
window = sg.Window('Hello Example', layout, finalize=True)

threading.Thread(target=get_compass_data, args=(window,), daemon=True).start()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-UPDATE-':
        window['-TEXT-'].update(values['-UPDATE-'])

window.close()