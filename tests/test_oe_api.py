from octopus_energy_api.octopus_energy_api import oe_api
from tests.sample_data import sample_account_details, sample_consumption, sample_meter_data
from octopus_energy_api.api_interface import api

from datetime import datetime, timedelta

def test_init(mocker):

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_account_details)
    
    energy_api = oe_api('account_number', 'api_key')

    expected = 'A-123AB123'

    actual = energy_api.account.number

    assert expected == actual

def test_account_details(mocker):

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_account_details)
    energy_api = oe_api('account_number', 'api_key')

    energy_api.account_details()

    expected = 'A-123AB123'

    actual = energy_api.account.number

    assert expected == actual


def test_datetime_conversion(mocker):

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_account_details)
    energy_api = oe_api('account_number', 'api_key')

    assert "2021-06-11T16:30:00" == energy_api.convert_datetime_to_tz(datetime(2021, 6, 11, 16, 30))


def test_consumption(mocker):

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_account_details)
    energy_api = oe_api('account_number', 'api_key')

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_consumption)

    today = datetime.today()
    start = today - timedelta(days=1)

    consumption = energy_api.consumption(start, today)

    assert 0.405 == consumption[0]['consumption']

    # test for failure when time difference too great
    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_account_details)
    energy_api = oe_api('account_number', 'api_key')

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_consumption)

    today = datetime.today()
    start = today - timedelta(days=400)

    try:
        consumption = energy_api.consumption(start, today)
        assert False
    except RuntimeError:
        assert True

def test_consumption_total(mocker):

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_account_details)
    energy_api = oe_api('account_number', 'api_key')

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_consumption)

    today = datetime.today()
    start = today - timedelta(days=1)

    output = energy_api.consumption_total(start, today)

    assert 2.71 == output

def test_consumption_mean(mocker):

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_account_details)
    energy_api = oe_api('account_number', 'api_key')

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_consumption)

    today = datetime.today()
    start = today - timedelta(days=1)

    output = energy_api.consumption_mean(start, today)

    assert 0.18 == output

def test_consumption_median(mocker):

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_account_details)
    energy_api = oe_api('account_number', 'api_key')

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_consumption)

    today = datetime.today()
    start = today - timedelta(days=1)

    output = energy_api.consumption_median(start, today)

    assert 0.082 == output

def test_consumption_cost(mocker):

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_account_details)
    energy_api = oe_api('account_number', 'api_key')

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_consumption)

    today = datetime.today()
    start = today - timedelta(days=1)

    output = energy_api.consumption_cost(start, today, 2.73)

    assert 7.3983 == output

def test_meter_point(mocker):

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_account_details)
    energy_api = oe_api('account_number', 'api_key')

    mocker.patch('octopus_energy_api.api_interface.api.run', return_value=sample_meter_data)

    expected = energy_api.account.mpan

    assert expected == energy_api.meter_point()['mpan']
