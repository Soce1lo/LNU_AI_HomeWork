import numpy as np


class DepthFirstSearch:
    def __init__(self, state, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth
        # self.symbol = symbol
        # self.answer = answer

    def get_empty_position(self):
        row, col = np.where(self.state == self.symbol)
        return row, col

    def show_node_info(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i, j], end='  ')
            print("\n")
        print('->')
        return

    def generate_sub_nodes(self):
        sub_nodes = []
        depth = 0
        if self.parent == None:
            depth = 1
        else:
            depth = self.parent.depth + 1
        row, col = self.get_empty_position()
        border_row, border_col = self.state.shape
        border_row -= 1
        border_col -= 1

        if row > 0:
            # 此节点可以生成向上移动的节点
            s = self.state.copy()
            temp = s.copy()
            s[row - 1, col] = s[row, col]
            s[row, col] = temp[row - 1, col]
            sub_nodes.append(DepthFirstSearch(state=s, parent=self, depth=depth))

        if row < border_row:
            # 此节点可以生成向下移动的节点
            s = self.state.copy()
            temp = s.copy()
            s[row + 1, col] = s[row, col]
            s[row, col] = temp[row + 1, col]
            sub_nodes.append(DepthFirstSearch(state=s, parent=self, depth=depth))

        if col > 0:
            # 此节点可以生成向左移动的节点
            s = self.state.copy()
            temp = s.copy()
            s[row, col - 1] = s[row, col]
            s[row, col] = temp[row, col - 1]
            sub_nodes.append(DepthFirstSearch(state=s, parent=self, depth=depth))

        if col < border_col:
            # 此节点可以生成向右移动的节点
            s = self.state.copy()
            temp = s.copy()
            s[row, col + 1] = s[row, col]
            s[row, col] = temp[row, col + 1]
            sub_nodes.append(DepthFirstSearch(state=s, parent=self, depth=depth))
        # 回传倒置的列表
        sub_nodes.reverse()
        return sub_nodes

    def search(self):
        search_table = []
        search_table.append(self)
        while len(search_table):
            temp = search_table.pop(-1)
            path = []
            if temp.depth < self.max_depth:
                if (temp.state == self.answer).all():
                    answer_depth = temp.depth
                    path.append(temp)
                    while temp.parent and temp.parent != self:
                        path.append(temp.parent)
                        temp = temp.parent
                    path.append(self)
                    path.reverse()
                    return path, answer_depth
                search_table.extend(temp.generate_sub_nodes())
            else:
                continue
        else:
            return None
