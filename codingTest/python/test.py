import copy

total_map = []

def make_map(i, j, grid):
    global total_map
    while True:
        print(i, j)
        if j == len(grid[0]):
            if i == len(grid) - 1:
                total_map.append(grid)
                break
            i += 1
            j = 0
        if grid[i][j] == '?':
            make_map(i, j + 1, copy_and_append(grid, i, j, 'a'))
            make_map(i, j + 1, copy_and_append(grid, i, j, 'b'))
            make_map(i, j + 1, copy_and_append(grid, i, j, 'c'))
            break
        else:
            j += 1

def copy_and_append(grid, i, j, alph):
    copy_grid = copy.deepcopy(grid)
    tmp = list(copy_grid[i])
    tmp[j] = alph
    tmp_str = "".join(tmp)
    copy_grid[i] = tmp_str
    return copy_grid

def solution(grid):
    answer = -1
    make_map(0, 0, grid)
    print(total_map)
    return answer

print(solution(["aa?"]))