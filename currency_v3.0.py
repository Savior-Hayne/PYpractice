"""
功能:汇率转换程序 v3.0
更新内容: 将汇率封装倒函数里
改进准备: 1.迪拉姆vs人民币的汇率,之后需要去网站实时获取
        2.多个汇率
"""
#def main():


def convert_currency(im, er):
    """
    汇率兑换函数
    im: in_money 输入金额
    er: exchange_rate 汇率
    """
    out = im * er
    return out

def main():
    """
    主函数
    """
    #汇率
    aed_vs_rmb = 1.89
    in_currency_value = input("请输入带单位的货币金额: ")
    in_currency = in_currency_value[-3:]

    if in_currency == 'AED':
        exchange_rate = aed_vs_rmb

    elif in_currency == 'RMB':
        exchange_rate = 1 / aed_vs_rmb


    else:
        # 其他情况
        exchange_rate = -1

    if exchange_rate != -1:
        in_money = eval(in_currency_value[:-3])
        out_money = convert_currency(in_money, exchange_rate)
        print('转换后的金额:', out_money)
    else:
        print('不支持该种货币,EXIT')


if __name__ == '__main__':
    main()
