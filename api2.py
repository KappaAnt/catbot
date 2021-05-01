import requests
import json
import os

class CatFact:
    def __init__(self):
        """
        Initializes CatFact instance vars
        args: none
        returns: none
        """  
        #Originally I had daily cat facts, but it refused to work
        #after I initially ran one fact. Im guessing its time constrained
        #SO.. I switched to this cat fact api!
        self.api_url = os.environ["FACT_TOKEN"]
        self.request = ""
        self.fact_json = ""
        self.condition = True
        
    def get(self):
        """
        Gets data from catfact api and prints cat fact
        args: none
        returns: none
        """
        try:
            self.request = requests.get(self.api_url)
            self.fact_json = self.request.json() 
            print("CAT FACT: " + self.fact_json['fact'])
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
            print("Possible last response option? - CatFacts")
            #Request Msg?
            print(self.request) 
            #Whole Json?
            #print(self.fact_json)
            #Last part of json dictionary?
            last = self.fact_json['length']
            print(last)
        else:
            return
        
            
