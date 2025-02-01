import tkinter
import os
from time import strftime
import time
import playsound
import random

PyOSVersion = "1.1.0"

def quit(event):
    if not skipShutdownAnim:
        playsound.playsound("assets/sounds/WindowsXPShutdown.mp3", False)
        app.after(1000, lambda: canvas.delete("all"))
        app.after(3500, lambda: app.quit())
    else:
        app.quit()

def start_drag(event):
    item = canvas.find_closest(event.x, event.y)[0]

    tags = canvas.gettags(item)

    for tag in tags:
        if tag in appTags:  
            current_group["tag"] = tag
            break

    last_mouse_position["x"] = event.x
    last_mouse_position["y"] = event.y

def drag(event):
    if current_group["tag"] is not None:
        dx = event.x - last_mouse_position["x"]
        dy = event.y - last_mouse_position["y"]

        canvas.move(current_group["tag"], dx, dy)

        last_mouse_position["x"] = event.x
        last_mouse_position["y"] = event.y


def webBrowserApp(event):
    closeStartMenu(1)

    canvas.create_rectangle(0, 0, 1280, 670, fill="black", tags="webbrowser")
    draggable = canvas.create_rectangle(10, 10, 1270, 50, fill="grey", tags="webbrowser")
    appHeader = canvas.create_text(640, 30, text="Web Browser", fill="black", font=("Arial", 20), anchor="center", tags = "webbrowser")
    canvas.create_text(640, 300, text="Not Finished", fill="white", font=("Arial", 20), justify = "left", tags = "app webbrowser")
    closeButton = canvas.create_rectangle(1230, 10, 1270, 50, fill="red", tags="webbrowser")

    canvas.tag_bind(closeButton, "<Button-1>", closeCurrentApp)


def shutDown(event):
    closeStartMenu(1)
    canvas.create_rectangle(350, 200, 950, 400, fill = "black", tags = "app shutDown")
    draggable = canvas.create_rectangle(360, 210, 940, 250, fill = "grey", tags = "app shutDown")
    closeButton = canvas.create_rectangle(900, 210, 940, 250, fill = "red", tags = "app shutDown")
    appHeader = canvas.create_text(650, 230, text="Shut Down", fill="black", font=("Arial", 20), anchor="center", tags = "app shutDown")
    canvas.create_text(650, 270, text="Shut Down?", fill="white", font=("Arial", 20), anchor="center", tags = "app shutDown")
    noButton = canvas.create_rectangle(400, 330, 600, 370, fill = "grey", tags = "app shutDown")
    noButton2 = canvas.create_text(500, 350, text="No", fill="white", font=("Arial", 20), anchor="center", tags = "app shutDown")
    yesButton = canvas.create_rectangle(700, 330, 900, 370, fill = "grey", tags = "app shutDown")
    yesButton2 = canvas.create_text(800, 350, text="Yes", fill="white", font=("Arial", 20), anchor="center", tags = "app shutDown")

    canvas.tag_bind(closeButton, "<Button-1>", closeCurrentApp)
    canvas.tag_bind(noButton, "<Button-1>", closeCurrentApp)
    canvas.tag_bind(noButton2, "<Button-1>", closeCurrentApp)
    canvas.tag_bind(yesButton, "<Button-1>", quit)
    canvas.tag_bind(yesButton2, "<Button-1>", quit)
    canvas.tag_bind(draggable, "<Button-1>", start_drag)
    canvas.tag_bind(draggable, "<B1-Motion>", drag)
    canvas.tag_bind(appHeader, "<Button-1>", start_drag)
    canvas.tag_bind(appHeader, "<B1-Motion>", drag)

def taskbar(destroy):
    if destroy is False:
        canvas.delete(taskbar_ID)
    else:    
        taskbar_ID = canvas.create_rectangle(0, 670, 1280, 720, fill = "red")

