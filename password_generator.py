#!/usr/bin/env python3
"""安全密码生成器"""

import random
import string


def generate_password(length=16, use_upper=True, use_lower=True,
                      use_digits=True, use_special=True):
    """生成随机密码"""
    characters = ""
    required = []

    if use_lower:
        characters += string.ascii_lowercase
        required.append(random.choice(string.ascii_lowercase))
    if use_upper:
        characters += string.ascii_uppercase
        required.append(random.choice(string.ascii_uppercase))
    if use_digits:
        characters += string.digits
        required.append(random.choice(string.digits))
    if use_special:
        special = "!@#$%^&*()_+-="
        characters += special
        required.append(random.choice(special))

    if not characters:
        return "错误: 至少需要选择一种字符类型"

    remaining = length - len(required)
    if remaining < 0:
        remaining = 0
        required = required[:length]

    password = required + [random.choice(characters) for _ in range(remaining)]
    random.shuffle(password)

    return ''.join(password)


def get_yes_no(prompt):
    """获取是/否输入"""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['y', 'yes', '是']:
            return True
        if answer in ['n', 'no', '否']:
            return False
        print("请输入 y 或 n")


def main():
    """主函数"""
    print("=" * 45)
    print("  安全密码生成器")
    print("=" * 45)

    while True:
        print("\n[选项]")
        print("1. 快速生成 (16位，包含所有字符类型)")
        print("2. 自定义生成")
        print("3. 退出")

        choice = input("\n请选择 (1/2/3): ").strip()

        if choice == '1':
            password = generate_password()
            print(f"\n生成的密码: {password}")
            print(f"密码长度: {len(password)} 位")

        elif choice == '2':
            try:
                length = int(input("密码长度 (8-64): "))
                length = max(8, min(64, length))
            except ValueError:
                length = 16

            use_lower = get_yes_no("包含小写字母? (y/n): ")
            use_upper = get_yes_no("包含大写字母? (y/n): ")
            use_digits = get_yes_no("包含数字? (y/n): ")
            use_special = get_yes_no("包含特殊字符? (y/n): ")

            password = generate_password(length, use_upper, use_lower,
                                         use_digits, use_special)
            print(f"\n生成的密码: {password}")
            print(f"密码长度: {len(password)} 位")

        elif choice == '3':
            print("再见!")
            break
        else:
            print("无效选择，请重试")


if __name__ == "__main__":
    main()
