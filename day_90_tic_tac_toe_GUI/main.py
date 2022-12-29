# game_on = True
row1 = ["1", "2", "3"]
row2 = ["4", "5", "6"]
row3 = ["7", "8", "9"]


# piece = ["X", "O"]

def mark_point(box, piece):
    box = box + 1
    if box < 4:
        row1[box-1] = piece
        # row1.insert(box-1, piece)
    elif box > 3 and box <7 :
        # row2.insert(box - 4 , piece)
        row2[box-4] = piece
    elif box > 6 and box <10 :
        row3[box-7] = piece
        # row3.insert(box - 7, piece)
    # print(boxes)

def add_row(rows, i):
    if i == 1: return [rows[0][0] , rows[1][0] , rows[2][0]]
    if i == 2: return [rows[0][1] , rows[1][1] , rows[2][1]]
    if i == 3: return [rows[0][2] , rows[1][2] , rows[2][2]]
    if i == 4: return [rows[0][0] , rows[1][1] , rows[2][2]]
    if i == 5: return [rows[0][2] , rows[1][1] , rows[2][0]]

def get_winner(player, piece):
    # winning logic
    # these are all the lines of three which determine a winner
    rows = [row1, row2, row3]
    # print(rows)
    for i in range(1,6):
        try:
            new_row = add_row(rows,i)
            # print(i, new_row)
            rows.append(new_row)
        except Exception as e:
            print(i,e)
    # print("Getting Winner...")
    for row in rows:
        if len(row) == 3:
            print(row , len(set(row)))
            if len(set(row)) == 1:
                # print(f"{player} of {piece} won!")
                return player
            # else:
    return None




