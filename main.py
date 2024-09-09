# import constants
import src.constants as const

# import functions
from src.token_functions import *

metris_token = read_token()

if metris_token == 0:
    metris_token = get_token(const.BASE_URI_DATA)
    print("[V] Token successfully created!")
    
else:
    print("[!] Token already created!")