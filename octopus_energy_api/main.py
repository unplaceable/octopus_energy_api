from octopus_energy_api import oe_api
from datetime import datetime, timedelta
import os

api_key = os.environ.get('API_KEY')
account_number = os.environ.get('ACCOUNT_NUMBER')

energy_api = oe_api(account_number, api_key)
# print(energy_api.account_details())


today = datetime.today()
start = today - timedelta(days=300)


print(energy_api.consumption_total(start, today))

print(energy_api.consumption_mean(start, today))

print(energy_api.consumption_median(start, today))

print(energy_api.consumption_cost(start, today, 2.73))


# print(energy_api.account_details())

# CONSUMPTION
# today = datetime.date.today()
# start = today.replace(day=1)

# print(energy_api.consumption(start, today))

# print(energy_api.products())
