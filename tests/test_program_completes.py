# test_capitalize.py

from boggle_solver.grid import Grid

grid_format_2 = [
        ['M','A','P'],
        ['E','T','E'],
        ['D','E','N'],
        
    ]

grid = Grid(existing_array=grid_format_2)

def test_program_completes():

    # Create grid instance
    grid = Grid(existing_array=grid_format_2)

    # Search for all words in the grid
    words = grid.find_all_words()

    # correct number of answers
    no_correct_answers = len(words)
    expected_answer = 46
    if no_correct_answers != expected_answer:
        raise Exception(f"number of answers equals {no_correct_answers} and not {expected_answer}.")