def startMenuClicked(event):
    global clockAppButtonID, webBrowserAppID, startMenuOpen

    print("Start menu clicked")
    closeDesktop(1)
    if startMenuOpen is True:
        closeStartMenu(1)
    else:
        startMenuOpen = True
        canvas.create_rectangle(0, 0, 1280, 670, fill = "black", tags = "app startMenu")
        clockAppButtonID = canvas.create_rectangle(300, 150, 340, 190, fill = "blue", tags = "app draggable clock startMenu") #app icon for clock
        canvas.create_text(320, 200, text= "Clock", fill="white", font=("Arial", 10), anchor="center", tags = "app clock startMenu")
        webBrowserAppID = canvas.create_rectangle(400, 150, 440, 190, fill = "green", tags = "app draggable webbrowser startMenu") #app icon for webbrowser
        canvas.create_text(420, 200, text= "Web Browser", fill="white", font=("Arial", 10), anchor="center", tags = "app webbrowser startMenu")
        textEditorAppID = canvas.create_rectangle(500, 150, 540, 190, fill = "yellow", tags = "app draggable textEditor startMenu") #app icon for text editor
        canvas.create_text(520, 200, text= "Text Editor", fill="white", font=("Arial", 10), anchor="center", tags = "app webbrowser startMenu")
        cliInterfaceAppID = canvas.create_rectangle(600, 150, 640, 190, fill = "grey", tags = "app draggable cliInterface startMenu") #app icon for cli interface
        canvas.create_text(620, 200, text= "CLI Interface", fill="white", font=("Arial", 10), anchor="center", tags = "app cliInterface startMenu")
        settingsAppID = canvas.create_rectangle(700, 150, 740, 190, fill = "purple", tags = "app draggable settings startMenu") #app icon for settings
        canvas.create_text(720, 200, text= "Settings", fill="white", font=("Arial", 10), anchor="center", tags = "app settings startMenu")
        paintAppID = canvas.create_rectangle(800, 150, 840, 190, fill = "pink", tags = "app draggable paint startMenu") #app icon for paint
        canvas.create_text(820, 200, text= "Paint", fill="white", font=("Arial", 10), anchor="center", tags = "app paint startMenu")  
        canvas.create_text(640, 100, text="Start Menu", fill="white", font=("Arial", 20), anchor="center", tags = "app startMenu")
        powerOffButton = canvas.create_rectangle(620, 600, 660, 640, fill = "red", tags = "app startMenu")
        canvas.create_text(640, 650, text= "Shut Down", fill="white", font=("Arial", 10), anchor="center", tags = "app startMenu")

        canvas.tag_bind(powerOffButton, "<Button-1>", shutDown)
        canvas.tag_bind(clockAppButtonID, "<Button-1>", clockApp) 
        canvas.tag_bind(webBrowserAppID, "<Button-1>", webBrowserApp) 
        canvas.tag_bind(textEditorAppID, "<Button-1>", textEditor)
        canvas.tag_bind(cliInterfaceAppID, "<Button-1>", openCLI)
        canvas.tag_bind(settingsAppID, "<Button-1>", settingsApp)
        canvas.tag_bind(paintAppID, "<Button-1>", paintApp)


def closeStartMenu(event):
    global startMenuOpen

    canvas.delete("startMenu")
    startMenuOpen = False

def closeCurrentApp(event):
    global appTags

    item = canvas.find_closest(event.x, event.y)[0]
    tags = canvas.gettags(item)
    appToDelete = ""

    currentAppToDelete = {"tag": None}

    for tag in tags:
        if tag in appTags:
            appToDelete = tag
            break

    closeApps(appToDelete)

    if appToDelete == "textEditor":
        entry.destroy()

    if appToDelete == "paint":
        with open("disk/paintFiles/paintTemp.txt", "w") as file:
            file.write("")

def closeApps(appToDelete):
    print("close apps")
    canvas.delete(f"{appToDelete}")

def closeDesktop(event):
    canvas.delete("startMenu")

class MockEvent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def createMockEvent():
    pointer_x = app.winfo_pointerx()  # Screen x-coordinate
    pointer_y = app.winfo_pointery()  # Screen y-coordinate

    # Convert screen coordinates to canvas coordinates
    canvas_x = canvas.canvasx(pointer_x)
    canvas_y = canvas.canvasy(pointer_y)

    mock_event = MockEvent(canvas_x, canvas_y)

    return mock_event

