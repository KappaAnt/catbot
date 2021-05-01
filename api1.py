import requests
import json
from PIL import Image


class CatPic:
    def __init__(self):
        """
        Initializes CatPic instance vars
        args: none
        returns: none
        """ 
        self.api1_key = "?api_key=e4e3d41a-8e34-449c-b8cd-57cd21e0f42e"
        self.api_url = "https://api.thecatapi.com/v1/images/search" + self.api1_key
        self.request = ""
        self.request_final = ""
        self.cat_json = ""
        self.condition = True
        
    def get(self):
        """
        Gets data from catpic api and prepares catpic url
        args: none
        returns: none
        """
        try:
            self.request = requests.get(self.api_url)
            self.cat_json = self.request.json()
            cat_url = self.cat_json[0]['url']
        
            self.request_final = requests.get(cat_url) #This is the png
            print("CAT PIC: PREPARED")
        except ConnectionError:
            print("Error Occured")
            print("You must Troubleshoot Connection")                  
            self.condition = False
            
    def response(self):
        """
        Prints last response from api (confused)
        args: none
        returns: none
        """
        if self.condition == True:
            #I dont know what exactly is the last response so I have some ideas
            print("Possible last response option? - CatPics")
            #Request Msg?
            print(self.request) 
            #Whole Json?
            #print(self.cat_json)
            #Last part of json dictionary?
            last = self.cat_json[0]['height']
            print(last)
        else:
            return
            
    def useData(self):
        """
        Creates a cat file image and shows user
        args: none
        returns: none
        """
        if self.condition == True:
            #Creating File from Data
            with open("cat_pic1.jpg", "wb") as f:
                f.write(self.request_final.content)
                
            image = Image.open("cat_pic1.jpg")
            #image.show()
        else:
            return
        
        
        
 
