import util.logger as logging
import util.defines as DEFINES
import util.base64Encode as b64
import sys
import yaml
import requests
import json


class SpotifyAPI:

    def __init__(self, configFilePath):

        with open(configFilePath) as file:
            config = yaml.full_load(file)

        # Create Logger
        loggerName = config["loggerName"]
        loggerLevel = config["loggerLevel"]
        self.logger = logging.getLogger(loggerName, loggerLevel)

        # Extract client detais
        self.clientID = config["clientID"]
        self.clientSecret = config["clientSecret"]

        # Get Token
        token, expiresIn = self.GetToken()
    

        self.logger.info("Init Completed")


    # Type: POST
    def GetToken(self):
        self.displayUserAction("Get Token")
        authorization = "{clientID}:{clientSecret}".format(clientID=self.clientID,clientSecret=self.clientSecret)
        b64_client_credentials = b64.encodeMessage(authorization)
        messageHeader = {"Authorization" : f"Basic {b64_client_credentials.decode()}"}
        messageBody = {"grant_type" : "client_credentials"}

        token = None
        expiresIn = None
        response = requests.post(DEFINES.BASE_URL_TOKEN, data=messageBody, headers=messageHeader)
        if response.status_code == DEFINES.API_RESPONSE_OK:
            responseData = response.json()
            token = responseData["access_token"]
            expiresIn = responseData["expires_in"]
            self.logger.info("token:{token}, expires In:{expiresIn}".format(token=token, expiresIn=expiresIn))
        else:
            self.logger.error("Failed to get the token, reason: {reason}".format(reason=response))

        return token, expiresIn
        
    def showClientDetails(self):
        self.displayUserAction("Show Client Details")
        self.logger.info("Client ID: {clientID}".format(clientID=self.clientID))
        self.logger.info("Client Secret: {clientSecret}".format(clientSecret=self.clientSecret))

    def displayUserAction(self, action):
        self.logger.info("==============  {action}  ==============".format(action=action))
        



