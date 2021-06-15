from octopus_energy_api import oe_api
import datetime

api_key = ""
account_number = ""

# account_details = oe_api.get_mpan_serial(account_number, api_key)

energy_api = oe_api(account_number, api_key)
energy_api.account_details()

energy_api = oe_api(account_number, api_key, mpan="", serial_number="")
energy_api.account_details()

# print(energy_api.account_details())

# CONSUMPTION
# today = datetime.date.today()
# start = today.replace(day=1)

# print(energy_api.consumption(start, today))

# print(energy_api.products())
