"""
    random_fox_api.py
    Jessica Soler
    5/2/2024
"""

import tkinter as tk
from tkinter import *

# I was able to get tkinter to open an image, but it opened in a photos app and not a GUI
# so after some research, I found the pillow library that allows me to open the image in a GUI
from PIL import Image, ImageTk
# image is used to open the image from the raw data in the API request
# imageTk is used to convert the image into a form tkinter can display

# BytesIO is used to convert the raw data from the API request into an image
from io import BytesIO

import requests

IS_DEBUGGING = False

URL = "https://randomfox.ca/floof/"

class Fox:
    def __init__(self):
        
        # create a GUI window
        self.root = tk.Tk()
        self.root.title("Random Foxes")
        
        self.create_widgets()
        self.root.mainloop()
        
#--------------------CREATE WIDGETS--------------------#
    def create_widgets(self):
        
        # create a button that gets a random fox image
        self.button = tk.Button(
            self.root,
            text="Get Fox",
            command=self.get_fox
        )
        self.button.pack()

        # create a label to display the fox image
        self.label = tk.Label(self.root)
        self.label.pack()
        
        # enter key will activate the get fox method
        self.root.bind('<Return>', self.get_fox)
        self.root.bind('<KP_Enter>', self.get_fox)
        
#--------------------GET FOX--------------------#        
    def get_fox(self, event=None):
    
        # GET request to the API and returned as a response object
        # response = raw data of the image file
        response = requests.get(URL)

        # watch for exception
        # if the status code == 200, request was successful
        # else, raise an exception
        if (response.status_code == 200):
            
            # json() is a method from the requests library
            # converting the JSON response into a python dictionary
            # fox = dictionary of the image file
            self.fox = response.json()
            
            # used to debug the data
            if (IS_DEBUGGING == TRUE):
                
                # display the status code
                print(f"\nStatus Code: {response.status_code}\n")
                
                # display the raw JSON data from the API
                print(f"The raw data from the API:")
                print(response.text)
                
                # display the Python dictionary
                print(f"\nThe JSON data converted to a Python dictionary:")
                print(self._advice_data)
                
            # accessing the image from the dictionary
            # and assigning it to a variable
            image_url = self.fox["image"]
            
            # GET request to the URL stored in the image_url variable
            # stores the response in the response variable
            response = requests.get(image_url)
            
            # open the image from the raw data in the API request
            # and convert it into a form tkinter can display
            image = Image.open(BytesIO(response.content))
            photo = ImageTk.PhotoImage(image)
            
            # display the image in the GUI
            # configure the label to display the image as a photo
            # and store the photo in the label
            self.label.config(image=photo)
            
            # store the reference to the photo in the label
            self.label.image = photo
            
        else:
            self.label.config(text="Error: Could not retrieve image")

        
#--------------------MAIN--------------------#
fox_gui = Fox()
        
    





