str = "this is a \tstring!"

print(str.capitalize())

print(str.center(30, "*"))

print(str.count("s", 0, len(str)))

print(str.count("s", 4, len(str)))

strBytes = str.encode("utf-8", "strict")
print(strBytes)
print(strBytes.decode("utf-8", "strict"))

print(str.endswith("g!", 0, len(str)))

print(str.endswith("g!", 0, len(str) - 5))

print(str.expandtabs(tabsize=8))

print(str.find("is", 4, len(str)))

print(str.find("is", 0, len(str) - 2))

print(str.index("is", 4, len(str)))

try:
    print(str.index("os", 0, len(str) - 2))
except:
    print("Error: 找不到子字符串os")
finally:
    print("str.index(\"os\", 0, len(str) - 2)")

print(str.isalnum())
print("123kfjkds".isalnum())

print(str.isalpha())
print("123fjkds唯独".isalpha())
print("fjkds唯独".isalpha())

print(str.isdigit())
print("\"1234\".isdigit() =", "1234".isdigit())
print("\"1234.12\".isdigit() =", "1234.12".isdigit())

print(str.islower())
print("\"82733KLJKkdsjfa\".islower() =", "82733KLJKkdsjfa".islower())

print(str.isupper())
print("\"82733KLJK\".isupper()=", "82733KLJK".isupper())

print(str.isnumeric())
print("\"123\".isnumeric() =", "123".isnumeric())
print("\"123.12\".isnumeric() =", "123.12".isnumeric())

print(str.isspace())
print("\"      \".isspace() = ", "      ".isspace())
print("\"      1\".isspace() = ", "      1".isspace())

str1 = "This Is String Example...Wow!!!"
print(str.istitle())

str2 = "This is string example....wow!!!"
print(str.istitle())

sql = """
    select
        F1,
        F2,
        F3
    from
        TB_TABLE
    where
        F4 = 'test'
    order by
        desc
"""
print(sql.lstrip())

print(str.split(" "))
print(str.split(" ", 2))

print(sql.splitlines(True))
print(sql.splitlines(False))

print("   123    ".strip())

print(str.title())

print(str.swapcase())

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)  # 制作翻译表

str3 = "this is string example....wow!!!"
print(str3.translate(trantab))
