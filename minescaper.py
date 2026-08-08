def create_mine_board(grid_size, mine_positions):

   """
    Create a mine board based on the given mine positions.

    Args:
        grid_size: The size of the square mine board.
        mine_positions: A list of (row, col) tuples representing mine positions.

    Returns:
        A 2D list where mines are represented by -1 and each safe cell
        contains the number of adjacent mines.
    """
    
    # create a 2D list and assign 0 to all position
    board = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

   # Place mines on the board
    for row, col in mine_positions:
        board[row][col] = -1

    # find mines and accumulate 1 to all adjacent num that not equal to -1
    for x in range(grid_size):
        for y in range(grid_size):
            if board[x][y] == -1:
                for row in range(x - 1, x + 2):
                    for column in range(y - 1, y + 2):
                        # skip original position with mine
                        if row == x and column == y:
                            continue
                        # if range not out of board, accumulate 1
                        if 0 <= row < grid_size and 0 <= column < grid_size:
                            if board[row][column] != -1:
                                board[row][column] += 1
    # return 2d list board
    return board
