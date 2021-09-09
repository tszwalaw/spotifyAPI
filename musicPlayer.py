import spotifyAPI as spotifyAPI
import sys

def main():

    configFilePath = sys.argv[1]
    
    API = spotifyAPI.SpotifyAPI(configFilePath)
    API.showClientDetails()

    

if __name__ == "__main__":
    main()