def settingsApp(event):
    global desktopTimeSetting, desktopTimeEnabled, desktopTimeButtonID, skipBootAnimButtonID, skipBootAnimSetting, skipShutdownAnimButtonID

    closeStartMenu(1)

    desktopTimeSetting = "red"
    skipBootAnimSetting = "red"
    skipShutdownAnimSetting = "red"

    if desktopTimeEnabled is True:
        desktopTimeSetting = "green"
    else:
        desktopTimeSetting = "red"

    if skipBootAnimInt == "1":
        skipBootAnimSetting = "green"
    else:
        skipBootAnimSetting = "red"

    if skipShutdownAnimInt == "1":
        skipShutdownAnimSetting = "green"
    else:
        skipShutdownAnimSetting = "red"

    canvas.create_rectangle(0, 0, 1280, 670, fill="black", tags="settings")
    draggable = canvas.create_rectangle(10, 10, 1270, 50, fill="grey", tags="settings")
    appHeader = canvas.create_text(640, 30, text="Settings", fill="black", font=("Arial", 20), anchor="center", tags = "settings")
    closeButton = canvas.create_rectangle(1230, 10, 1270, 50, fill="red", tags="settings")

    canvas.create_text(100, 80, text="Taskbar Time", fill="white", font=("Arial", 20), anchor="center", tags = "settings")
    desktopTimeButtonID = canvas.create_rectangle(200, 60, 240, 100, fill=desktopTimeSetting, tags="settings")

    canvas.create_text(140, 150, text="Skip Boot Animation", fill="white", font=("Arial", 20), anchor="center", tags = "settings")
    skipBootAnimButtonID = canvas.create_rectangle(280, 130, 320, 170, fill=skipBootAnimSetting, tags="settings")

    canvas.create_text(170, 220, text="Skip Shutdown Animation", fill="white", font=("Arial", 20), anchor="center", tags = "settings")
    skipShutdownAnimButtonID = canvas.create_rectangle(340, 200, 380, 240, fill=skipShutdownAnimSetting, tags="settings")

    applyChangesButtonID = canvas.create_rectangle(480, 600, 800, 660, fill="green", tags="settings")
    applyChangesTextID = canvas.create_text(640, 630, text="Apply Changes", fill="white", font=("Arial", 20), anchor="center", tags = "settings")


    canvas.tag_bind(closeButton, "<Button-1>", checkChanges)
    canvas.tag_bind(desktopTimeButtonID, "<Button-1>", configureDesktopTimer)
    canvas.tag_bind(skipBootAnimButtonID, "<Button-1>", configureSkipBootAnim)
    canvas.tag_bind(skipShutdownAnimButtonID, "<Button-1>", configureSkipShutdownAnim)
    canvas.tag_bind(applyChangesButtonID, "<Button-1>", applySettings)
    canvas.tag_bind(applyChangesTextID, "<Button-1>", applySettings)

def applySettings(event):
    global skipBootAnimInt, skipShutdownAnimInt
    
    canvas.delete("all")

    with open("disk/settings/skipBootAnim.txt", "w") as file:
        if skipBootAnim == True:
            file.write("1")
            skipBootAnimInt = "1"
        else:
            file.write("0")
            skipBootAnimInt = "0"
    
    with open("disk/settings/skipShutdownAnim.txt", "w") as file:
        if skipShutdownAnim == True:
            file.write("1")
            skipShutdownAnimInt = "1"
        else:
            file.write("0")
            skipShutdownAnimInt = "0"

    init()

def checkChanges(event):
    global desktopTimeSetting, desktopTimeEnabled, skipBootAnim, skipShutdownAnim

    if desktopTimeSetting == "green":
        desktopTimeEnabled = True
    else:
        desktopTimeEnabled = False
    
    if skipBootAnimInt == "1":
        skipBootAnim = True
    else:
        skipBootAnim = False

    if skipShutdownAnimInt == "1":
        skipShutdownAnim = True
    else:
        skipShutdownAnim = False

    closeCurrentApp(createMockEvent())

def configureSkipShutdownAnim(event):
    global skipShutdownAnim, skipBootAnimSetting, skipShutdownAnimButtonID

    if skipShutdownAnim is False:
        skipShutdownAnim = True
        canvas.itemconfig(skipShutdownAnimButtonID, fill="green")
    else:
        skipShutdownAnim = False
        canvas.itemconfig(skipShutdownAnimButtonID, fill="red")


def configureSkipBootAnim(event):
    global skipBootAnimButtonID, skipBootAnimSetting, skipBootAnim

    if skipBootAnim is False:
        skipBootAnim = True
        canvas.itemconfig(skipBootAnimButtonID, fill="green")
    else:
        skipBootAnim = False
        canvas.itemconfig(skipBootAnimButtonID, fill="red")

