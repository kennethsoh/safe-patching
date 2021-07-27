'''                                                                                   
File Name       : proxy.py                                                            
Author          : Kenneth Soh                                                         
Date created    : 29 June 2021                                                        
'''                                                                                   
                                                                                      
                                                                                      
import os                                                                             
import sys                                                                            
import json                                                                           
import time                                                                           
import requests                                                                       
from vtapi3 import VirusTotalAPIFiles, VirusTotalAPIError, VirusTotalAPIAnalyses      

apikey = "<insert api key>" # Insert your VirusTotal API key here
                                                                                      
class Device:                                                                         
    def __init__(self, url, signature, updateurl):                                    
        self.url = url                                                                
        self.signature = signature                                                    
        self.updateurl = updateurl                                                    
                                                                                      
    def info(self):                                                                   
        print(f"Mud URL       : {self.url}")                                          
        print(f"Mud Signature : {self.signature}")                                    
        print(f"Mud updateurl : {self.updateurl}")

    def getFirmware(self):                                                            
                                                                                      
        # Download firmware file                                                      
        r = requests.get(self.updateurl)                                              
        print(f"[INFO] Downloading firmware file from {self.updateurl} .")
        with open(f'/proxy/files/{updatefilename}', 'wb') as f:
            f.write(r.content)

        # Upload File to VirusTotal for analysis
        vt_files = VirusTotalAPIFiles(apikey)  
        try:
            print(f"[INFO] Uploading '/proxy/files/{updatefilename}' to VirusTotal for
 checks.")           
            os.chdir("/proxy/files")
            upload = vt_files.upload(f"{updatefilename}")
            os.chdir("/proxy")
        except VirusTotalAPIError as error: 
            print(f"Upload Error {error, error.err_code}")
        else:
            if vt_files.get_last_http_error() == vt_files.HTTP_OK:
                uploadresult = json.loads(upload)

                # Obtain file id from uploadresult
                uploadid = uploadresult["data"]["id"]

                # Send file id for analysis 
                vt_analyses = VirusTotalAPIAnalyses(apikey)
                try:
                    analyse = vt_analyses.get_report(f'{uploadid}')
                except VirusTotalAPIError as err:
                    print(err, err.err_code)
                else: 
                    if vt_analyses.get_last_http_error() == vt_analyses.HTTP_OK:
                        analyseresult = json.loads(analyse)
                        #analyseresult = json.dumps(analyseresult, sort_keys=False, indent=4)   # (DO NOT SORT)                  
                                           
                        # Check if file is flagged as malicious or suspicious and delete file if malicious or suspicious         
                        if (analyseresult["data"]["attributes"]["stats"]["malicious"] > 0 or analyseresult["data"]["attributes"]["stats"]["suspicious"] > 0):               
                            print(f"[WARNING] '{updatefilename}' is a malicious/suspicious file, it will be deleted.")           
                            os.chdir("/proxy/files")
                            os.remove(f"{updatefilename}")
                            os.remove(f"{filename}.json")
                            print(f"[INFO] '{updatefilename}' and '{filename}.json' has been deleted from {os.uname()[1]}.")     
                        else:
                            print(f"[INFO] '{updatefilename}' is safe for use. It willbe saved at: '/proxy/files/{updatefilename}.'")                                      
                    else:
                        sys.exit('HTTP Error [' + str(vt_analyses.get_last_http_error()) +']')             
            else:
                sys.exit('HTTP Error [' + str(vt_files.get_last_http_error()) +']')
                  
if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('You need to specify the json file to be read')
    file = (sys.argv[1])[6:]
    f = open('/proxy/files/'+file)
    data = json.load(f)
    mud = data['ietf-mud:mud']
    try:
        device = Device(mud["mud-url"], mud["mud-signature"], mud["mud-updateurl"])

        filename = file.rstrip('.json')
        updatefilename = filename + str((os.path.splitext(device.updateurl))[1])

        device.getFirmware()
    except:
        sys.exit("An error has occured with the mudfile. Please check.")      
                                                                                                 
                                                    
