import requests

class CatGif:
    def __init__(self):
        """
        Initializes CatPic instance vars
        args: none
        returns: none
        """ 
       
        self.api_url = "https://cataas.com/cat/gif"
        self.request = ""
        self.condition = True
        
    def get(self):
        """
        Gets data from catpic api and prepares catpic url
        args: none
        returns: none
        """
        try:
            #self.request = requests.get(self.api_url)
            #self.cat_json = self.request.json()
            #cat_url = self.cat_json[0]['url']
            
            cat_url = self.api_url
            self.request = requests.get(cat_url) #This is the png
            print("CAT PIC: PREPARED")
        except ConnectionError:
            print("Error Occured")
            print("You must Troubleshoot Connection")                  
            self.condition = False
            
            
    def useData(self):
        """
        Creates a cat file image and shows user
        args: none
        returns: none
        """
        if self.condition == True:
            #Creating File from Data
            with open("cat_gif.gif", "wb") as f:
                f.write(self.request_final.content)
                

        else:
            return
