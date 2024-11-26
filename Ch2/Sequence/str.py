#1. 它匹配子字符串而不是元素
#>>> '这里' in "沃尔多在哪里？"
False
#>>> '沃尔哪' in "沃尔多在哪里？" 
False

#2. 三引号分隔跨多行的字符串字面量
#>>> """Python之禅宣称，可读性很重要。'Python之禅\n宣称，"可读性很重要。"\n阅读更多：import this。'

#3. \n被视为一个字符而非两个字符

#4. >>> str(2) + '是' + str(digits) + '的一个元素'
'2是[1, 8, 2, 8]的一个元素'

#5. 如果你想在你的 Python 代码中使用不同的编码，你可以在每个文件的第一行放置一个编码声明。
#   这个声明将一个.py文件定义为 windows - 1252：
#   # -*- coding: windows-1252 -*-