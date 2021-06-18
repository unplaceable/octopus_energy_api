from octopus_energy_api.account import account
from tests.sample_data import sample_account_details



def test_account_loads(mocker):

    # mocker.patch('octopus_energy_api.account.account.__init__', return_value=to_return)
    example_account = account(sample_account_details)
    expected = 'A-123AB123'
    assert expected == example_account.number


def test_all_account_data():

    example_account = account(sample_account_details)

    account_number = example_account.all_account_data()['number']
    
    expected = 'A-123AB123'
    assert expected == account_number


def test_account_properties():

    example_account = account(sample_account_details)
    
    properties = example_account.get_properties()

    property_1_id = properties[0]['id']

    expected = 1234567
    assert expected == property_1_id