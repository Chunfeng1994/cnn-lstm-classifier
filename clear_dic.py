from idna import unichr
from langconv import *
from string import punctuation as pun_en
from zhon.hanzi import punctuation as pun_zh
import re

a = []
list1= []
def illegal_coding(line):

   pattern1 = re.compile(r'&[a-zA-Z]+;')
   pattern2 = re.compile(r'&#[0-9]+;')
   line1 = pattern1.findall(line)
   line2 = pattern2.findall(line)
   if len(line1) != 0:
      a.append(line1)
   if len(line2) != 0:
       a.append(line2)
   for element in a:
       for elem in element:
           list1.append(elem)
   return set(list1)

def sub_space(line):
    line = re.sub(r"\s{2,}", " ", line)
    line = re.sub(r'\u200b', "", line)

    line = re.sub(r'[\u00A0\u2000-\u200F\u2028-\u202F\u205F-\u206F]+',' ',line)


    return line.strip()

def sub_illegal(string):
    string = re.sub(r'&amp;', "&", string)
    string = re.sub(r'&#215;', "×", string)
    string = re.sub(r'&times;', "×", string)
    string = re.sub(r'&deg;', "°", string)
    string = re.sub(r'&hellip;', "…", string)
    string = re.sub(r'&#249;', "ù", string)
    string = re.sub(r'&yen;', "¥", string)
    string = re.sub(r'&#160;', " ", string)
    string = re.sub(r'&ndash;', "–", string)
    string = re.sub(r'&ang;', "∠", string)
    string = re.sub(r'&xi;', "ξ", string)
    string = re.sub(r'&oline;', "‾", string)
    string = re.sub(r'&#176;', "°", string)
    string = re.sub(r'&hearts;', "♥", string)
    string = re.sub(r'&le;', "≤", string)
    string = re.sub(r'&rarr;', "→", string)
    string = re.sub(r'&mdash;', "—", string)
    string = re.sub(r'&zwj;', "", string)
    string = re.sub(r'&sigma;', "σ", string)
    string = re.sub(r'&#128522;', "😊", string)
    string = re.sub(r'&theta;', "θ", string)
    string = re.sub(r'&nabla;', "∇", string)
    string = re.sub(r'&forall;', "∀", string)
    string = re.sub(r'&#30528;', "着", string)
    string = re.sub(r'&prime;', "′", string)
    string = re.sub(r'&mu;', "μ", string)
    string = re.sub(r'&tau;', "τ", string)
    string = re.sub(r'&macr;', "¯", string)
    string = re.sub(r'&ldquo;', "“", string)
    string = re.sub(r'&gamma;', "γ", string)
    string = re.sub(r'&larr;', "←", string)
    string = re.sub(r'&or;', "∨", string)
    string = re.sub(r'&bull;', "•", string)
    string = re.sub(r'&#172;', "¬", string)
    string = re.sub(r'&uarr;', "↑", string)
    string = re.sub(r'&lambda;', "λ", string)
    string = re.sub(r'&zwnj;', "", string)
    string = re.sub(r'&kappa;', "κ", string)
    string = re.sub(r'&#173;', "­", string)
    string = re.sub(r'&ordm;', "º", string)
    string = re.sub(r'&chi;', "χ", string)
    string = re.sub(r'&#39;', "'", string)
    string = re.sub(r'&piv;', "ϖ", string)
    string = re.sub(r'&#225;', "á", string)
    string = re.sub(r'&#180;', "´", string)
    string = re.sub(r'&epsilon;', "ε", string)
    string = re.sub(r'&rho;', "ρ", string)
    string = re.sub(r'&alpha;', "α", string)
    string = re.sub(r'&sect;', "§", string)
    string = re.sub(r'&lsquo;', "‘", string)
    string = re.sub(r'&#183;', "·", string)
    string = re.sub(r'&beta;', "β", string)
    string = re.sub(r'&#128051;', "🐳", string)
    string = re.sub(r'&ograve;', "ò", string)
    string = re.sub(r'&rdquo;', "”", string)
    string = re.sub(r'&rsquo;', "’", string)
    string = re.sub(r'&acute;', "´", string)
    string = re.sub(r'&#128557;', "😭", string)
    string = re.sub(r'&lowast;', "∗", string)
    string = re.sub(r'&oacute;', "ó", string)
    string = re.sub(r'&pi;', "π", string)
    string = re.sub(r'&gt;', ">", string)
    string = re.sub(r'&nbsp;', " ", string)
    string = re.sub(r'&#186;', "º", string)
    string = re.sub(r'&frasl;', "⁄", string)
    string = re.sub(r'&cap;', "∩", string)
    string = re.sub(r'&lt;', "<", string)
    string = re.sub(r'&Omega;', "Ω", string)
    string = re.sub(r'&darr;', "↓", string)
    string = re.sub(r'&#175;', "¯", string)
    string = re.sub(r'&omicron;', "ο", string)
    string = re.sub(r'&#233;', "é", string)
    string = re.sub(r'&iota;', "ι", string)
    string = re.sub(r'&#243;', "ó", string)
    string = re.sub(r'&#165;', "¥", string)
    string = re.sub(r'&omega;', "ω", string)
    string = re.sub(r'&quot;', '"', string)
    string = re.sub(r'&#128024;', "🐘", string)
    string = re.sub(r'&not;', "¬", string)
    string = re.sub(r'&radic;', "√", string)
    return string




