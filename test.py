# import re
#
# def url(line):
#     line = re.sub(r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?','<url>',line)
#     return line
#
# flag = False
# path = "./Demo/att.txt"
# file_write = open("./final/attraction.txt", encoding="UTF-8", mode="w")
#
# with open(path, 'r', encoding='utf8') as f:
#     flag = False
#     for idx, line in enumerate(f.readlines()):
#             line = line.strip()
#             w_line = line
#             myset = []  # 建立列表
#             if line.isdigit():
#                 file_write.write(line + "\n")
#                 flag = True
#
#             if flag:
#                 if len(line) == 1:
#                     continue
#                 if line == "<ssssssssssss>":
#                     file_write.write("\n"+line + "\n")
#                     flag = False
#                     continue
#                 line = url(line)
#                 if len(line) != 0:
#                     if (line[len(line)-1] >= u'\u4e00') and (line[len(line)-1] <= u'\u9fa5') or line[len(line)-1] :
#                         line += "。"
#                         myset.append(line)  # 将字符加入
#
#                         line = ''.join(myset)  # ''隔开，合并为一个字符串
#
#                     else:
#                         myset.append(line)  # 将字符加入
#                         line = ''.join(myset)  # ''隔开，合并为一个字符串
#
#                 else:
#                     line = line.strip("\n")
#                 print(myset)
#                 file_write.write(line)
#             else:
#                 file_write.write(line + "\n")
#
import re

str = re.sub(r'[,]+',"",",,,,,,,,,.")
print(str)
