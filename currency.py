"""
功能:汇率转换程序 v2.0
更新内容: 1.对于输入内容的判断
        2.加入循环
        3.封装函数
"""

aed_vs_rmb = 1.89

#程序入口
in_currency_value = input("请输入带单位的货币金额(退出程序请输入q): ")

while in_currency_value != 'q':

    in_currency = in_currency_value[-3:]

    if in_currency == 'AED':
        # 输入的是迪拉姆
        out_value = eval(in_currency_value[:-3]) * aed_vs_rmb
        print('转换后的金额：', out_value)

    elif in_currency == 'RMB':
        out_value = eval(in_currency_value[:-3]) * 1/aed_vs_rmb
        print('转换后的金额：', out_value)

    else:
        # 其他情况
        print('暂不支持输入的币种和内容')
    in_currency_value = input("请输入带单位的货币金额(退出程序请输入q): ")
    print('********************************************')

print('程序退出,EXIT')



