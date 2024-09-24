import unittest

def rotate(x: int) -> int: 
    return (x>>1) + (x%2)*8

def neighbors(i: int, j: int, pipe: int) -> set[tuple[int, int]]:
    r=set()
    up = 0b1000
    right = 0b0100
    down = 0b0010
    left = 0b0001
    if(up & pipe):
        r.add((i-1,j))
    if(down & pipe):
        r.add((i+1,j))
    if(right & pipe):
        r.add((i,j+1))
    if(left & pipe):
        r.add((i,j-1))
    return r


def is_valid_solution(solution: list[list[int]]) -> bool:
    pred: dict[tuple[int,int], tuple[int, int]] = dict()
    visited: set[tuple[int, int]] = set()
    q: list[tuple[int, int] ]= [(0,0)]
    while(len(visited)<16 and q):
        current_x, current_y = q.pop(0)
        for neighbor in neighbors(current_x, current_y, solution[current_x][current_y]):
            if(neighbor[0]<0 or neighbor[0]>3 or neighbor[1]<0 or neighbor[1]>3):
                return False
            if(neighbor == pred.get((current_x, current_y))):
                continue
            if(neighbor in visited):
                print("ya visitado")
                print(f"current: ({current_x},{current_y})")
                print(f"neighbor: ({neighbor[0]},{neighbor[1]})")
                print(f"pred: ({pred[(current_x, current_y)]})")
                return False
            
            q.append(neighbor)
            pred[neighbor] = (current_x, current_y)
        
        visited.add((current_x, current_y))
    return len(visited)==16

class TestPipesGame(unittest.TestCase):
    def test_neighbors(self):
        result = neighbors(0, 0, 0b0110)
        expected = {(1, 0), (0, 1)}
        assert result == expected
    
    def test_neighbors2(self):
        result = neighbors(0, 1, 0b0101)
        expected = {(0, 0), (0, 2)}
        assert result == expected

    
    def test_solved_game_returns_true(self):
        game = [
            [0b0110, 0b0101, 0b0001, 0b0010],
            [0b1110, 0b0101, 0b0101, 0b1011],
            [0b0010, 0b0110, 0b0111, 0b1001],
            [0b0100, 0b1001, 0b1100, 0b0001],
                ]
        
        result = is_valid_solution(game)
        assert result == True

    def test_unsolved_game_returns_true(self):
        game = [
            [0b0000, 0b0000, 0b0000, 0b0000],
            [0b0000, 0b0000, 0b0000, 0b0000],
            [0b0000, 0b0000, 0b0000, 0b0000],
            [0b0000, 0b0000, 0b0000, 0b0000],
                ]
        assert not is_valid_solution(game)

if __name__ == "__main__":
    unittest.main()