def configureDesktopTimer(event):
    global desktopTimeEnabled, desktopTimeButtonID

    if desktopTimeEnabled is True:
        desktopTimeEnabled = False
        canvas.itemconfig(desktopTimeButtonID, fill="red")
    else:
        desktopTimeEnabled = True
        canvas.itemconfig(desktopTimeButtonID, fill="green")


def clockApp(event):
    
    closeStartMenu(1)

    canvas.create_rectangle(350, 200, 950, 400, fill = "black", tags = "app clock")
    draggable = canvas.create_rectangle(360, 210, 940, 250, fill = "grey", tags = "app clock")
    closeButton = canvas.create_rectangle(900, 210, 940, 250, fill = "red", tags = "app clock")
    appHeader = canvas.create_text(650, 230, text="Clock", fill="black", font=("Arial", 20), anchor="center", tags = "app clock")    
    time = canvas.create_text(650, 300, text= "00:00:00", fill="white", font=("Arial", 40), anchor="center", tags = "app clock")


    canvas.tag_bind(draggable, "<Button-1>", start_drag)
    canvas.tag_bind(draggable, "<B1-Motion>", drag)
    canvas.tag_bind(appHeader, "<Button-1>", start_drag)
    canvas.tag_bind(appHeader, "<B1-Motion>", drag)
    canvas.tag_bind(closeButton, "<Button-1>", closeCurrentApp)

    def update_time():
        current_time = strftime("%H:%M:%S")
        canvas.itemconfig(time, text=current_time)
        canvas.after(1000, update_time)

    update_time()

def desktop(event):
    global timeID, desktopTimeEnabled

    READMEIconID = canvas.create_rectangle(20, 10, 80, 90, fill = "blue", tags = "desktop")
    canvas.create_text(50, 100, text= "README", fill="black", font=("Arial", 10), anchor="center", tags = "desktop")
    canvas.tag_bind(READMEIconID, "<Button-1>", openReadmeDoc)
    if desktopTimeEnabled:
        timeID = canvas.create_text(1200,695, text = "00:00:00", fill = "white", font = ("Arial", 20))

def openReadmeDoc(event):

    docText = "Web Browser is a placeholder\nClick Escape key to force quit\nIn the text editor the blue button saves the current session and the green button loads the saved session\nOnly one Text Editor session can be saved at a time"

    canvas.create_rectangle(0, 0, 1280, 670, fill = "black", tags = "app readme")
    draggable = canvas.create_rectangle(10, 10, 1270, 50, fill = "grey", tags = "app readme")
    closeButton = canvas.create_rectangle(1230, 10, 1270, 50, fill = "red", tags = "app readme")
    appHeader = canvas.create_text(640, 30, text="README", fill="black", font=("Arial", 20), anchor="center", tags = "app readme")    
    docContents = canvas.create_text(640, 300, text=docText, fill="white", font=("Arial", 20), justify = "left", tags = "app readme")

    canvas.tag_bind(closeButton, "<Button-1>", closeCurrentApp)

def textEditor(event):
    global entry, entry_window

    closeStartMenu(1)

    entry = tkinter.Text(app, width = 155, height = 37, bg = "black", fg = "white", insertbackground = "white")
    entry_window = canvas.create_window(640, 360, window=entry)
    canvas.create_rectangle(0, 0, 1280, 670, fill="black", tags="textEditor")
    draggable = canvas.create_rectangle(10, 10, 1270, 50, fill="grey", tags="textEditor")
    appHeader = canvas.create_text(640, 30, text="Text Editor", fill="black", font=("Arial", 20), anchor="center", tags = "textEditor")
    closeButton = canvas.create_rectangle(1230, 10, 1270, 50, fill="red", tags="textEditor")
    saveButton = canvas.create_rectangle(70, 675, 400, 715, fill="red", tags="textEditor")
    loadButton = canvas.create_rectangle(420, 675, 750, 715, fill="red", tags="textEditor")
    clearButton = canvas.create_rectangle(770, 675, 1100, 715, fill="red", tags="textEditor")
    saveText = canvas.create_text(235, 695, text="Save", font=("Arial", 20), anchor="center", tags="textEditor")
    loadText = canvas.create_text(580, 695, text="Load", font=("Arial", 20), anchor="center", tags="textEditor")
    clearText = canvas.create_text(935, 695, text="Clear", font=("Arial", 20), anchor="center", tags="textEditor")

    canvas.tag_bind(closeButton, "<Button-1>", closeCurrentApp)
    canvas.tag_bind(saveButton, "<Button-1>", saveFile)
    canvas.tag_bind(loadButton, "<Button-1>", loadFile)
    canvas.tag_bind(saveText, "<Button-1>", saveFile)
    canvas.tag_bind(loadText, "<Button-1>", loadFile)
    canvas.tag_bind(clearButton, "<Button-1>", lambda event: entry.delete("1.0", tkinter.END))
    canvas.tag_bind(clearText, "<Button-1>", lambda event: entry.delete("1.0", tkinter.END))

