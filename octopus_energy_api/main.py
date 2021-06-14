from octopus_energy_api import oe_api
import datetime

# Controller declarations
api = oe_api(api_key, mpan, serial_number, account_number)

# print(api.GetAccountDetails())

today = datetime.date.today()
start = today.replace(day=1)

print(api.get_consumption(start, today))






"""
data = database()

# Get last updated time for spreadsheet
last_updated = data.get_highest_interval_start()
last_updated = last_updated + datetime.timedelta(minutes = 30)
last_updated = data.convert_datetime(last_updated, output_type='tz')

# Call OE API to get all updates since then
end_time = data.convert_datetime(datetime.datetime.now(), output_type='tz')
output = api.get_consumption(last_updated, end_time)

# Upload data
if len(output)==0:
    print("no new data")

for row in output:
    print(f"{row['interval_start']} uploaded")
    new_row = []

    new_row.append(data.convert_datetime(row['interval_start'], input_type='tz', output_type='sheets'))
    new_row.append(data.convert_datetime(row['interval_end'], input_type='tz', output_type='sheets'))
    new_row.append(row['consumption'])
    
    start_day=data.convert_datetime(row['interval_start'], input_type='tz').strftime('%A')
    new_row.append(start_day)

    data.upload_row(new_row)
    time.sleep(2)"""
