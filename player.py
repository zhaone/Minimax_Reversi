#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 


class Player(object):
    """
    玩家基类
    """

    def __init__(self, color=None):
        """
        获取当前玩家状态
        :param color: 如果 color=='X',则表示是黑棋一方; color=='O'，则表示白棋一方。
        """
        self.color = color

    def get_move(self, board):
        """
        根据当前棋盘获取最佳落子位置坐标
        :param board: 当前棋盘
        :return: 落子位置坐标
        """
        pass

    def move(self, board, action):
        """
        落下棋子，根子落下的棋子坐标获取反转棋子的坐标列表
        :param board: 棋盘
        :param action: 落下棋子的坐标
        :return: 反转棋子的坐标列表
        """
        flipped_pos = board._move(action, self.color)
        return flipped_pos