def saveFile(event):
    text = entry.get("1.0", tkinter.END).strip()
    directory = "disk/textFiles/textEditorMemory.txt"
    with open(directory, "w") as file:
        file.write(text)

def loadFile(event):
    with open("disk/textFiles/textEditorMemory.txt", "r") as file:
        content = file.read()
    entry.delete("1.0", tkinter.END)
    entry.insert("1.0", content)

def updateDesktopTime():
   current_time = strftime("%H:%M:%S")
   canvas.itemconfig(timeID, text=current_time)
   canvas.after(1000, updateDesktopTime)

def openCLI(event):
    global entryCLI, entry_windowCLI, cliBg

    closeStartMenu(1)
    cliBg = canvas.create_rectangle(0, 0, 1280, 720, fill = "black", tags="cli")
    entryCLI = tkinter.Text(app, width = 116, height = 34, bg = "black", fg = "white", insertbackground = "white", font=("Courier", 14))
    entry_windowCLI = canvas.create_window(640, 360, window=entryCLI)
    with open("disk/bsodLog/bsod.txt", "r") as file:
        didBsodHappenLastTime = file.read()
    if didBsodHappenLastTime == "1":
        entryCLI.insert("1.0", "Entering recovery mode...\nA fatal error occured on last boot. Type 'repair' to attempt system repair.\n<recovery>")
        entryCLI.bind("<Return>", processRecoveryCommand)
    else:
        entryCLI.insert("1.0", f"PyOS Version {PyOSVersion}\nWelcome to PyOS. Type 'help' for a list of commands.\n<root>")
        entryCLI.bind("<Return>", processCommand)

def processCommand(event):
    import time
    current_line = entryCLI.index("insert").split(".")[0]
    line_text = entryCLI.get(f"{current_line}.0", f"{current_line}.end")

    directory = "<root>"

    if line_text == directory + "help":
        entryCLI.insert(tkinter.END, f"""
List Of Commands:
help        - Displays a list of available commands
exit        - Exit PyOS
desktop     - Open PyOS desktop
clear       - Clear the command line
time        - Get the current time
ver         - Get current PyOS version
status      - Display the system status
sudo        - Run with admin permisions
rm -rf /    - Delete the all saved files
{directory}""")
    elif line_text == directory + "clear":
        entryCLI.delete("1.0", tkinter.END)
        entryCLI.insert(tkinter.END, f"{directory}")
    elif line_text == directory + "desktop":
        closeCLI()
    elif line_text == directory + "exit":
        quit(1)
    elif line_text == directory + "time":
        time = strftime("%H:%M:%S")
        entryCLI.insert(tkinter.END, f"\n{time}\n{directory}")
    elif line_text == directory + "ver":
        entryCLI.insert(tkinter.END, f"\n{PyOSVersion}\n{directory}")
    elif line_text == directory + "status":
        entryCLI.insert(tkinter.END, f"\nSystem status: Healthy\n{directory}") 
    elif line_text == directory + "rm -rf /":
        entryCLI.insert(tkinter.END, f"\nAccess denied as you do not have the required privileges\n{directory}")
    elif line_text == directory + "sudo rm -rf /":
        entryCLI.insert(tkinter.END, f"\nThis command will wipe the drive\nAre you sure you want to proceed? (y/n)\n<sudo>")
    elif line_text == "<sudo>y":
        entryCLI.insert(tkinter.END, f"\nProccessing...")
        app.after(1000, lambda: entryCLI.insert(tkinter.END, f"\nRemoving desktop..."))
        app.after(2000, lambda: entryCLI.insert(tkinter.END, f"\nRemoving files..."))
        app.after(3000, lambda: entryCLI.insert(tkinter.END, f"\nRemoving command line..."))
        app.after(5000, closeCLI)
        app.after(5000, lambda: canvas.create_rectangle(0, 0, 1280, 720, fill = "white", tags="cli"))
        app.after(7000, lambda: canvas.create_rectangle(0, 0, 1280, 720, fill = "black", tags="cli"))
        app.after(8000, bsod)
    elif line_text == "<sudo>n":
        entryCLI.insert(tkinter.END, f"\nProccess terminated\n{directory}")
    else:
        entryCLI.insert(tkinter.END, f"\nUnknown Command\n{directory}")
        playsound.playsound("assets/sounds/error.mp3", False)

