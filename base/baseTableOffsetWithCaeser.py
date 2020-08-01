###!/usr/bin/python

# by FlyingMcDonald
# https://github.com/FlyingMcDonald

import sys, getopt

#用于base64加密，获取待加密字符串的二进制值
def getBinaryStr_encode(Str):
    binaryStr=''
    for a in Str:
        #ord()用于获取字符的ASCII码，bin()用于将ASCII码转为二进制
        binary = bin(ord(a)).replace('0b', '')
        #如果binary长度小于八位，在前面补0
        while len(binary) < 8:
            binary='0'+binary
        
        #将每个字符的二进制串进行拼接，连接为一个大的二进制串
        binaryStr+=binary
    return binaryStr

#用于base64加密，将传入的二进制串按每6位进行分割，然后存入一个列表中
def subBinaryStr_encode(binaryStr):
    strList = []

    #若二进制串不为6的倍数，在后面补0
    while len(binaryStr)%6 != 0:
        binaryStr+='0'
    
    #将二进制串进行分割
    for num in range(0,int(len(binaryStr)/6)):
        index = num*6   #起始截取索引
        sub = (num+1)*6 #结束截取索引
        strList.insert(num, binaryStr[index:sub])
    return strList

#base64加密
def encode(Str, baseTable):
    base64Str = ''
    binaryStr = getBinaryStr_encode(Str) #获取二进制串
    strList = subBinaryStr_encode(binaryStr) #获取列表

    #当列表长度不能整除3时，在列表后面补=号
    while len(strList)%3 != 0:
        strList.append('=')

    #遍历列表
    for a in range(len(strList)):
        if strList[a] != '=':

            #当元素小于八位，在前面补0
            while len(strList[a]) < 8:
                strList[a]='0'+strList[a]
            
            #获取加密后的字符串，int(strList[a], 2)在这里将二进制转为十进制
            #然后按照编码表来获取相应字符，再将每个字符拼接
            base64Str += baseTable[int(strList[a], 2)]
        else:
            base64Str+='='
    # print(base64Str)
    return base64Str

#用于base64解密， 获取密文的二进制字符串
def getBinaryStr_decode(Str, baseTable):
    realStrBinary = ''
    Str = Str.replace('=', '')
    for char in Str:

        #获取该字符在编码表中的索引
        for index in range(len(baseTable)):
            if baseTable[index] == char:
                # 将索引转化为二进制串
                binary = bin(index).replace('0b', '')
                #若二进制串不足6位，在前面补0
                while len(binary) != 6:
                    binary='0'+binary
                #拼接每个二进制串
                realStrBinary+=binary
    # print(realStrBinary)
    return realStrBinary

# 用于解密，将传入的二进制串按每8位进行分割，然后存入一个列表中
def subBinaryStr_decode(realStrBinary):
    realStrBinaryList = []
    #若二进制串长度无法整除8，则将二进制串后面余下的0去掉
    if len(realStrBinary)%8 != 0:
        a = len(realStrBinary)-len(realStrBinary)%8
        realStrBinary = realStrBinary[:a]
        # print(realStrBinary)
    
    #分割二进制串
    for num in range(int(len(realStrBinary)/8)):
        index = num*8 #起始截取索引
        sub = (num+1)*8 #结束截取索引
        realStrBinaryList.insert(num, realStrBinary[index:sub])
    # print(realStrBinaryList)
    return realStrBinaryList

#密文解密
def decode(base64EncodeStr, baseTable):
    realStr = ''

    #获取二进制串
    realStrBinary = getBinaryStr_decode(base64EncodeStr, baseTable)

    #获取列表
    realStrBinaryList = subBinaryStr_decode(realStrBinary)

    #获取真实的字符串
    for a in realStrBinaryList:
        asc = int(a, 2)
        realStr += chr(asc)
    return realStr

#检查base64编码表，base64编码表长度必等于64，否则会出错
def checkBase64Table(baseTable):
    if len(baseTable) != 64:
        return False
    else:
        return True

#设置编码表的偏移量
def offsetTable(baseTable, offset):
    str_1 = baseTable[:int(offset)]
    str_2 = baseTable[int(offset):]
    baseTable = str_2+str_1
    print("base tables: "+baseTable)
    return baseTable


#这玩意我不知道怎么写，靠自己了
def main(argv):
    baseTable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    if '-d' in argv and '-e' in argv:
        print('Can\'t encrypt and decrypt at the same time')
        sys.exit()

    if '-t' in argv:
        arg = ''
        for index in range(len(argv)):
            if argv[index] == '-t':
                arg = argv[index+1]
                break
        if not checkBase64Table(arg):
            print("Length Error: Base64 table length should be 64 bits")
            sys.exit()
        else:
            baseTable = arg
    if '-o' in argv:
        arg = ''
        for index in range(len(argv)):
            if argv[index] == '-o':
                arg = argv[index+1]
                break
        baseTable = offsetTable(baseTable, arg)
        # print(baseTable)
    try:
        opts, args = getopt.getopt(argv, 'he:d:t:o:')
    except getopt.GetoptError:
        print('''usage:base64 <Option> <String>
            -e encode : Encrypted String by base64
            -d decode : Decrypted base64 String
            -t  table : Custom base64 table
            -h   help : Help doc
            -o offset : Base64 table offset''')
        sys.exit(2)    
    
    if len(opts) == 0:
        print('''usage:base64 <Option> <String>
            -e encode : Encrypted String by base64
            -d decode : Decrypted base64 String
            -t  table : Custom base64 table
            -h   help : Help doc
            -o offset : Base64 table offset''')
    else:
        for opt, arg in opts: 
            if opt == '-d':
                print('解密结果：'+decode(arg, baseTable))
            elif opt == '-e':
                print('加密结果：'+encode(arg, baseTable))
            elif opt == '-h':
                print('''usage:base64 <Option> <String>
                    -e encode : Encrypted String by base64
                    -d decode : Decrypted base64 String
                    -t  table : Custom base64 table
                    -h   help : Help doc
                    -o offset : Base64 table offset''')

if __name__ == "__main__":
    main(sys.argv[1:])