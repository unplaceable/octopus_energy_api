from octopus_energy_api import oe_api
import os
import sys

print('sys args...')
print(sys.argv)

# load from environment variables
api_key = os.environ.get('API_KEY')
account_number = os.environ.get('ACCOUNT_NUMBER')

energy_api = oe_api(account_number, api_key)


def test_account_details():
    expected_output = '020-11-19T00:00:00Z'

    output = energy_api.account_details()['properties'][0]['moved_in_at']
    random=sys.argv[1]
    if output != expected_output:
        raise Exception(f"expected {expected_output}, got {output}. Random: {random}.")



def test_meter_point():
    
    expected_output="{'gsp': '_C', 'mpan': '1200041737043', 'profile_class': 2}"
    
    output = str(energy_api.meter_point())

    if output != expected_output:
        raise Exception(f"expected {expected_output}, got {output}.")