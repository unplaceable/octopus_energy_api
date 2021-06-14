# test_capitalize.py

from boggle_solver.letter import Letter

letterA = Letter('A', (0,0))
letterB = Letter('B', (2,2))


def test_letter():
    
    compare = 'A'
    if letterA.letter != compare:
        raise Exception(f"Returned {letterA.letter} instead of {compare}.")

    compare = 'B'
    if letterB.letter != compare:
        raise Exception(f"Returned {letterA.letter} instead of {compare}.")


def test_grid_pos():

    compare = (0,0)
    if letterA.grid_pos != compare:
        raise Exception(f"Returned {letterA.grid_pos} instead of {compare}.")

    compare = (2,2)
    if letterB.grid_pos != compare:
        raise Exception(f"Returned {letterA.grid_pos} instead of {compare}.")



