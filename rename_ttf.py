import fontforge

name = r'C:\Users\liuch\Documents\00\HYAoDeSaiU\_crh1.0.ttf'
# 读取字体文件
font = fontforge.open(name)

# 设置字体名称
font.fontname = '火炬_crh1.0'
font.familyname = '火炬_crh1.0'

# 保存为新文件
font.generate(r'D:\aProject\py\FontDiffuser\crh.ttf')

# ffpython D:\aProject\py\FontDiffuser\rename_ttf.py