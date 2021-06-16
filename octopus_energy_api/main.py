from octopus_energy_api import oe_api
import os

api_key = os.environ.get('API_KEY')
account_number = os.environ.get('ACCOUNT_NUMBER')

# account_details = oe_api.get_mpan_serial(account_number, api_key)

energy_api = oe_api(account_number, api_key)
print(energy_api.account_details()['properties'][0]['moved_in_at'])

energy_api = oe_api(account_number, api_key, mpan="", serial_number="")
# energy_api.account_details()


print(energy_api.meter_point())

# print(energy_api.account_details())

# CONSUMPTION
# today = datetime.date.today()
# start = today.replace(day=1)

# print(energy_api.consumption(start, today))

# print(energy_api.products())