def processRecoveryCommand(event):
    current_line = entryCLI.index("insert").split(".")[0]
    line_text = entryCLI.get(f"{current_line}.0", f"{current_line}.end")

    directory = "<recovery>"

    if line_text == directory + "repair":
        entryCLI.insert(tkinter.END, f"\nAttempting system repair...")
        app.after(5000, repairSystem)
        app.after(5000, lambda: entryCLI.insert(tkinter.END, f"\nSuccess! Restart system to finish repair\n{directory}"))
    elif line_text == directory + "exit":
        quit(1)
    elif line_text == directory + "status":
        entryCLI.insert(tkinter.END, f"\nSystem status: Critical\n{directory}") 
    else:
        entryCLI.insert(tkinter.END, f"\nUnknown command\n{directory}")

def closeCLI():
    entryCLI.destroy()
    canvas.delete(cliBg)   
    taskbar(True)
    desktop(1)
    startMenuID = canvas.create_rectangle(10, 675, 50, 715, fill = "black")
    canvas.tag_bind(startMenuID, "<Button-1>", startMenuClicked)
    
def bsod():
    canvas.create_rectangle(0, 0, 1280, 720, fill = "white", tags="cli")
    app.after(1000, lambda: canvas.create_rectangle(0, 0, 1280, 720, fill = "blue", tags="cli"))
    app.after(1000, lambda: canvas.create_text(640, 360, text="Fatal Error", font=("Courier", 40), fill="white"))
    app.after(6000, lambda: app.quit())
    with open("disk/bsodLog/bsod.txt", "w") as file: # 1 means bsod happend and 0 means it didnt
        file.write("1")
    
def repairSystem():
    with open("disk/bsodLog/bsod.txt", "w") as file:
        file.write("0") 

def init():
    taskbar(True)
    desktop(1)

    startMenuID = canvas.create_rectangle(10, 675, 50, 715, fill = "black")
    canvas.tag_bind(startMenuID, "<Button-1>", startMenuClicked)

    updateDesktopTime()

def bootAnim():
    image = tkinter.PhotoImage(file="assets/images/python.png")
    app.after(1000, lambda: canvas.create_image(640, 250, image=image, tags="boot"))
    app.after(1000, lambda: canvas.create_text(640, 430, text="PyOS", font=("Arial", 40), fill="Black", tags="boot"))

    app.after(2500, lambda: canvas.create_rectangle(340, 500, 940, 580, fill = "black", tags="boot"))

    app.after(3000, lambda: canvas.create_rectangle(345, 505, 375, 575, fill = "grey", tags="boot"))
    app.after(3500, lambda: canvas.create_rectangle(380, 505, 410, 575, fill = "grey", tags="boot"))
    app.after(4000, lambda: canvas.create_rectangle(415, 505, 445, 575, fill = "grey", tags="boot"))
    app.after(4500, lambda: canvas.create_rectangle(450, 505, 480, 575, fill = "grey", tags="boot"))
    app.after(5000, lambda: canvas.create_rectangle(485, 505, 515, 575, fill = "grey", tags="boot"))
    app.after(5500, lambda: canvas.create_rectangle(520, 505, 550, 575, fill = "grey", tags="boot"))
    app.after(5600, lambda: canvas.create_rectangle(555, 505, 585, 575, fill = "grey", tags="boot"))
    app.after(5700, lambda: canvas.create_rectangle(590, 505, 620, 575, fill = "grey", tags="boot"))
    app.after(5800, lambda: canvas.create_rectangle(625, 505, 655, 575, fill = "grey", tags="boot"))
    app.after(5900, lambda: canvas.create_rectangle(660, 505, 690, 575, fill = "grey", tags="boot"))
    app.after(6000, lambda: canvas.create_rectangle(695, 505, 725, 575, fill = "grey", tags="boot"))
    app.after(7500, lambda: canvas.create_rectangle(730, 505, 760, 575, fill = "grey", tags="boot"))
    app.after(8000, lambda: canvas.create_rectangle(765, 505, 795, 575, fill = "grey", tags="boot"))
    app.after(9000, lambda: canvas.create_rectangle(800, 505, 830, 575, fill = "grey", tags="boot"))
    app.after(10000, lambda: canvas.create_rectangle(835, 505, 865, 575, fill = "grey", tags="boot"))
    app.after(11500, lambda: canvas.create_rectangle(870, 505, 900, 575, fill = "grey", tags="boot"))
    app.after(13500, lambda: canvas.create_rectangle(905, 505, 935, 575, fill = "grey", tags="boot"))

    app.after(13500, lambda: playsound.playsound("assets/sounds/macosStartup.mp3", False))
    app.after(14500, lambda: canvas.delete("all"))
    app.after(15000, init)
    app.after(15000, lambda: app.bind("<Escape>", quit))

    app.image = image

