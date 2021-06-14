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
Create an API instance. Access details can be found using this fantastic tutorial by Guy Lipman [guylipman.medium.com](https://guylipman.medium.com/accessing-your-octopus-smart-meter-data-3f3905ca8fec)

```python
from octopus_energy_api import oe_api

api_key = ""
mpan = ""
serial_number = ""
account_number = ""

energy_api = oe_api(api_key, mpan, serial_number, account_number)
```

To confirm this worked, the below function can be used.

```python
energy_api.account_details()
```

## Getting Consumption Data

```python
from octopus_energy_api import oe_api
import datetime

energy_api = oe_api(api_key, mpan, serial_number, account_number)

today = datetime.date.today() # setting end date to today
start = today.replace(day=1) # setting start date to the beginning of the month

energy_api.get_consumption(start, today)
```
