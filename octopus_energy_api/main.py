from octopus_energy_api import oe_api
import datetime

# Controller declarations
api = oe_api(api_key, mpan, serial_number, account_number)

# print(api.GetAccountDetails())

today = datetime.date.today()
start = today.replace(day=1)

print(api.get_consumption(start, today))