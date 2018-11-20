"""
功能: 52周存钱挑战
更新: 1.记录每周的金额
"""

def main():
    """
    主函数
    """

    money_per_week = 10     # 每周的存入金额
    i = 1                   # 记录周数
    increase_money = 10     # 递增的金额
    total_week = 52         # 总共的周数
    saving = 0              # 账户累计金额

    while i <= total_week:
        # 存钱操作
        # saving = saving + money_per_week
        saving += money_per_week

        #输出信息
        print('第{}周,存入{}元,账户累计{}元'.format(i,money_per_week,saving))

        # 更新下一周的存钱金额
        money_per_week += increase_money
        i += 1


if __name__ == '__main__':
    main()


