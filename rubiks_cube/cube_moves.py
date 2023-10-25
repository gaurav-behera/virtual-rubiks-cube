import copy
import random


def white_cw(pos):
    res = copy.deepcopy(pos)
    res[5][3], res[5][5], res[5][6], res[5][8], res[5][9], res[5][11], res[5][0], res[5][2] = \
        pos[5][0], pos[5][2], pos[5][3], pos[5][5], pos[5][6], pos[5][8], pos[5][9], pos[5][11]
    res[5][4], res[5][7], res[5][10], res[5][1] = pos[5][1], pos[5][4], pos[5][7], pos[5][10]
    res[6][3], res[6][5], res[8][5], res[8][3] = pos[8][3], pos[6][3], pos[6][5], pos[8][5]
    res[6][4], res[7][5], res[8][4], res[7][3] = pos[7][3], pos[6][4], pos[7][5], pos[8][4]
    return res


def yellow_cw(pos):
    res = copy.deepcopy(pos)
    res[3][11], res[3][9], res[3][8], res[3][6], res[3][5], res[3][3], res[3][2], res[3][0] = \
        pos[3][2], pos[3][0], pos[3][11], pos[3][9], pos[3][8], pos[3][6], pos[3][5], pos[3][3]
    res[3][10], res[3][7], res[3][4], res[3][1] = pos[3][1], pos[3][10], pos[3][7], pos[3][4]
    res[0][3], res[0][5], res[2][5], res[2][3] = pos[2][3], pos[0][3], pos[0][5], pos[2][5]
    res[0][4], res[1][5], res[2][4], res[1][3] = pos[1][3], pos[0][4], pos[1][5], pos[2][4]
    return res


def blue_cw(pos):
    res = copy.deepcopy(pos)
    res[0][5], res[0][3], res[3][0], res[5][0], res[8][3], res[8][5], res[5][8], res[3][8] = \
        pos[5][8], pos[3][8], pos[0][5], pos[0][3], pos[3][0], pos[5][0], pos[8][3], pos[8][5]
    res[0][4], res[4][0], res[8][4], res[4][8] = pos[4][8], pos[0][4], pos[4][0], pos[8][4]
    res[3][9], res[3][11], res[5][11], res[5][9] = pos[5][9], pos[3][9], pos[3][11], pos[5][11]
    res[3][10], res[4][11], res[5][10], res[4][9] = pos[4][9], pos[3][10], pos[4][11], pos[5][10]
    return res


def green_cw(pos):
    res = copy.deepcopy(pos)
    res[2][3], res[2][5], res[3][6], res[5][6], res[6][5], res[6][3], res[5][2], res[3][2] = \
        pos[5][2], pos[3][2], pos[2][3], pos[2][5], pos[3][6], pos[5][6], pos[6][5], pos[6][3]  # outer corners
    res[2][4], res[4][6], res[6][4], res[4][2] = pos[4][2], pos[2][4], pos[4][6], pos[6][4]  # outer edges
    res[3][3], res[3][5], res[5][5], res[5][3] = pos[5][3], pos[3][3], pos[3][5], pos[5][5]  # surface corners
    res[3][4], res[4][5], res[5][4], res[4][3] = pos[4][3], pos[3][4], pos[4][5], pos[5][4]  # surface edges
    return res


def red_cw(pos):
    res = copy.deepcopy(pos)  # to avoid aliasing
    res[0][3], res[2][3], res[3][3], res[5][3], res[6][3], res[8][3], res[5][11], res[3][11] = \
        pos[5][11], pos[3][11], pos[0][3], pos[2][3], pos[3][3], pos[5][3], pos[6][3], pos[8][3]
    res[1][3], res[4][3], res[7][3], res[4][11] = pos[4][11], pos[1][3], pos[4][3], pos[7][3]
    res[3][0], res[3][2], res[5][2], res[5][0] = pos[5][0], pos[3][0], pos[3][2], pos[5][2]
    res[3][1], res[4][2], res[5][1], res[4][0] = pos[4][0], pos[3][1], pos[4][2], pos[5][1]
    return res


