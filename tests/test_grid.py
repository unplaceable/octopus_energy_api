# test_capitalize.py

from boggle_solver.grid import Grid

grid_format_2 = [
        ['M','A','P'],
        ['E','T','E'],
        ['D','E','N'],
        
    ]

grid = Grid(existing_array=grid_format_2)


def test_valid_word():
    
    # valid word
    word = 'met'
    result = grid.valid_word(word)
    if result == False:
        raise Exception(f"valid_word returned {result} for {word}.")

    # invalid word
    word='efoiwefoijfowefo'
    result = grid.valid_word(word)
    if result == True:
        raise Exception(f"valid_word returned {result} for {word}.")

def test_get_letter():
    
    # valid letter
    grid_pos = (0,0)
    result = grid.get_letter(grid_pos)
    if result.letter != 'M':
        raise Exception(f"grid_pos returned {result.letter} for {grid_pos}.")

    # invalid letter
    grid_pos = (0,0)
    result = grid.get_letter(grid_pos)
    if result.letter == 'L':
        raise Exception(f"grid_pos returned {result.letter} for {grid_pos}.")




