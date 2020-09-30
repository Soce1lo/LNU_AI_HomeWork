"""
version:python3.7
author:BHR
"""

import numpy as np

from BreadFirstSearch import BreadFirstSearch
from DepthFirstSearch import DepthFirstSearch


# 广度优先搜索
def bread_first_search(symbol_of_empty, original_state_node, target_state_node, max_width):
    # 将空白标识赋给搜索方法类
    BreadFirstSearch.symbol = symbol_of_empty
    # 为搜索方法类设置最大宽度
    BreadFirstSearch.max_width = max_width

    # 设置类目标状态
    BreadFirstSearch.answer = target_state_node
    s = BreadFirstSearch(state=original_state_node)
    path = s.search()
    if path != None:
        print('此问题可解')
        print('变化过程为：')
        for i in path:
            i.show_node_info()
    else:
        print('此问题在当前空间限制下无解')


# 深度优先搜索
def depth_first_search(symbol_of_empty, original_state_node, target_state_node, max_depth):
    # 将空白标识赋给类
    DepthFirstSearch.symbol = symbol_of_empty

    # 设定目标状态
    DepthFirstSearch.answer = target_state_node
    # 设置搜索类最大深度
    DepthFirstSearch.max_depth = max_depth

    s = DepthFirstSearch(state=original_state_node)
    path, answer_depth = s.search()
    if path != None:
        print('此问题可解，目标状态所在深度为%d' % (answer_depth))
        print('变化过程为：')
        for i in path:
            i.show_node_info()
    else:
        print('此问题在当前深度限制下不存在可行解')


if __name__ == '__main__':
    # 定义空白标识
    symbol_of_empty = ' '
    # 设置起始状态
    original_state_node = np.array([[2, 8, 3], [1, 6, 4], [7, symbol_of_empty, 5]])
    # 设置目标状态
    target_state_node = np.array([[1, 2, 3], [8, symbol_of_empty, 4], [7, 6, 5]])

    # 进行广度优先搜索
    max_width = 10000
    bread_first_search(symbol_of_empty, original_state_node, target_state_node, max_width)

    # 设定深度优先搜索最大深度
    max_depth = 5
    depth_first_search(symbol_of_empty, original_state_node, target_state_node, max_depth)
