import os, uuid, sys, json
import argparse
import tkinter
from tkinter import *

class App:

    def parseCommandArgs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-config")
        args = parser.parse_args()
        print(args.config)
        return args

    def loadConfig(self, path):
        local_path = os.getcwd() + '\\' + str(path)
        with open(local_path) as json_file:
            jsonConfig = json.loads(json_file.read())
            print("loaded config from data.json!")
            return jsonConfig

    def saveConfigButtonClickHandler(self):
        # set values in config
        # self.config['vision']['maxThreshold'] = self.maxThresholdScale.get()

        local_path = os.getcwd() + '\\config.json'
        with open(local_path, 'w') as outfile:
            json.dump(self.config, outfile)
            print("saved config to data.json!")

    def loadConfigButtonClickHandler(self):
        print("load config!")
        self.config = self.loadConfig(self.args.config)

        # load values in config
        # self.minThresholdScale.set(self.config['vision']['minThreshold'])

    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # parse command line args
        self.args = self.parseCommandArgs()
        self.config = self.loadConfig(self.args.config)
        print('args parsed!')

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = 640 , height = 480 )
        self.canvas.pack()

        self.saveConfigButton = Button(window, text="Save Config", command=lambda: self.saveConfigButtonClickHandler())
        self.saveConfigButton.pack(padx=15, pady=5, side=LEFT)

        self.loadConfigButton = Button(window, text="Load Config", command=lambda: self.loadConfigButtonClickHandler())
        self.loadConfigButton.pack(padx=15, pady=5, side=LEFT)
        # self.loadConfigButton = Button(window, text="Load Config", command=self.loadConfigButtonClickHandler())
        # self.loadConfigButton.pack(padx=15, pady=5, side=LEFT)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 5
        self.update()

        self.window.mainloop()

    def update(self):
        
        # update logic here...


        # do this at the end of update
        self.window.after(self.delay, self.update)

# Create a window and pass it to the Application object
App(tkinter.Tk(), "Starter Project")