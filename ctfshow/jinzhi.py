# -*- coding: utf-8 -*-
def conversion_num(num, src, dest): #任意进制转换
    rtn = ''
    # 1、校验源（N进制）和目标（M进制）是否相同
    if src == dest:
        rtn = num
    # 2、转成10进制#
    if src != 10:
        num_str = str(num)
        # 将列表翻转
        num_str = num_str[::-1]
        exe_num = 0
        dec_num = 0
        # 从最后一位数开始
        for num_char in num_str:
            # 十六进制处理
            if num_char == 'A' or num_char == 'a':
                num_char = '10'
            elif num_char == 'B' or num_char == 'b':
                num_char = '11'
            elif num_char == 'C' or num_char == 'c':
                num_char = '12'
            elif num_char == 'D' or num_char == 'd':
                num_char = '13'
            elif num_char == 'E' or num_char == 'e':
                num_char = '14'
            elif num_char == 'F'or num_char == 'f':
                num_char = '15'

            num_int = int(num_char)
            if exe_num == 0:
                dec_num += num_int
            else:
                dec_num += src ** exe_num * num_int
            exe_num += 1
        # 得到给定数字的十进制形式
        num = dec_num
    # 3、转成目标进制
    # 判断目标进制是否为十进制
    if dest == 10:
        rtn = num
    else:
        num = int(num)
        while True:
            divisor = num // dest
            remainder = num % dest
            # 十六进制处理
            if remainder == 10:
                remainder = 'A'
            elif remainder == 11:
                remainder = 'B'
            elif remainder == 12:
                remainder = 'C'
            elif remainder == 13:
                remainder = 'D'
            elif remainder == 14:
                remainder = 'E'
            elif remainder == 15:
                remainder = 'F'
            rtn = str(remainder) + rtn
            if divisor <= 0:
                break
            else:
                num = divisor
    # 4、处理空的字符串
    if rtn == '':
        rtn = '0'
    return rtn

st = '0b9b'
ss = 707665719167847083727987956679898393
print(conversion_num(st,16,10))
print(conversion_num(ss,10,16))
