# import libs
import pandas as pd
import requests

# import constants
import src.constants as const


def planilhape(metris_token):

    headers = {
        "Authorization": f"Bearer {metris_token}"
    }

    response = requests.get(const.GAP, headers=headers)
    
    if response.status_code == 200:
        data = pd.DataFrame(response.json())
        print(f"[V - Planilha PE] Data request has succefully")
        return data
    else:
        print(f'[! - Planilha PE] Request Error {response.status_code}')
        return False