def paintApp(event):
    closeStartMenu(1)

    canvas.create_rectangle(0, 0, 1280, 670, fill="black", tags="paint")
    canvas.create_rectangle(30, 80, 170, 640, fill="grey", tags="paint")
    #colours
    blackID = canvas.create_rectangle(35, 90, 95, 150, fill="black", tags="paint")
    whiteID = canvas.create_rectangle(105, 90, 165, 150, fill="white", tags="paint")
    redID = canvas.create_rectangle(35, 160, 95, 220, fill="red", tags="paint")
    orangeID = canvas.create_rectangle(105, 160, 165, 220, fill="orange", tags="paint")
    blueID = canvas.create_rectangle(35, 230, 95, 290, fill="blue", tags="paint")
    greenID = canvas.create_rectangle(105, 230, 165, 290, fill="green", tags="paint")
    yellowID = canvas.create_rectangle(35, 300, 95, 360, fill="yellow", tags="paint")
    pinkID = canvas.create_rectangle(105, 300, 165, 360, fill="pink", tags="paint")
    purpleID = canvas.create_rectangle(35, 370, 95, 430, fill="purple", tags="paint")
    brownID = canvas.create_rectangle(105, 370, 165, 430, fill="brown", tags="paint")

    paintArea = canvas.create_rectangle(200, 50, 1080, 670, fill="white", outline="white", tags="paint")
    draggable = canvas.create_rectangle(10, 10, 1270, 50, fill="grey", tags="paint")
    appHeader = canvas.create_text(640, 30, text="Paint", fill="black", font=("Arial", 20), anchor="center", tags="paint")
    closeButton = canvas.create_rectangle(1230, 10, 1270, 50, fill="red", tags="paint")

    saveButton = canvas.create_rectangle(70, 675, 400, 715, fill="red", tags="paint")
    loadButton = canvas.create_rectangle(420, 675, 750, 715, fill="red", tags="paint")
    clearButton = canvas.create_rectangle(770, 675, 1100, 715, fill="red", tags="paint")
    saveText = canvas.create_text(235, 695, text="Save", font=("Arial", 20), anchor="center", tags="paint")
    loadText = canvas.create_text(580, 695, text="Load", font=("Arial", 20), anchor="center", tags="paint")
    clearText = canvas.create_text(935, 695, text="Clear", font=("Arial", 20), anchor="center", tags="paint")

    canvas.tag_bind(paintArea, "<B1-Motion>", paintSquares)
    canvas.tag_bind(paintArea, "<Button-1>", paintSquares)
    canvas.tag_bind(closeButton, "<Button-1>", closeCurrentApp)
    canvas.tag_bind(blackID, "<Button-1>", lambda event: changeBrushColour(event, "black"))
    canvas.tag_bind(whiteID, "<Button-1>", lambda event: changeBrushColour(event, "white"))
    canvas.tag_bind(redID, "<Button-1>", lambda event: changeBrushColour(event, "red"))
    canvas.tag_bind(orangeID, "<Button-1>", lambda event: changeBrushColour(event, "orange"))
    canvas.tag_bind(blueID, "<Button-1>", lambda event: changeBrushColour(event, "blue"))
    canvas.tag_bind(greenID, "<Button-1>", lambda event: changeBrushColour(event, "green"))
    canvas.tag_bind(yellowID, "<Button-1>", lambda event: changeBrushColour(event, "yellow"))
    canvas.tag_bind(pinkID, "<Button-1>", lambda event: changeBrushColour(event, "pink"))
    canvas.tag_bind(purpleID, "<Button-1>", lambda event: changeBrushColour(event, "purple"))
    canvas.tag_bind(brownID, "<Button-1>", lambda event: changeBrushColour(event, "brown"))

    canvas.tag_bind(saveButton, "<Button-1>", savePaintFile)
    canvas.tag_bind(loadButton, "<Button-1>", loadPaintFile)
    canvas.tag_bind(saveText, "<Button-1>", savePaintFile)
    canvas.tag_bind(loadText, "<Button-1>", loadPaintFile)
    canvas.tag_bind(clearButton, "<Button-1>", clearPaintFile)
    canvas.tag_bind(clearText, "<Button-1>", clearPaintFile)

