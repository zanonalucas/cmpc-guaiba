import pandas as pd
import requests
from datetime import datetime, timedelta

import src.constants as const 

def get_spc_treemap(metris_token):
    '''
    Get the OEE KPI Historical JSON.
    '''

    #try:
    bearer_auth = {'Authorization': 'Bearer ' + metris_token}

    df_list = list()

    # Limita dados de um mês.
    # for i in range(1, 32):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    parameters = dict()
    parameters['start'] = start_date
    parameters['end'] = end_date
    response = requests.get(url=const.SPC_TREEMAP_ENDPOINT, params=parameters, headers=bearer_auth, verify=False)

    if response.status_code == 200:
        df_list.append(pd.DataFrame(response.json()))

    elif response.status_code == 404:
        print('Not Found.')
        return False

    else:
        print("Status Error: " + str(response.status_code))
        return False
        
    # except Exception as e:
        # return False

    df = pd.concat(df_list)

    return df

def get_spc(metris_token):
    '''
    Get the OEE KPI Historical JSON.
    '''

    #try:
    bearer_auth = {'Authorization': 'Bearer ' + metris_token}

    df_list = list()

    # Limita dados de um mês.
    # for i in range(1, 32):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=520)
    parameters = dict()
    parameters['start'] = start_date
    parameters['end'] = end_date
    response = requests.get(url=const.SPC_TREEMAP_ENDPOINT, params=parameters, headers=bearer_auth, verify=False)

    if response.status_code == 200:
        df_list.append(pd.DataFrame(response.json()))

    elif response.status_code == 404:
        print('Not Found.')
        return False

    else:
        print("Status Error: " + str(response.status_code))
        return False
        
    # except Exception as e:
        # return False

    df = pd.concat(df_list)

    return df