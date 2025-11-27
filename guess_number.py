#!/usr/bin/env python3
"""简单的猜数字游戏"""

import random


def play_game():
    """运行猜数字游戏"""
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("=" * 40)
    print("  欢迎来到猜数字游戏!")
    print("=" * 40)
    print(f"我想了一个 1-100 之间的数字")
    print(f"你有 {max_attempts} 次机会猜中它\n")

    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts

        try:
            guess = int(input(f"第 {attempts} 次猜测: "))
        except ValueError:
            print("请输入一个有效的数字!\n")
            attempts -= 1
            continue

        if guess < 1 or guess > 100:
            print("请输入 1-100 之间的数字!\n")
            attempts -= 1
            continue

        if guess == secret:
            print(f"\n恭喜你猜对了! 答案就是 {secret}")
            print(f"你用了 {attempts} 次就猜中了!")
            return True
        elif guess < secret:
            print(f"太小了! 还剩 {remaining} 次机会\n")
        else:
            print(f"太大了! 还剩 {remaining} 次机会\n")

    print(f"\n游戏结束! 正确答案是 {secret}")
    return False


def main():
    """主函数"""
    while True:
        play_game()
        print("\n" + "-" * 40)
        again = input("再玩一次吗? (y/n): ").strip().lower()
        if again != 'y':
            print("谢谢游玩, 再见!")
            break
        print()


if __name__ == "__main__":
    main()
