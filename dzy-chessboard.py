#445A

# def change(board,OGchar):
#     if OGchar == 'B':
#         alt="W"
#     else:
#         alt="B"
#
#     for row in range(len(board)):
#         for cell in range(len(board[row])):
#             if board[row][cell]==OGchar:
#                 if cell < len(board[row])-1 and board[row][cell+1]==OGchar:
#                     board[row][cell+1]=alt
#                 elif row < len(board)-1 and board[row+1][cell]==OGchar:
#                     board[row+1][cell]=alt
#                 # if row>0 and board[row-1][cell]==OGchar:
#                 #     board[row-1][cell]=alt
#                 # if cell>0 and board[row][cell-1]==OGchar:
#                 #     board[row][cell-1]=alt


n, m = list(map(int, input().split()))

board = []

for i in range(n):
    s = input()
    board.append([*s])

for row in range(len(board)):
    for col in range(len(board[row])):
        if board[row][col] == '.':
            board[row][col] = 'B'

for row in range(len(board)):
    if row % 2 == 0:
        alt = "W"
    else:
        alt = "B"
    for col in range(len(board[row])):
        if alt == "W":
            alt = "B"
        else:
            alt = "W"
        if board[row][col] != "-":
            board[row][col] = alt

for row in range(len(board)):
    print("".join(board[row]))
