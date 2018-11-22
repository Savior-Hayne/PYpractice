"""
功能: 52周存钱挑战
更新: 1.记录每周的金额
     2.改用for循环
     3.可以根据用户自定义每周存入金额,递增金额,总共周数,并封装成函数

"""
import math


def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    """
    计算n周内的存款金额
    """
    money_week_list = []  # 记录每周存款数的列表
    saving = 0              #账户累计总金额

    # while i <= total_week:
    for i in range(total_week):
        # 存钱操作
        # saving = saving + money_per_week
        # saving += money_per_week

        """
        换使用列表来存每周存款数明细,并用来计算计算累计金额
        """
        money_week_list.append(money_per_week)
        saving = math.fsum(money_week_list)

        # 输出信息
        print('第{}周,存入{}元,账户累计{}元'.format(i + 1, money_per_week, saving))

        # 更新下一周的存钱金额
        money_per_week += increase_money

    return saving


def main():
    """
    主函数
    """

    money_per_week = float(input('请输入每周的存入金额:'))     # 每周的存入金额
    increase_money = float(input('请输入每周递增的金额:'))     # 递增的金额
    total_week = int(input('请输入希望存钱的总共周数:'))        # 总共的周数

    #调用函数
    save_money_in_n_weeks(money_per_week, increase_money, total_week)


if __name__ == '__main__':
    main()


