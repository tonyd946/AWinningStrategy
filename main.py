input:
    n x n board
    (p,Q)

# take a 2-D array called board, initialized with empty strings
board[n][n]

for (r, c, x) in p:
    board[r][c] = x

    
############################################
# check if Q has a potential winning spot
# block it if one is found
############################################

# check if Q has a potential winning spot along the columns
missing = []  # empty array
for r in [1,2, ... n]:
    for c in [1,2 ... n]:
        if board[r][c] != Q:
            missing.append(c)
    if len(missing) == 1: # Q has a winning spot, block it
        board[r][missing[0]] = P
        return

# check if Q has a potential winning spot along the rows
missing = []  # empty array
for c in [1,2, ... n]:
    for r in [1,2 ... n]:
        if board[r][c] != Q:
            missing.append(c)
    if len(missing) == 1: # Q has a winning spot, block it
        board[missing[0]][c] = P
        return
      
# check if Q has a potential winning spot along the primary diagonal
missing = []  # empty array
for r in [1,2, ... n]:
  if board[r][r] != Q:
    missing.append(c)
  if len(missing) == 1: # Q has a winning spot, block it
    board[missing[0]][missing[0]] = P
    return
  
# check if Q has a potential winning spot along the secondary diagonal
missing = []  # empty array
for r in [1,2, ... n]:
  if board[r][N + 1 - r] != Q:
    missing.append(c)
  if len(missing) == 1: # Q has a winning spot, block it
    board[missing[0]][missing[0]] = P
    return

############################################
# Q doesn't have a potential winning spot
# check if P has a potential winning spot
############################################

# check if P has a potential winning spot along the columns
missing = []  # empty array
for r in [1,2, ... n]:
    for c in [1,2 ... n]:
        if board[r][c] != P:
            missing.append(c)
    if len(missing) == 1: # P has a winning spot, mark it and P wins
        board[r][missing[0]] = P
        return

# check if P has a potential winning spot along the rows
missing = []  # empty array
for c in [1,2, ... n]:
    for r in [1,2 ... n]:
        if board[r][c] != P:
            missing.append(c)
    if len(missing) == 1: # P has a winning spot, mark it and P wins
        board[missing[0]][c] = P
        return
      
# check if P has a potential winning spot along the primary diagonal
missing = []  # empty array
for r in [1,2, ... n]:
  if board[r][r] != P:
    missing.append(c)
  if len(missing) == 1: # P has a winning spot, mark it and P wins
    board[missing[0]][missing[0]] = P
    return
  
# check if P has a potential winning spot along the secondary diagonal
missing = []  # empty array
for r in [1,2, ... n]:
  if board[r][N + 1 - r] != P:
    missing.append(c)
  if len(missing) == 1: # P has a winning spot, mark it and P wins
    board[missing[0]][missing[0]] = P
    return


##########################################################
# At this point neither P nor Q can win in the next turn
# select one unoccupied slot in random and mark it for P
##########################################################

occupied_rows, occupied_cols = [], []
for (r, c, _) in p:
  occupied_rows.append(r)
  occupied_cols.append(c)
  
select r from [1,2 ... n] such that r is not in occupied_rows
select c from [1,2 ... n] such that c is not in occupied_cols

return (r,c, P) # next move for P
