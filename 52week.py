"""
功能: 52周存钱挑战
更新: 1.记录每周的金额
     2.改用for循环
"""
import math
def main():
    """
    主函数
    """

    money_per_week = 10     # 每周的存入金额
    #i = 1                   # 记录周数
    increase_money = 10     # 递增的金额
    total_week = 52         # 总共的周数
    saving = 0              # 账户累计金额
    money_week_list = []    # 记录每周存款数的列表

    #while i <= total_week:
    for i in range(total_week):
        # 存钱操作
        # saving = saving + money_per_week
        # saving += money_per_week
        """
        换使用列表来存每周存款数明细,并用来计算计算累计金额
        """
        money_week_list.append(money_per_week)
        saving = math.fsum(money_week_list)


        #输出信息
        print('第{}周,存入{}元,账户累计{}元'.format(i+1,money_per_week,saving))

        # 更新下一周的存钱金额
        money_per_week += increase_money
        #i += 1


if __name__ == '__main__':
    main()


