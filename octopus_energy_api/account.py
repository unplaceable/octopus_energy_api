
class account():

    def __init__(self, account_data):
        self.account_data = account_data
        for k, v in account_data.items():
            setattr(self, k, v)

        # setting additional values
        self.mpan = self.properties[0]['electricity_meter_points'][-1]['mpan']
        self.serial_number = self.properties[0]['electricity_meter_points'][-1]['meters'][-1]['serial_number']

    def all_account_data(self):

        return self.account_data

    def get_properties(self):

        return self.properties
