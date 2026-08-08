def create_mine_board(grid_size, mine_positions):

    """ 
    This functions is used to creat a mine board
    input:
        grid_size: integer represent the length of the mine board
        mine_position: a list of positions tuple (x,y). x=row, y=column
    return:
        a 2d list mine board which contian -1 represent position of mine 
        and safe cells  around mine will accumulate 1.
    """
    
    # create a 2D list and assign 0 to all position
    board_list = [[0 for x in range(grid_size)] for y in range(grid_size)]

    # put -1 in the position of mine in the board
    for vertical, horizontal in mine_positions:
        board_list[vertical][horizontal] = -1

    # find mines and accumulate 1 to all adjacent num that not equal to -1
    for x in range(grid_size):
        for y in range(grid_size):
            if board_list[x][y] == -1:
                for row in range(x - 1, x + 2):
                    for column in range(y - 1, y + 2):
                        # skip original position with mine
                        if row == x and column == y:
                            continue
                        # if range not out of board, accumulate 1
                        if 0 <= row < grid_size and 0 <= column < grid_size:
                            if board_list[row][column] != -1:
                                board_list[row][column] += 1
    # return 2d list board
    return board_list
