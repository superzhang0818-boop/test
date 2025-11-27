#!/usr/bin/env python3
"""石头剪刀布游戏"""

import random


def get_computer_choice():
    """电脑随机选择"""
    return random.choice(['石头', '剪刀', '布'])


def determine_winner(player, computer):
    """判断胜负"""
    if player == computer:
        return 'tie'

    win_conditions = {
        '石头': '剪刀',
        '剪刀': '布',
        '布': '石头'
    }

    if win_conditions[player] == computer:
        return 'player'
    return 'computer'


def play_game():
    """运行游戏"""
    score = {'player': 0, 'computer': 0, 'tie': 0}
    rounds = 0

    print("=" * 40)
    print("  石头剪刀布游戏")
    print("=" * 40)
    print("输入: 1=石头, 2=剪刀, 3=布, q=退出\n")

    choices = {'1': '石头', '2': '剪刀', '3': '布'}

    while True:
        user_input = input("你的选择: ").strip().lower()

        if user_input == 'q':
            break

        if user_input not in choices:
            print("无效输入，请输入 1, 2, 3 或 q\n")
            continue

        player_choice = choices[user_input]
        computer_choice = get_computer_choice()
        rounds += 1

        print(f"\n你出了: {player_choice}")
        print(f"电脑出了: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)

        if result == 'tie':
            print("结果: 平局!")
            score['tie'] += 1
        elif result == 'player':
            print("结果: 你赢了! 🎉")
            score['player'] += 1
        else:
            print("结果: 电脑赢了!")
            score['computer'] += 1

        print(f"比分 - 你: {score['player']} | "
              f"电脑: {score['computer']} | "
              f"平局: {score['tie']}\n")

    # 游戏结束统计
    print("\n" + "=" * 40)
    print("  游戏结束 - 最终统计")
    print("=" * 40)
    print(f"总局数: {rounds}")
    print(f"你赢了: {score['player']} 局")
    print(f"电脑赢了: {score['computer']} 局")
    print(f"平局: {score['tie']} 局")

    if score['player'] > score['computer']:
        print("\n最终结果: 你是赢家! 🏆")
    elif score['computer'] > score['player']:
        print("\n最终结果: 电脑获胜!")
    else:
        print("\n最终结果: 打成平手!")

    print("谢谢游玩!")


if __name__ == "__main__":
    play_game()
