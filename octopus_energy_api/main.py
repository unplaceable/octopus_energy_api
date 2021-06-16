from octopus_energy_api import oe_api
import datetime
import os

api_key = os.environ.get('API_KEY')
account_number = os.environ.get('ACCOUNT_NUMBER')

energy_api = oe_api(account_number, api_key)
# print(energy_api.account_details()['properties'][0]['moved_in_at'])

today = datetime.date.today()
start = today.replace(day=1)

energy_api.consumption_total(start, today)

energy_api.consumption_mean(start, today)

energy_api.consumption_median(start, today)


# print(energy_api.account_details())

# CONSUMPTION
# today = datetime.date.today()
# start = today.replace(day=1)

# print(energy_api.consumption(start, today))

# print(energy_api.products())