def orange_cw(pos):
    res = copy.deepcopy(pos)
    res[2][5], res[0][5], res[3][9], res[5][9], res[8][5], res[6][5], res[5][5], res[3][5] = \
        pos[5][5], pos[3][5], pos[2][5], pos[0][5], pos[3][9], pos[5][9], pos[8][5], pos[6][5]
    res[1][5], res[4][9], res[7][5], res[4][5] = pos[4][5], pos[1][5], pos[4][9], pos[7][5]
    res[3][6], res[3][8], res[5][8], res[5][6] = pos[5][6], pos[3][6], pos[3][8], pos[5][8]
    res[3][7], res[4][8], res[5][7], res[4][6] = pos[4][6], pos[3][7], pos[4][8], pos[5][7]
    return res


def white_acw(pos):
    res = white_cw(white_cw(white_cw(pos)))
    return res


def yellow_acw(pos):
    res = yellow_cw(yellow_cw(yellow_cw(pos)))
    return res


def blue_acw(pos):
    res = blue_cw(blue_cw(blue_cw(pos)))
    return res


def green_acw(pos):
    res = green_cw(green_cw(green_cw(pos)))
    return res


def red_acw(pos):
    res = red_cw(red_cw(red_cw(pos)))
    return res


def orange_acw(pos):
    res = orange_cw(orange_cw(orange_cw(pos)))
    return res


def white_x2(pos):
    res = white_cw(white_cw(pos))
    return res


def yellow_x2(pos):
    res = yellow_cw(yellow_cw(pos))
    return res


def blue_x2(pos):
    res = blue_cw(blue_cw(pos))
    return res


def green_x2(pos):
    res = green_cw(green_cw(pos))
    return res


def red_x2(pos):
    res = red_cw(red_cw(pos))
    return res


def orange_x2(pos):
    res = orange_cw(orange_cw(pos))
    return res


def scramble_cube():
    global pos
    count = 0
    output = []
    prev = "  "
    pos = copy.deepcopy(solved_state)

    while count < 20:
        i = random.randrange(18)
        if moves[i][0] != prev[0]:
            output.append([moves[i]])
            prev = moves[i]
            pos = eval(standard_moves[moves[i]])
            count += 1
    return output, pos


solved_state = [[' ', ' ', ' ', 'y', 'y', 'y', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', 'y', 'y', 'y', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', 'y', 'y', 'y', ' ', ' ', ' ', ' ', ' ', ' '],
                ['r', 'r', 'r', 'g', 'g', 'g', 'o', 'o', 'o', 'b', 'b', 'b'],
                ['r', 'r', 'r', 'g', 'g', 'g', 'o', 'o', 'o', 'b', 'b', 'b'],
                ['r', 'r', 'r', 'g', 'g', 'g', 'o', 'o', 'o', 'b', 'b', 'b'],
                [' ', ' ', ' ', 'w', 'w', 'w', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', 'w', 'w', 'w', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', 'w', 'w', 'w', ' ', ' ', ' ', ' ', ' ', ' ']]

standard_moves = {"L": "red_cw(pos)", "R": "orange_cw(pos)", "F": "green_cw(pos)", "B": "blue_cw(pos)",
                  "U": "yellow_cw(pos)", "D": "white_cw(pos)", "L'": "red_acw(pos)", "R'": "orange_acw(pos)",
                  "F'": "green_acw(pos)", "B'": "blue_acw(pos)", "U'": "yellow_acw(pos)", "D'": "white_acw(pos)",
                  "L2": "red_x2(pos)", "R2": "orange_x2(pos)", "F2": "green_x2(pos)", "B2": "blue_x2(pos)",
                  "U2": "yellow_x2(pos)", "D2": "white_x2(pos)"}
moves = list(standard_moves.keys())
