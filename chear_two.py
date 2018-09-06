import re
from string import punctuation as pun_en
from zhon.hanzi import punctuation as pun_zh

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if (uchar >= u'\u4e00') and (uchar <= u'\u9fa5'):
        return True
    else:
        return False

def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""
    if is_chinese(uchar) is True:
        return False

    if uchar.isalpha():
        return True
    else:
        return False

flag = False
path = "./final/attraction.txt"
file_write = open("./final/attraction1.txt", encoding="UTF-8", mode="w")
pattern_ch = re.compile("[{}]".format(pun_zh))
pattern_en = re.compile("[{}]".format(pun_en))
with open(path, 'r', encoding='utf8') as f:
    flag = False

    for idx, line in enumerate(f.readlines()):
        line = line.strip()

        c_line = line
        if line.isdigit() and len(line) == 1:
            file_write.write(line + "\n")
            flag = True

        if flag:
            if line.isdigit() and len(line) == 1:
                continue
            if line == "<ssssssssssss>":
                file_write.write("\n" + line + "\n")
                flag = False
                continue
            line = line.replace(" ","®")
            line_list = list(line)
            c_line = ""
            for ids,word in enumerate(line_list):
                if ids < 1 or ids > len(line_list) - 2:
                    c_line += word
                    continue
                if word == "®":

                    if pattern_ch.match(line_list[ids-1]) or pattern_en.match(line_list[ids-1]) or pattern_ch.match(line_list[ids+1]) or pattern_en.match(line_list[ids+1]):
                        word = ""
                    if is_number(line_list[ids - 1]) and is_number(line_list[ids + 1]):

                        word = " "
                    elif is_alphabet(line_list[ids - 1]) and is_alphabet(line_list[ids + 1]):
                        word = " "
                    elif is_number(line_list[ids - 1]) and is_alphabet(line_list[ids + 1]):
                        word = " "
                    elif is_alphabet(line_list[ids - 1]) and is_number(line_list[ids + 1]):

                        word = " "
                    # elif is_chinese(line_list[ids - 1]) and is_chinese(line_list[ids + 1]) and len(line_list[ids + 1]) == 1:
                    #
                    #     word = ""
                c_line += word
            c_line = c_line.replace("®","℗")
            file_write.write(c_line)
        else:
            file_write.write(line + "\n")





