[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

GitHub: [github.com/euanacampbell/octopus_energy_api](https://github.com/euanacampbell/octopus_energy_api)

PyPi: [pypi.org/project/octopus-energy-api](https://pypi.org/project/octopus-energy-api/)

## Installation

```bash
pip install octopus-energy-api
```

## Import

```python
from octopus_energy_api import oe_api
```

## Usage
Two ways of creating an API instance.

#### Load access details in manually - Can be found using this fantastic tutorial by Guy Lipman [guylipman.medium.com](https://guylipman.medium.com/accessing-your-octopus-smart-meter-data-3f3905ca8fec).

```python
from octopus_energy_api import oe_api

account_number = ""
api_key = ""
mpan = ""
serial_number = ""

energy_api = oe_api(account_number, api_key, mpan=mpan, serial_number=serial_number)
```

#### Get mpan and serial numbers from account number + api key. (currently only works for single property accounts)

```python
from octopus_energy_api import oe_api

api_key = "value here"
account_number = "value here"

energy_api = oe_api(account_number, api_key)
```

To confirm this worked, the below can be used. A valid response should be returned.

```python
energy_api.account_details()
```

## Consumption Data

```python
from octopus_energy_api import oe_api
import datetime

energy_api = oe_api(account_number, api_key, mpan=mpan, serial_number=serial_number)

today = datetime.date.today() # setting end date to today
start = today.replace(day=1) # setting start date to the beginning of the month

energy_api.consumption(start, today)
```

## Product Data

```python
from octopus_energy_api import oe_api

energy_api = oe_api(account_number, api_key, mpan=mpan, serial_number=serial_number)

energy_api.products()
```
