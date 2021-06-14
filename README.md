[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE) [![boggle_test Actions Status](https://github.com/euanacampbell/boggle_solver/workflows/boggle_test/badge.svg)](https://github.com/euanacampbell/boggle_solver/actions)

GitHub: [github.com/euanacampbell/boggle_solver](https://github.com/euanacampbell/boggle_solver)

PyPi: [pypi.org/project/boggle-solver](https://pypi.org/project/boggle-solver/)

## Installation

```bash
pip3 install boggle-solver
```

## Import

```python
from boggle_solver import *
```

## Usage
Create a 2-dimensional array and pass this into the package.

```python
from boggle_solver import *

grid = [
        ['M','A','P'],
        ['E','T','E'],
        ['D','E','N'],
       ]

boggle=Grid(grid)
```

To confirm this worked, the below function can be used.

```python
boggle.print_grid()

['M', 'A', 'P']
['E', 'T', 'E']
['D', 'E', 'N']
```

Now search for all words. This will take ~20 seconds for a 3x3 grid.

```python
words = boggle.find_all_words()

print(words[:10])

['MEAT', 'MET', 'METED', 'MEET', 'MAT', 'MATE', 'MATED', 'MAP', 'EDEN', 'EAT']
```
