"""
功能: 52周存钱挑战
更新: 1.记录每周的金额
     2.改用for循环
     3.可以根据用户自定义每周存入金额,递增金额,总共周数,并封装成函数
     4.根据用户输入的日期,判断是一年中的第几周,然后输出相应的存款金额

"""
import math
import datetime


def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    """
    计算n周内的存款金额
    """
    money_week_list = []    # 记录每周存款数的列表
    saved_money_list = []   # 记录每周累计存款金额
    # saving = 0              # 账户累计总金额

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
        # 将每周的累计金额都存入列表里
        saved_money_list.append(saving)

        # 输出信息
        print('第{}周,存入{}元,账户累计{}元'.format(i + 1, money_per_week, saving))

        # 更新下一周的存钱金额
        money_per_week += increase_money

    return saved_money_list


def main():
    """
    主函数
    """

    money_per_week = float(input('请输入每周的存入金额:'))     # 每周的存入金额
    increase_money = float(input('请输入每周递增的金额:'))     # 递增的金额
    total_week = int(input('请输入希望存钱的总共周数:'))        # 总共的周数

    # 调用函数
    saved_money_list = save_money_in_n_weeks(money_per_week, increase_money, total_week)
    input_date_str = input('请输入日期(yyyy/mm/dd): ')
    # 讲输入的日期字符串转换成日期格式
    input_date = datetime.datetime.strptime(input_date_str, '%Y/%m/%d')
    # 通过isocalendar函数计算出第几周
    week_num = input_date.isocalendar()[1]
    print('第{}周的存款: {}元'.format(week_num, saved_money_list[week_num - 1]))


if __name__ == '__main__':
    main()


