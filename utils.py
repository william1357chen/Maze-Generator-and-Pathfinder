class Cell:
    def __init__(self, idx, rep, coord):
        self.idx = idx
        self.rep = rep
        self.coord = coord

    def __repr__(self) -> str:
        return "Cell (idx={}, rep={}, coords={})".format(
            self.idx, self.rep, self.coord
        )


class DisjointSet:
    def __init__(self):
        self.parent = []  # Cell(idx, rep, coord)

    def find(self, idx):
        if self.parent[idx].rep == idx:
            return self.parent[idx].idx
        else:
            return self.find(self.parent[idx].rep)

    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        self.parent[irep].rep = self.parent[jrep].idx

    def check_rep(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        return self.parent[irep].rep == self.parent[jrep].rep

    def __repr__(self) -> str:
        return str(self.parent)

class CellCoord:
    def __init__(self, col, row) -> None:
        self.col = int(col)
        self.row = int(row)

    def __eq__(self, other):
        if type(other) == tuple:
            return self.col == other[0] and self.row == other[1]
        else:
            return self.col == other.col and self.row == other.row

    def __repr__(self):
        return "CellCoord (col: {}, row: {})".format(self.col, self.row)

class Instruction:
    def __init__(self, node, color, state=None, status=None):
        self.node = node
        self.color = color
        self.state = state
        self.status = status
    def run(self):
        if self.state is not None:
            self.node.state = self.state 
        if self.status is not None:
            self.node.status = self.status 
        self.node.color = self.color

def test():
    hi = DisjointSet()
    hi.parent.append(Cell(0, 0, (10, 10)))
    hi.parent.append(Cell(1, 1, (11, 11)))
    hi.parent.append(Cell(2, 2, (12, 12)))
    print(hi)
    
    hi.union(0, 1)
    print(hi)
    print(hi.find(0))
    print(hi.check_rep(0,1))


if __name__ == '__main__':
    test()