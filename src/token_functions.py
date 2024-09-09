import pickle
from getpass import getpass
from src.metrisapi.account import AccountClient
from src import constants

def read_token():
    """ Get token from pickle file

    Returns:
        string: content of pickle file
    """
    try:
        with open(constants.FILENAME_TOKEN, 'rb') as pickle_file:
            pickle_content = pickle.load(pickle_file)
        return pickle_content
    except:
        print("[!] The token hasn't been created yet")
        return 0

def get_token(base_uri_data):
    """ Save token to pickle file

    Returns:
        string: token string of the saved pickle file
    """
    print("[*] Type your Metris user and password to create a new token")
    ac = AccountClient(base_uri_data)
    metris_token = ac.authenticate(username=getpass("Username: "), password=getpass("Password: "))['id']
    print(metris_token)
    with open(constants.FILENAME_TOKEN, 'wb') as pickle_file:
        pickle.dump(metris_token, pickle_file, pickle.HIGHEST_PROTOCOL)
    
    return metris_token