def strQ2B(string):
    rstring = ""
    for uchar in string:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        if inside_code < 0x0020 or inside_code > 0x7e:
            rstring += uchar
        else:
            rstring += chr(inside_code)
    return rstring

def url(line):
    line = re.sub(r"(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]", "<url>", line)

    return line



# 转换繁体到简体
def cht_to_chs(line):
    line = Converter('zh-hans').convert(line)
    #line.encode('utf-8')
    return line

def total_length(line):
    dic = []
    line = re.sub(r'\s',"",line)
    pattern_alpha = re.compile(r'[a-zA-Z]+')
    pattern_digit = re.compile(r'([0-9]\d*\.?\d*)|(0\.\d*[1-9])')
    pattern_ch = re.compile("[{}]".format(pun_zh))
    pattern_en = re.compile("[{}]".format(pun_en))
    line1 = pattern_alpha.findall(line)
    for alpha in line1:
        line = re.sub(r'[{}]'.format(alpha),"",line)
    line2 = pattern_digit.findall(line)
    for digit in line2:
        line = re.sub(r'[{}]'.format(digit[0]), "", line)
    line3 = pattern_ch.findall(line)
    for ch in line3:
        line = re.sub(r'[{}]'.format(ch), "", line)
    line4 = pattern_en.findall(line)
    for en in line4:
        line = re.sub(r'[{}]'.format(en), "", line)
    return len(set(line)) + len(set(line1)) + len(set(line2))


flag = False
path = "./Demo/attraction.txt"
file_write = open("./final/attraction.txt", encoding="UTF-8", mode="w")
pattern_ch = re.compile("[{}]".format(pun_zh))
print(pattern_ch)
pattern_en = re.compile("[{}]".format(pun_en))
print(pattern_en)
# with open(path, 'r', encoding='utf8') as f:
#     flag = False
#
#     for idx, line in enumerate(f.readlines()):
#         line = line.strip()
#
#         c_line = line
#         myset = []  # 建立列表
#         if line.isdigit() and len(line) == 1:
#             file_write.write(line + "\n")
#             flag = True
#
#         if flag:
#             if line.isdigit() and len(line) == 1:
#                 continue
#             if line == "<ssssssssssss>":
#                 file_write.write("\n" + line + "\n")
#                 flag = False
#                 continue
#             line = url(line)
#             line = sub_illegal(line)
#             line = sub_space(line)
#             line = strQ2B(line)
#
#             line = cht_to_chs(line)
#
#             if len(line) > 0:
#                 print(line)
#                 if pattern_ch.match(line[len(line)-1]) or pattern_en.match(line[len(line)-1]):
#                         pass
#                 else:
#                     line += "。"
#             if len(line) > 0:
#
#                 myset.append(line)  # 将字符加入
#                 line = ''.join(myset)  # ''隔开，合并为一个字符串
#             else:
#                 line = line.strip("\n")
#
#
#
#             file_write.write(line)
#         else:
#             file_write.write(line + "\n")












