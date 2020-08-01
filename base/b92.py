import base64
import base92
import urllib
import re
import binascii

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
            if num_char == 'A':
                num_char = '10'
            elif num_char == 'B':
                num_char = '11'
            elif num_char == 'C':
                num_char = '12'
            elif num_char == 'D':
                num_char = '13'
            elif num_char == 'E':
                num_char = '14'
            elif num_char == 'F':
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

st = "MyU1RCU1Q2FtbldvNCUyOEYlMjMlMjZXYUo0Y3QrayUyMyslMjFEc0Zja0tVNjVHJTVDUGlZWFM0JTI0RmNqdyU1RGE0Y0V6ayUyNSslMjE5JTVCSVFTYWQlM0M0JTIxJTNBZ283WEMzekUlM0UlM0RCJTVEJTVDMyU1REYuayUyNCslMjFVZkdIazNYJTIxNCUyMWhobEkrUi5ISG4lM0QlMjFVNDUlMjdGKmslMjMqbiUzRkFHR2p3WCUyNjQlMjFRJTNEayUyMytCSlRGJTIxU1BhSzRjRXJpWlhkJTNGOUUlM0RrJTNCWCUyNDRCJTVDTG1wWEMzJTdDRiUyM1NQWm80QiUzQW9wJTVEWCUyMy5ESCUyQ2srWCUyODMlNUQlNUNhbW5XbzQlMjhGJTIzJTI2V2FKNGN0K2slMjMrJTIxRHNHR2pvVTY1RyU1Q1BpWVhTNCUyNEZjJTNDdiU1RGE0Y0V6ayUyNSslMjElM0Y5RFhTYWQlM0M0JTIxJTNBZ283WEM0JTIxRSUzRSUzREIlNUQlNUMzJTVERi5rJTI0KyUyMVAlMkNHSGszWCUyMTQlMjFoaG1uV04uSEhuJTNEJTIxVTQ1JTI3RiUyNmxIKm4lM0ZBR0dqd1glMjY0JTIxUSUzRGslMjMrQkpURiUyMVNQYUs0QkY2aVpYZCUzRjlFJTNEayUzQlglMjU0JTIxJTI0NG1wWEMzJTdDRiUyM1NQJTVEJTVDMnklM0FvcCU1RFglMjMuREglMkNrK1psMyU1RCU1Q2FtbldvNCUyOEYlMjMlMjZXUkQ0Y3QrayUyMyslMjFEc0dHandVNjVHJTVDUGlZWFM0JTI0RmQlM0N2JTVEYTRjRXprJTI1KyUyMTklNURFJTNEU2FkJTNDNCUyMSUzQWdvN1hDMyU3Q0UlM0UlM0RCJTVEJTVDMyU1REYuayUyNCslMjFVZkdIazNYJTIxNCUyMWhobW5XJTVFLkhIbiUzRCUyMVU0NSUyN0YlMjZsR1dvJTNGQUdHandYJTI2NCUyMVElM0RvNytCSlRGJTIxU1BhSzRCUTlpWlhkJTNGOUUlM0RrJTNCWCUyNTQlMjEvS21wWEMzJTdDRiUyM1NQWm41aCUzQW9wJTVEWCUyMy5ESCUyQ2srWm0zJTVEJTVDYW1uV280JTI4RiUyMyUyNldVMzRjdCtrJTIzKyUyMURzRmNrU1U2NUclNUNQaVlYUzQlMjZGJTIxJTI2RyU1RGE0Y0V6ayUyNSslMjE5JTVERFhTYWQlM0M0JTIxJTNBZ283WDM0LkUlM0UlM0RCJTVEJTVDMyU1REYuayUyNFglMjMlMjhlR0hrM1glMjE0JTIxaGhsSSpuLkhIbiUzRCUyMVU0NSUyN0YlMjZsSipuJTNGQUdHandYJTI2NCUyMSU1Q1BmaytCSlRGJTIxU1BhSzRCUTFpWlhkJTNGOUUlM0RrJTNCWCUyNDRCRXptcFhDMyU3Q0YlMjNTUCU1RCU1QzQlMjElM0FvcCU1RFglMjMuREglMkNrK1puMyU1RCU1Q2FtbldvNCUyOEYlMjMlMjZXUkQ0Y3QrayUyMyslMjFEc0dHandVNjVHJTVDUGlZWFM0JTI0RiUyNCUyNkclNURhNGNFemslMjUrJTIxJTNGOURYU2FkJTNDNCUyMSUzQWdvN1hDM3pFJTNFJTNEQiU1RCU1QzMlNURGLmslMjRYJTIzLkJHSGszWCUyMTQlMjFoaG1uV04uSEhuJTNEJTIxVTQ1JTI3RiUyNmslMjZXbyUzRkFHR2p3WCUyNjQlMjFROXNLK0JKVEYlMjFTUGFLNEJROWlaWGQlM0Y5RSUzRGslM0JYJTI0NEIlNUNMbXBYQzMlN0NGJTIzU1AlNUQlNUMyeSUzQW9wJTVEWCUyMy5ESCUyQ2szWCUyMTMlNUQlNUNhbW5XbzQlMjhGJTIzJTI2V1glMjE0Y3QrayUyMyslMjFEc0ZkJTI2T1U2NUclNUNQaVlYUzQlMjRGZCUyNkclNURhNGNFemslMjUrJTIxOSU1RERYU2FkJTNDNCUyMSUzQWdvN1hDM3hFJTNFJTNEQiU1RCU1QzMlNURGLmslMjQrMi4="
st = base64.b64decode(st)
st = urllib.unquote(st)
st = base92.b92decode(st)
st = st.decode('hex')
print st
st = re.split(r'%u',st)
dic = {'2648':'0','2649':'1','264A':'2','264B':'3','264C':'4','264D':'5','264E':'6','264F':'7','2650':'8','2651':'9','2652':'A','2653':'B'}
std = ''
for x in range(1,len(st)):
    std+=dic[st[x]]
st = conversion_num(str(std),12,16)
st = re.findall(r'.{2}',st)
sts = ''
for x in range(0,len(st)):
    sts+=binascii.a2b_hex(str(st[x]))
print(base64.b16decode(sts))