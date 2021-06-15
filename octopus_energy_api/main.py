from octopus_energy_api import oe_api
import datetime

api_key = ""
account_number = ""

account_details = oe_api.get_mpan_serial(account_number, api_key)

mpan = account_details['mpan']
serial_number = account_details['serial_numbers'][1]

api = oe_api(api_key=api_key, mpan=mpan, serial_number=serial_number, account_number=account_number)

# print(api.account_details())

# CONSUMPTION
today = datetime.date.today()
start = today.replace(day=1)

print(api.get_consumption(start, today))
