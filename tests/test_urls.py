from octopus_energy_api.urls import urls
from octopus_energy_api.account import account
from tests.sample_data import sample_account_details



def test_url_build():
    
    # with params
    assert "https://api.octopus.energy/testing" == urls.build_url('/testing')

    # without params
    assert "https://api.octopus.energy/testing/params" == urls.build_url('/testing', '/params')

def test_accounts_url():
    
    assert "https://api.octopus.energy/v1/accounts/AB1234" == urls.accounts_url('AB1234')

def test_products_url():
    
    assert "https://api.octopus.energy/v1/products/?brand=OCTOPUS_ENERGY" == urls.products_url()


def test_consumption_url():
    
    # without page size
    assert "https://api.octopus.energy/v1/electricity-meter-points/mpan/meters/serial/consumption?page_size=25000&period_from=start&period_to=end&order_by=period" == urls.consumption_url('mpan', 'serial', 'start', 'end')

    # with page size
    assert "https://api.octopus.energy/v1/electricity-meter-points/mpan/meters/serial/consumption?page_size=10000&period_from=start&period_to=end&order_by=period" == urls.consumption_url('mpan', 'serial', 'start', 'end', page_size=10000)

def test_meter_point_url():
    
    assert "https://api.octopus.energy/v1/electricity-meter-points/mpan/" == urls.meter_point_url('mpan')