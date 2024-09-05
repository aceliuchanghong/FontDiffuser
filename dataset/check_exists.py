# -*- coding: utf-8 -*-

import os
import re

txt = """
lch:匐凰猊庾庳廊阇阊阍阐添液梁密谎婧袈恿续靓辇款塃揸趁耋搔葺董葖戟朝厦殖雳悲量鼎戢喳崽赎锈掣犊粤御禽舜腋猹飓觞觚馊庾阑尊遒道焱溲谣嫂彘缉缌缎缘飨瑟填搏携搋摇勤蓦蓖蓬蓠蒗蒙榄椽酩酬雾辑睨嗫鄙置鼠傻鹎魁徭愆愈遥腮腹猿飔飕亶瘐瘅鄘鄣阙豢煅溪漓滚粱窦窣媲嫁叠缡瑶璃赘髦翥銎墉綦蔫慕摹蔟蕖模槜酾酶酿酸厮碶碴蜚龈瞍嘁嶂幢舞舔稳熏僭僮鼻獐獍夤裹豪膏塾腐彰阚鲞粼滹潴漳漏慵蜜谭肇谮谰谲暨嫣嫜凳缦缪缫璋璆撒撅撑擒撸撞撤撙墀蕈蕤蕲蕊槽槭橡槲樟敷醇醉魇餍磙霉霈觑嘿噢噙嶙墨镊镆镌镎镓稼篓篆牖徵艘摩麾褒瘠齑毅遵憋潵潮潭鲨澳潼澈澜潏懂懊寮谳谵履戮豫髻撼熹擞蕻薪薏颠樾檎橦樽赝飙霍霎餐氅曈蹅螨螭器噬镜镞赞憩穆篚篱盥儒邂瘴瘸瘳斓羲燎燠燧嬗缰璨戴壕擦藏薰藐檐檩檀翳磷壑瞳蹊蟀嚎赡黜黝镡簇簋繁黛鼾徽爵邈朦膻鳃鳆鹫赢懑濠擘嬷骤藕藜藩蹙礓瞻曛黠黟镰镱簟簪艟癔邋攒藿蘅蘑攀霪霭蠖蠓蟾蠊巅簿鳗蟹颤瓣羹鳖疆骥缵瓒鬓壤攘馨霰曦嚼嚷巍黩黥臜獾魔糯灌蠢醺礴礳霸颦黯癫蘸鼹矗鑫囔
"""


# 1.获取 r'C:\Users\liuch\Documents\00\HYChenMeiZiJ'下面所有png图片的名称,比如"刘.png",那么就是刘
# 2.最后,如果txt哪些字除了"lch:"之外没有出现在 characters 里面,那么就返回 "lch:没有出现的文字"


def check_missing_characters():
    # 定义图片目录路径
    image_dir = r'C:\Users\liuch\Documents\00\HYChenMeiZiJ'

    # 获取所有PNG图片的文件名
    png_files = [f for f in os.listdir(image_dir) if f.endswith('.png')]

    # 提取文件名中的汉字
    characters = [re.sub(r'\.png$', '', f) for f in png_files]
    print(characters)

    # 从txt中提取除"lch:"之外的所有字符
    txt_chars = set(txt.replace("lch:", "").replace("\n", "").strip())

    # 找出在txt中但不在characters列表中的字符
    missing_chars = [char for char in txt_chars if char not in characters]

    # 如果有未出现在characters中的字符,返回结果字符串
    if missing_chars:
        return f"lch:{''.join(missing_chars)}"
    else:
        return "txt中的所有字符都出现在characters中"


# 测试函数
print(check_missing_characters())
