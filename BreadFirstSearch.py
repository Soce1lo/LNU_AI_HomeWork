import numpy as np


class BreadFirstSearch:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
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
            sub_nodes.append(BreadFirstSearch(state=s, parent=self))

        if row < border_row:
            # 此节点可以生成向下移动的节点
            s = self.state.copy()
            temp = s.copy()
            s[row + 1, col] = s[row, col]
            s[row, col] = temp[row + 1, col]
            sub_nodes.append(BreadFirstSearch(state=s, parent=self))

        if col > 0:
            # 此节点可以生成向左移动的节点
            s = self.state.copy()
            temp = s.copy()
            s[row, col - 1] = s[row, col]
            s[row, col] = temp[row, col - 1]
            sub_nodes.append(BreadFirstSearch(state=s, parent=self))

        if col < border_col:
            # 此节点可以生成向右移动的节点
            s = self.state.copy()
            temp = s.copy()
            s[row, col + 1] = s[row, col]
            s[row, col] = temp[row, col + 1]
            sub_nodes.append(BreadFirstSearch(state=s, parent=self))
        return sub_nodes

    def search(self):
        # 保存待搜索节点
        opean_table = []
        opean_table.append(self)
        while len(opean_table):
            path = []
            temp = opean_table.pop(0)
            if len(opean_table) > self.max_width:
                return None
            if (temp.state == self.answer).all():
                path.append(temp)
                while temp.parent and temp.parent != self:
                    path.append(temp.parent)
                    temp = temp.parent
                path.append(self)
                path.reverse()
                return path
            opean_table.extend(temp.generate_sub_nodes())
        else:
            return None
