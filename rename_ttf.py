import fontforge

name = r'C:\Users\lawrence\Documents\WeChat Files\wxid_yamvaf39vkqm22\FileStorage\File\2024-09\火炬_crh1.0.ttf'
# 读取字体文件
font = fontforge.open(name)

# 设置字体名称
font.fontname = '火炬_crh1.0'
font.familyname = '火炬_crh1.0'

# 保存为新文件
font.generate(r'C:\Users\lawrence\PycharmProjects\FontDiffuser\crh2.ttf')

# ffpython C:\Users\lawrence\PycharmProjects\FontDiffuser\rename_ttf.py