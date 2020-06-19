import PySimpleGUI as sg

image_gif = "img/icon_64x64.gif"
image_icon = "img/battery_health.icns"

sg.theme("DarkTanBlue")
# "SandyBeach, BrightColors, Black, DarkBlack1
# Section 2: Stuff in Window, Elements/Widgets
layout = [ [sg.Image(filename=image_gif, pad=(50, 0, (0, 0))), sg.Text(" BATTERY HEALTH ", font='futura 40')],
           [sg.Text("What is the Current Cycle Count? ", size=(30, 1)), sg.In(key='current_cc', tooltip=" Is Dave really single? " + "\n" + "...Clear my Schedule.", size=(30, 1))],
           [sg.Text("What is the Max Cycle? ", size=(30, 1)), sg.In(key='maxcc', tooltip=' Why whisper when a yell travels twice as far? ', size=(30, 1))],
           [sg.Text("What is the Current Max Power? ", size=(30, 1)), sg.In(key='currentpow', tooltip=" Three Incredible Financial Tips: " + "\n" + " 1. Cut your own hair. " + "\n" + " 2. Stop mowing the lawn. " + "\n" + " 4. Blow up your TV ", size=(30, 1))],
           [sg.Text("What is 80% of Max Power", size=(30, 1)), sg.In(key='maxpow', tooltip="Have I told you what a good job you're doing? " + "\n" + " You're doing a great job! ",  size=(30, 1))],
           [sg.Button("Get Battery Health", bind_return_key=True, size=(25, 1), pad=(10, 5)), sg.Button('Cancel', size=(27, 1), pad=((30, 5), 10))], ]
          #[sg.Output(size=(50, 0), pad=(30, 5), key='health')]]

# default pad is (5, 3), which is 5 px on x-axis and 3 on y-axis
# (5, 5) 5 pad x-axis left and right, 5px pad above and beloForceTopLevel
# If you want 200 pixels on the left side, and 3 pixels on the right,
# the pad would be ((200,3), 3). In this example, only the x-axis is split.

# Create Window
window = sg.Window('Get Battery Health', icon=image_icon, font=('Helvetica', '13'), debugger_enabled=True).Layout(layout)

# Event Loop to process "Events" and get the "Values" of the Inputs
while True:
    event, values = window.read()

    current_cc = int(values['current_cc'])
    maxcc = int(values['maxcc'])
    currentpow = int(values['currentpow'])
    maxpow = int(values['maxpow'])

    if current_cc < maxcc and currentpow > maxpow:
        health = "Normal"
    if current_cc < maxcc and currentpow < maxpow:
        health = "Defective"
    if current_cc > maxcc:
        health = "Depleted"
    if current_cc == maxcc or currentpow == maxpow:
        health = "I doubt it. Try again or something..."

    if event in (None, 'Cancel'):
        break
    # Close Window
    window.close()
# In a GUI they can replace input and print (there often is no console)
# There are a lot of them, and a lot of options.
# Create window
    # print(health, " ", end="")
    sg.popup(title="Results", icon=image_icon, font=('Futura', '15'), custom_text=f"Your Battery:\n Is {health}!")


