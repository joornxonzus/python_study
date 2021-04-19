# coding = utf-8

import unicodedata


# 定义函数

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:

        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


print(is_number('foo'))
print(is_number('le3'))
print(is_number('1.3'))
