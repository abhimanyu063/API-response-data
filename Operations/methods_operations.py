from Config import api_config as api
import requests
import json
import csv
from datetime import datetime


class getData:
    def __init__(self):
        pass

    def getApiResponseData(self):
        try:
            # Configure api url from api.config.py file.
            url = api.api_config["url"] + "?" + "resource_id=" +  api.api_config["resource_id"] + "&limit=" + str(api.api_config["limit"])
            print("Loading api url.")
            # Getting response from api using GET method.
            res = requests.get(url)
            print("Getting response from api.")
            # Checking response code if returning 200 then will go for further opertions.
            if res.status_code == 200:
                print("Got ok response from api.")
                # Loading json response data.
                jsondata = json.loads(res.content.decode('UTF-8'))
                print("Loading response data in json.")
                # We will open a file for writing.
                datafile = open("Files/Output_file.csv", 'w', newline='')
                print("Opening a file for writing.")
                # Create csv writer object.
                csv_wrt = csv.writer(datafile)
                print("Create csv writer object.")
                count = 0
                # Filtering out the json response data through loop.
                for data in jsondata['result']['records']:
                    if count == 0:
                        # Loading header for CSV file.
                        header = data.keys()
                        # Writing header of CSV file.
                        csv_wrt.writerow(header)
                        count +=1
                    # Writing data of CSV file
                    csv_wrt.writerow(data.values())
                # Colsing the opened file.
                datafile.close()
                print('completed')                    
        except Exception as e:
            raise e