def changeBrushColour(event, colour):
    global paintBrushColour
    paintBrushColour = colour

def paintSquares(event):
    if event.x >= 200 and event.x <= 1070:
        if event.y >= 50 and event.y <= 660:
            canvas.create_rectangle(event.x, event.y, event.x + 10, event.y + 10, fill=paintBrushColour, outline=paintBrushColour, tags="paint drawn")
            with open("disk/paintFiles/paintTemp.txt", "a") as file:
                file.write(f"{event.x} {event.y} {paintBrushColour}\n")

def loadPaintFile(event):
    canvas.delete("drawn")
    contents = ""

    with open("disk/paintFiles/paint.txt", "r") as file:
        for line in file:
            values = line.split()
            x = int(values[0])
            y = int(values[1])
            colour = values[2]
            canvas.create_rectangle(x, y, x + 10, y + 10, fill=colour, outline=colour, tags="paint drawn")

    with open("disk/paintFiles/paint.txt", "r") as file:
        contents = file.read()
        print(contents)

    with open("disk/paintFiles/paintTemp.txt", "w") as file:
        file.write(contents)

def savePaintFile(event):
    with open("disk/paintFiles/paintTemp.txt", "r") as file:
        contents = file.read()
        with open("disk/paintFiles/paint.txt", "w") as file:
            file.write(contents)

def clearPaintFile(event):
    canvas.delete("drawn")
    with open("disk/paintFiles/paintTemp.txt", "w") as file:
        file.write("")

app = tkinter.Tk()
app.title("PyOS")
app.geometry("1920x1080") # true dimensions approx.: 1280, 720. Top of screen is 0 for some reason (bottom is 720)
app.attributes("-fullscreen", True)

last_mouse_position = {"x": 0, "y": 0}
current_group = {"tag": None}
is_dragging = {"value": False}

startMenuOpen = False

appTags = ["clock", "shutDown", "webbrowser", "readme", "textEditor", "cli", "settings", "paint"]
cliOpen = True

desktopTimeEnabled = True


canvas = tkinter.Canvas(app, width=1000, height=600, bg="grey")
canvas.pack(fill = "both", expand = True)

paintBrushColour = "black"

skipBootAnim = False
skipShutdownAnim = False

with open("disk/settings/skipBootAnim.txt", "r") as file:
    skipBootAnimInt = file.readline().strip()

with open("disk/settings/skipShutdownAnim.txt", "r") as file:
    skipShutdownAnimInt = file.readline().strip()

with open("disk/bsodLog/bsod.txt", "r") as file:
    didBsodHappenLastTime = file.read()

if skipBootAnimInt == "1":
    skipBootAnim = True
else:
    skipBootAnim = False

if skipShutdownAnimInt == "1":
    skipShutdownAnim = True
else:
    skipShutdownAnim = False

if not skipBootAnim and didBsodHappenLastTime != "1":
    bootAnim()
elif didBsodHappenLastTime == "1":
    openCLI(1)
else:
    app.bind("<Escape>", quit)
    init()

app.mainloop()