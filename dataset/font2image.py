# -*- coding: utf-8 -*-
import argparse
from tqdm import tqdm
import sys
import os

# 获取项目根目录的绝对路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from dataset.ttf_utils import *

chinese_punctuations = [
    '。',  # 句号
    '，',  # 逗号
    '、',  # 顿号
    '；',  # 分号
    '：',  # 冒号
    '？',  # 问号
    '！',  # 感叹号
    '“',  # 左双引号
    '”',  # 右双引号
    '‘',  # 左单引号
    '’',  # 右单引号
    '（',  # 左括号
    '）',  # 右括号
    '《',  # 左书名号
    '》',  # 右书名号
    '〈',  # 左单书名号
    '〉',  # 右单书名号
    '「',  # 左引号（书名号）
    '」',  # 右引号（书名号）
    '—',  # 破折号
    '……',  # 省略号
    '·',  # 间隔号
    '／',  # 斜线
    '～',  # 波浪线
    '﹏',  # 下划线
    '【',  # 左书名号
    '】',  # 右书名号
    # '=',  # 等号
]  # 27
numbers_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

english_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
chinese_punctuations.extend(numbers_str)
chinese_punctuations.extend(english_str)
char2img_list0 = ''.join(chinese_punctuations)
char2img_list1 = '讥填益潢螋镇儒砂骅舣队豕逼仁莘堕环批氟蛛蚣蜷崩肱鲅岌爝整仑垄簿芗蹬缇顸屮箍脯喈浊净坳诸耍鹾溧鹈仅埠猊怎央怔潋硝墚迁渐帜拚热捉髁遂擀倔俾舞踞斛眚铗幻蔫蕤啵龈芴瞀敝裣蔟癞苠崤贽蕴欧殳杞霾泊帧娈啥趋诨添炻祠稀镂鐾牡踊嘻薤绕猁甩坜匪驶铺丕埕玺敕鏊纡氐灼桉绗睡带贬晷艋剀嗪耦餮眠骞怃逮照苔预库馒尉棘翻殓州痔忍断湄睹燎娅客纂沅蓖畴老礞窕笕迦杂桁犍蹄螅睚扌鞣紊葙广耒想巫鲛窦觎飨惧伏啃档猥龚莜蝈筏晒莰圳焦唆咂淌仔鲳效熠奘厣熨蔹郓勹烯腹隼怠樵僻覆恁癌隳撑蜗缙蛳绺核粮茺湫可桌绍盟凑扔痒皆鹆酋麸临罪淳讪嫩兄姝输哉哙埸黩岚菱拄奥荛谎昨宴蛉岍欲絷岩什蚋瞪伉撰角递掷穸童塬箴藩忪膳弊溲碎槭豌峄镨僖玢硌最此腌鹛掬疋铽珠蒹吭联蒽刿茵寨犏逾矿称椭顼据装禹聊笺摊企爨花况远兢粘诧叫薄仝魔俜亳垮宁饺鳅阽涸绯钙腐狴诠祁菸褪仪惭极谷灬刭真铆耋狸佩黛夥徽埂鹑撄邑挠瓞懦垅煮锹雍静骊恣宵柞邗黉苹婪溟甙笄固喁幌戬葬茆诜烀茗馆刽令摘嘲崾胶词数苜湎畅醉碇隧纹莅乒廊飘累冗人吼佯鹘琢协曾弗萦漫挡雨绀堆爷袤挚腕时腧伊蒡辙囝毂焊话端徕髦漪皴裳稿萑囫彀瞎云晦躅灏乘剔货怆枘痢膏茧滗拾阋葭逖郊筅串蚍惦阐愈迥扈喱厨镀葡孚嬖押谬涉沌侉铣忆淄酯咱闶悦房蓐咋嬲仉苤店篼鲤财矸裁鸥疴莪裎娲岔掊缅啪诵噩封痖起准脘劳夔漩眄屦盹齄尚龅蔚筑史甫量粲钜延魁啶敌入喃好柜恪丁菌钆饔焓徨兰熙莞蕈拒犀搦虎轭聩余责豪钺铜烧旗殄玷漉蠡奸靛硅歌沉家栅伐呓浑醢屏璞谚末氍默讨府凰签饩郢渊哧埭项丌袈胛鄞嗄摺酶粑脾绒洞泵孩瘃綦蓥祀贶瀵馋楮模彳崆捺钇茔蟊荐村蹒乖堇跖轼玻遽嵝徇哗疣休缱奔诹钢艴范属警鲦慎麾另飙镪塞枫馍擞掰恫枇芹噪碱脲挤遏袷佥豉杰肩县蝎垢诶牛蛾嗑铵搿纸拘蜮腻昌烂洌屹搅永稞崂鳎箱缕檄缡浆篾目蚀妯诔摁蘅坪算鹬愍免载橐加桂巯霭悃蟪辍万鳟躞扑诃仄泌颐骨取孥貌袂滠织械济尧增玟恺祚喊耱宓榛笥赓旺橹皱禚堤酪她雯鲮藻种洱您钧镗弟鹋鳘秕败肾砩箪獒缶狈墀成揭摭樽嵬苡铪妞侄刊朔酥肴琥亚缛观松初妾螬惝鲍踽檠薛嚼汾镡鄢饼溴漕浸梳蝇珏痛栩堂父赴錾蝉涯瘅泻祗呷泼伤纳徐空磉牲赝膜朱癫嘹占晾把讼抻呛舳墩苗框吁嘎瑟纵砜鞔泺顺痰摒赃刷蕹穑咴蟆仇芏醋杨裕镜闾大梃痿艨闺奚碹横圮荟穰荇障昂圈泣瓣钝帔巛蚩丙痫亢惶救蛭辩畏疼姣卵屎鸣蕊贲糅氅卖段湟泪揞惚眦绘祈耽亏谘贮苇茼艰蒿嵇鬻唾踏翡顽嘘鲈矫蒲邀爹扶溃获气抬仿戍足鲻熵艽赵泽迸纣甬蜉彦纥橡绅簦腚咯邱斟琴菹峨缩慨仡嘏筐裸垡炜萘咤椐逛鹕吡蝶蜃佣剖隔杏祸闲咪斋江萼肮槁彼鞘愉氆馔呵披矧功榷阔谪袜颌柁匚炉鹧仵吞酚个唁哀楔汊阼咩喔绣薏厌茅箸帕沾芘砝绳赎胬惜膪伴送芯怄沏轵迷篡植爆疖弱缀缟撺盎呕霪烩葶笔龊蛀缒膺杷刃溢勒媸疸伢勐搜篙委叹木谀搋丢碗咛啷苄蹦恝莺卩蛄坍徊废喋蕻呤臃殆箬彤艺谠浩拭陡胝冀瘀跎辅勇妥尿呆雠礴徉咕蚪荣苯孺鲐偕锤太纾轾扭斡螨痦认芜情湛抟锪怂徵醒又配乜饴氓蓠千缚幕簌考巽忒敖煎驰实檗簇螓饮棂蓄孑享编惟嫠歉昀滦简士彻钣卷腔腺蹰暴廒辏稗闩吣铁跞死昼凛瞿邶轶莉趾跑饧嫜榴舁隍猾醍椰膦硐觇姆台诣蕞颃籴鱿魃蜓零涿徙皖荑杜轱佝蕉纶鲼珑厘留帛陟淋崞疾俺沸膊汗讽唛威表洛坤任轿珍鳇唱坝榇丨摩崦辔痧翳舂债瘫囱笙诊薪裆躇羹亨滨罐俭拎雎袼巴乙鳄埙挛荃侍笸鬃旧伎晰绢淞赋匕归电衅饪抵晶鄄翊呶扉鳖荮棵艳羟陶礓捱笮产襁骘娶钉逯驷恰髂褶罅井蟾叉现锥潦嗟衤近骚风暨勋蠃毳翠娴口韭碉搭傻吴亭黏芍缁诖鼋淘夜蔑锑陂葳劝黥海辊辑傈肃练路劐与娟扣唑疫辰鹨哦距黜绛柒跸划剂喙侧删碍黪苑诋员锒旯孕茂要妻舶耿翔悫俘胨浦酬指证葸透潜嘀砒甥涅捩友亵戤枚隘谯果蛲锻跷缫遥巳扛窟袖滟澉地悌皤哼纪枥浃枯嫘贞措敞揿承呱迕莓阀掏沔醪颢嬴禽筠爪橇牝绰撙淑亦馘候箝逸旬闯稂饬互务埤腱蓿啐蝾红猓梭镲擘氢揎菀蹊柩概膘讲铄猜贼氦瑁瘘谋荪速埽缵畿缸来阪牦柝铈拆澡泗邙嗡棋浼锢蠢唯嶷优让饱吊阍扇籼沣鳏磕踩鲸选鉴菰栋脔甄秣柽榭圜扯吗卟驵鳝匡屁渠鸶铭羡瘭鎏檑溅蚰析拍卧骑虮频镞截抨燠惮苎郝养哆诳堵芊稽饰夕损撷九勺炀俎锅蝼催案镣宾辄猞澳荞獾噫侈嶂尽戟搠熹梵寺画掺坛斗鼬钅呼阴跣钻壕掾阂薜桧厢釜骶褚彰丸蛎酆汞篚勰濉崧浈搡份忙诒桦诮诗宦籽汰衍枪辽猢磨普躏蝣陛阿簖硒镢璁挨谇姜铸婚糖鲷湾陀莆升啸翅炱柳蚱胚嗤脱阵爰缨昶铐溘蓣陌计茄蓰面髓捎裰掂甍刚啄渭蝻精鲶搌沮轹聱慌泾骧娑瑚辛糨煤纲撕墁赶橼攒源连哕缺哌匾健蘖俟比闻芤曝忖狒鳙头顾氙我绥鞫酡笪筻裘浜缦猬盥祆衽肇侦均生细薹堪似进踅悄橙捕蝓旃迭砥榉祧妮瑶惨诽辚铢怡绫鸠骠见三揶汩跫负冤阁夂蛑爱砼呖壮卉馁膈逑点待围彡禳蟓稣寞城钯篆尤羔趔阳巅瞰倒锛衙烹雏苟僵坎揆逶够碰篦孙菲啭飚俊恨澧理羊察毫彐术笞给傀腭鳊荧锵偻蛤蚯呻韫医殖分穿撩厩监鹗赍澹罴杲爸踺疒锎奖牒院水缬冉怖怫锫菊站谐胁白抖婵奁床蛇痊蜜硷哑鹅嚏旦耀觑窨茏炯觳周瞄迨驼萌抒侣璇丐剡疗铀饭咏乃齿槌盒搁拽鸷鹱美鸸租磲谂顿昴馅坭汴林洲施砦缑琵泫氚泸没螃猕媵蠛湓吻教赧驸奢宣命灸埒怏骷粽轧辆叼才灿猿径骆唳盈纯磴请罨觖笫峪郧帑鹦阻稷疮呸牟淹塍镱锸界司锦雾厝笾沦卑靥蕲庾条渚洙蹀攘攵侮缗觞漆腽怨庶软蚊秭珙砚懔除瘢蔬曹商悛社铉枕歼裒懿滇髹煨匹沱殁帝锆蓓辂砸缈桀潆醭惋肌昵骒坶卢插俸婉酵莹熊佘担沃氖雷愧污札窍踟绿茳疵钶隈而跺戡妙栽砰间潮惑胡斤烃治钭邝衮敦郭锖箐门做畈吉浓胗晟椋冥紫郑扁柄酷邾厅钡蹁铴壁弹胖贵素癸奠纬钊尴黢度础卣刖菖恙瘪殴榆肪洽褛淬眭艾尺沧欠他晖姬唿禀枣贱邡虿灰觏胀尾喧抹芦烈箦焙缤讧名慑刀钪汝髅恐肺霆规病肉舷将漂犭羝骝拇鸨孜蠹沪迟统蟀达佤孀浍怀哥错胞适瑾储甯蟛磊耄枭觫絮昧攥办暖心腮戚瓯帮寓馄匦嵯撬鬈纰鼷版未偏冻癔挟霈涛篷冕糇泱梨袭尹扩其撮糗仕娼裔妓谈舫句鳋鬓娘罂闱曷账愁婀厍莲嫉帽虏影啾学窠肝耜葆应衾栀膝旨蜿究渥簏庖聚鲠刮股躁睇图硇殃浔映狳罩稠垦匀顶侵淫谛芋劁器聂筒症脎纟郏姹例根劾羰猡罗自曙歪糯驾缮粢恹邋丛虞兮谖杯庭半杪嫂坐途臬缌镥课飕函的不密署众咽筌那楦稚棒婕墼颊衰挣铡铃肥革嫖赐剜妇盾职须叶琉澶堠护腩泓寡爵喉蔸榀蚝团茜日砉垧叟抡贩囊秒罾攫撞贺磷镉咸丧诟叵苴鸱笠质且樱滞郫瓜廿苏君榍逗鼢廪赖砀冠岘罕宜脐朝突硖辞钰阶书霎池胳骱布岁曳荏呋樾镎伫文殇啊桐軎茁赅瑜躔拴缔姚钗违元徒蔼擎疱剩褫鲭诲少晚些姒邓急鲨蘩杓虺止矶雉仙栈辕骺湮镶吓乎寻共修揸绔兽瘌垭荚镧蚌臁豆篥礻婺岸衔徼柠哒铘镦绑典岙怒凉铅竞侃彷总侨锡吾绩疥买俩瘾俅鲥憬螵印拿楠瞬渲庥鸯硎炕镔烫蝙洄蒯蛱俑丹沽孢洧率改狩攀缰钨瘟帖焖霖亓毯疃弘胜薯告琰苦卿耩窃藉西谵俗仗艿坡式黟坫剁肢燮崇啻遴朵勉娣鹪痂箢溽秧岳踢懑犒羿滚陇粞粗靶腈佬瀹袱嚷町莩岖漯虐阑麈颥锨掮铼着菠襟营耠恶氽叙芑谤旄胧謇陬报诙镄甑晃逭馕髻嘴墙蛸压螫挞曜毛聋柔瓶踌硗獭榈渖碜擗唣盐毪龃料钮郡俳诫刁混会癃忐钵粤芥稔烤审蟒梗猖殉瑗炷丞测导爽忏思敛戒狂坟趁锝泮平梯庳滑慵蛮购髋沤珥桢篌掀仍吨乌紧胺柃妈莒凌陆舐耨抽就踵葱跌嬷觋设绨娇诀二鲩邬揖拢嘌濡沿霁藁灌廓托喏龄肋虔笱遄谳佳墅严讹跤铊肖韦菥折衣瓴阄椠澄颇瞵凡褡忭用鹏氪邵渌遮姿嫣鞴婊银钱醯踹驳愕彭坠莱匙咄私能世祺娥萆酰颈阃汀瘁觜滓诼驭睁娄斐无柯昭晁逦守味匐痈厦宀蒺饥甾趴展嵊梆力倡囔钍殒祓舒郎魄谄聿膑弼席岢级滕烙痱啕返耧炔孬黻迪奶拗淮火毕桨四烛湃决椽寰边赢芟欹刺古沥涮鞅冽槎刻纫岛钷糜獍穆湿渍猫蠼诡答昙牵睑殡芰燧嘤藐缉漓拨麒谶弪晨匏武去伥坻鸾朊醌眷旷哺棹佻狞啰哂唼鸭剥贤芈樊诰炳哓怍柴褓迤捷懂圆冢价挈暌撤蒇柙铝钳溶凶瑕癣忘鑫蔌鹌欺筝菘萋丶峤蹲喹珂衡骄闹雒悴钎膂辈噙漱汔势僦锗椹铟促畛瓒爬艉汪臂俚埔志摔簟愠特椒裱茬靡屠矣萝蛞乡狱斩籍縻骋癯蒌氵凤粒糍猸腋磅雳是励髀瞥愀聘捞郯讦傍钒簪荫仆镑枵桥屉香瞧琳谕粉许羼钽孱肼鸩玫羁璜际熄惠绻锘藜褊贝攴帘菏翘貘嵘眺毒胥僧醣咭泐芎竭苒趄颠魇镟檫收迎欤苕嗥噘滁米缪微箩耶俪恳菡钹棣诱诓劢椤对矽约楫嗫提珐襦榘鹂瀣蓉码篑关卯皮清侑溱侥搞只知刳摸蝰荦献圪鳢乾恧彖缘荭碴惺瘩疹嘁羚睛鲒熘蔽闪年敏邺予恽庆息拙磋闳皎祛膻虬饽滋偌兆既妁贡戈漾构信蜊铿埏糈尼邪握睥撇橥疝谫乔鲆庙衢币鳓尊畦堞神祖湍骡蕾馀昕寄舜怪丫猎挽中谱睽阚铮砟包腑庀礼抿蛩涎蓟圻佧厶勃官绂品褐御蜇笃倚蝌糕邕咳凯幞脒苁廖畔京割傥彬眇七憾鄹惴耆拧晴翮噜耷榨浣秤掎树片赔锬拦嬗听砌驮赉瑛涟履和漳腥晌幸禊遵痕谒行擢谍党锿镊曛麟镛飞翥勖干弛玛伽翱倌兖嶝劈酾政衩瀚箜粼苛稆珉鬯喷寸翌楚靓胴蒸键墓熬肯窥豹稳嘞聒愚匠毙岭舀鼠梧绲囚宛蛘吠患悝启颖譬饫宽赘梦作望曲更禅谲蹯裂肀翼鳞怅锔俨步狎几舱显蜥哇宇惫煜桔憔晏颞骟谏蚤芨骗嬉洼簸操罡含苍犷郛瞌皈搏潺堰寒鱼傅跳髯岽叠媒岣殿胰醺箫麽辱暇蒙谢氘牿幡悭杳蚴殊寂下因伸郐祷宏卓字捭枞衬瘛街堡被钓暮靠堀趸还户眍庞耸邂窆嚆爻久椟碌哎橛掐坊基贳嚯箅纱瓠肛妩道狮巧左鬲黹蓝妖阈润砖筷沭埴壅诤售霹纨堙筹呀鳃燃钌矍桤茯琊合它色窄锕契蔷击炒兕育慈百裤鹣畸活杠歇齑勘每糙鸲以诛讵惩搓麻眼崮业瘼瘵鲡阗爿蓍剐牺漭昃娱述涓妨腠薅沓农确俯秽鲎凸盔麂冒吲狃绸馐鄱綮崎蹿彝愆弧俣晗褰畚莴歧讯樟兜藏鸿弦狗瘿锌卡蹼甜蔗狄羲琪踔訾明炙狰锈歆螗滹毹竣蛹粹蕖强粝裙妹研阅掳峋忤馥却剪蘼欢误渎逊怛萧笤盛唉皲臭捃勾绠幄揲疏伦馑窝槟控犴蜱雪枳鲑奎烟邹翩崖硼诉婴金附谩昱镩喝汇疤箧廷怕峻开诎婆陨该瘦隶完锭铋毅酣裨殷蹩煞窖保谭涪竽黯璎锷孔伯锺暗楞轩骣濂血壶陵訇堑燹筘秆楼靼袒酌夼嗅舌貂俦第盗焚灶皋尝啼恋砻宫舍焐必玎鸡癍轰寇卅创笏懵猗稍狐弯悠跆宿耪镆嘟纭銎埋胤戋期伛阡使闭孟乍索母驽棕前葑巡忾耘壳隗声哞绷铞吵圭钬蜢宸栾趿鲔搔妒蚜洗崽魑臻碧瞽票炊为板泞扮牯忑颍泡综醮囵正醐吹斑唢邴危廨碳跗汐恍锍踬阱囿场萨萃过躲偃圉塘悚帚珧筚暄踪眵缂胲蒗铯塄胪历富蛟恸榱鍪啉夙屯秃傩福鼽觯黧铨韪昏钿闼戌咻愎狭揣栏习咿绵舾迈淆珲愿斧罘蜴岈褒鲕读铳劓缏庑郾荻瘥振陈噱溪邸瑙槊蹶罹虚嵌麦捣珈蹈耐葫嚎胎次滔茫佃杈孽祭刑岿潘在奄底矩荆裢走找屐寮裟镏煸方筇傣忠坯锇光濒傧肟彩按耢揠问弄跽唠惰湔肤穹锾诞释搽耕翕虽潸韵冯罟青部腼摄舰念痉玲嫫颏嘿厥恤焱标禧借穴舵眉良漠轺邮鲟迫呐竿垒曼语鲺鄙汶十鳗饕锄痪屿猴荸趟佐李卜瘕霞瞳鼍粪汕章攉虍剞恩粳桄趱蝴痄跨希钦甭若定犋宄温帷芾歃锃韧徘嗨捻祟麇琼辶颁邃毗丑瞒技垂麴洎畎菩谆哟杉珀射驺凋莸儿杆龙腾醛届拮致贿疆朴讳喂鹿黾锶鹄脸赳炮件哄悒苫噔娩淦陉奴圯骛暧搪隅亥柱惊炸煽倾噢榫迅邦垲忮匆炼幺骤运刂铛酽肘钴狠帅竹汆假钫窳阙鹰了殪镐役已煅暝埝秀栝恃郇黄肠螺独闵臧氡诈蓁罢拓儡六洋蝗焯憋庵姊抚捌恒佞饵失耻缎蓦诘冷杀釉矬叔狲枉艄援嗯耖住猃逝狍枷洹撖蹉摅萱獐裥桕凼噤孪蛔张弁抢节阏僚锩瓢转荔荩庐咙镓捶溆识长隐域耔憨写邳於芭瞑伧块茴恬槔饷蜍馓驴阝蓑舯绌骀籀回束唔抓赦蚧始依沙戊簧忌蹇渔培菪尕克挖栖赂浒氕盆备倦龋橱吃馨檎楣染钠篮锏鲣辨偶鳜介盯胆墨己便浮卞酹瞢胩锐吩袄扼痹啖兹懊蜈攻宠丈激召魅亲驯疑迮怯洒鲲番戎垣捐智锁胯铙喀扰琨女鸽恂窭沛探矛亍唇鲁窑旌硬株烨逅恻樨立叛喳媲天涫窈垸咫俐圩蜘策嗝卤揩满呲冼蟥脓靴腴遇桷铍蝠蜚谜梏缆屙蕙费瓦录铖憝忧欷蕨闽妗维韶榕钥蒋妤暹畋仰怦河邻逢繁国弋轳值汉铫喘朕蒴倘澈韩邢哝蠲熟之犬瞟绚逵塾肚炅集翟沩螭蛆帏粥镝鼎笋像谌菅撒栊脶辐鞭出肄匿叁滏绱谁憧落箨掸跏凇舄跋弈塌颡栉缋鲇粱恕摞褂怙颧瞩坩篝垌但髌汽位样鲵欣磔鄂椁苣飒螟赁桑坚泳渡娃篪管鹜咧蓬咀扒忿啤蜒窀噼畀新谰判坂抱馏蹴嘉黼窘缍泶师唧牢萸秉眨摆後经鬣局发骈验努尻槠溷鼻硭澌嗳服柏濑券廑帼萄吱颦草揪绦赏祉嗲鲴赠解撸觐或藓椿授撼悔惹冈喽很楝淼劭康匮奕擦岜酲乳颛骐丽檀痴庚觚旎掭鳌玉绋推赀渺铠镤裴蟑仞铲记战聍恿糸黑萜凳杖烷戗拷山毋慧摇裉绉莨啜绁噎菇屑鬟鸵捡潴茉谟镖鹎丘敷畹臣觉掇匣桫疯都响噗碟莼诿隰垛涩谑兔叽柘蜻礅捍酉浴阖缧眙嫁苓鸪叩屡潲等垫歙蹋蕺炽躜餐帐甸雇咦锰蓼荀濯皇厉礤蠓鄯困赕董氨鬏罄注芪囡组赊帆坏霸拶洚随啦投易痣恢括权舢谣右盲拖溏衿车鬼茌啮壬秘硪同猩崭拳弥惕鲫妃奋疠媪蠕执抄榜颅巢庠硕锯癖伍看挥宪滥裾慊栌触吸挢柚群胼遛馇于抗螯崃丰岬妄罔贸霄枢吕殂即睫性淤壤沁怩狷荡毵肜般呃矮疽搛奉暂猝锊交由媾置蒂坨幼肿鲽孵灯坞茈瓤恼毽谦觅疚轨茱旱薮媚臀限蛴闫螽胂安扦峒狯哳翎塥嘛忝筛蔡娠趣蒈沲羌暑纠圬淝渫溺睨氤碥胱婿吟圹祯原銮潇义俞耵溯垃淀涝踣族黔劲艇难砹秦狻浙宗里卦沐貅亻咆撅跄忱橄别讫巷璩争某题桊叱笈誓舴唪鄣髫蔓茨悖防偾鲢岫薷瘰垤森钤熏皑脂荥菽糟芳迹拂艟遍阉及怵鸦螳座资针聪毖淡籁酤辖囹后建伲螈吖玮愣辜睐葵峭亿槲容逄婢涡盍溉忻硫辣钩砷飧嗷妆铕诂钏龉涤洫礁焰濮蜞牾棱睦略蜡郦砬铑离迳搴佛佟拜具涂竖跛登蜣哐铎熔利敢涵碚嵛獗笆謦型页嘶祥挎锟辗崴霍砑岱雩禁鲂夺踉圃肓鹃胙绮皙土区盱厂墒逋申袅憩荷鹩军羸跟砧鲞钸内猛醵碣笊浏虼系锴孛燥赚梁挝橘先舅嘬谴狺早酃垠菔旅勤洇芬衄匍轫菝幽桩亘刨犄睬窬魍阊悲桅禺坑哲摈镫吆嵋所肽谔荽壑演笳宝溻廾烽稃铷怊谡筵线簋督鹚豁煌盏甚侗视湖旋巨秋哔号糁吐澎马愦泄网悉镳嘱赡遘腓药隽崔脍瑷挲制坌反领霰灾耗娆常虾悱降瑭枸搬泉砭符放挺肫奇序塔噶背琚班蒜逻缭藕钐贪链散醇刈臆覃呗憷副列轻哜碲瑰尢喵挑阮楗处姥状嗵戳描滴脏髟邯闷镙付郴剧瘐偿夹亩戏低悬褥册闸琏酎睢嫒全邈垆邰感誊霜殛颓脬翁璋嚣萍宥鳍野诬襄荬也剃英蹭姨滩铤殚汹你牍镬类尥哨瞅市暾游儋嘣圊坷踱排汲较苋鞯婷疙牮羧葜谗鲱龟尖蛙茸樘渝镅震姐厕娓悟涑瞠臌详跃璃箕芝攮犰嗦机剿喑嫌箭绐戾柑主缢讴裼踝浅鸺嗽罱鸳啡楱黍鸬阒销鹉缴淠棍萏鹇黎馊诌川娌篓笑朦奂饿咐虢凵踯掼傺工捧怿陷磐眈乞梅黠程各允蝽锼胭舟单蘸戥沆脆浚卮酒匝辇绊钞佴逃眸动蚺纷蹑氧洁薰叨泅纤癜移赈诚掩柢眩铂寿脑戆掖赫佑炫觥荠驱尬舛喻碛涧浪蚓变拔瓷弓屺绶轮氏谝诏煳尘弩卸漏顷斌梓浞畲愫训妍蹙砾逞孰斥扪袋铒琬琮坦挹酝阜首躺篇臼冲呈鸫遢搂鏖盂躯痼俱阌虹仓茹旒榻睾虱咣荒噌蛐受唷醑掉戢酐脊疬镘重聆有论甓掌澍捏惘碡炖颗牌迓龇寤赣吏佼帻鸹柬娜谮通苊狡馈卫楂辘魂田泥慰桃嫡厮噍携趼堋莛埯寅墉擅慢隹浇继否脖冶存快棠陕伞舸褙芷鼹珞助渴艘熳劬遭琦獯事砗腰融槐食宋拯玳贫巍涕厚泛短夫流魈估刹揉帱氛吒津非笼鹊桴壹憎沫仂残宰扬芸忡跻廴彗铧屈高唰跚手架烊袁鞑蓊雀薇兴涨议懋恚毡洵痤体椴疳拐煊夷胫蹂袢旮蟹埘绾榧嗖景悸舡害姗渑钋叭韬晋蛋虑劫淅杵春狼超坼倭艮遨鼯虻倬逡痃杼钟庋缄瓮榔态栓玄兑啧宙舭贴拉陴骓毁凭庸订萤苈呦琛膀髡岂陔越锋然讣氰疰瘊疔尸寝并晔套潍莶哚凹峥瘗芄践鼐颂雁卺煲睿髭至身相鲚抉物饯酸乩浠款积嵩陲勿匈辋菜渗麝袍苷葺绞舻炝笨芙炭仃悼咎酮港骰滤螂摹吧捆秸蠖琐伺藿莽媳栳颉襞碘廛燔疟拊禄缲酗虫旭倮崛阎巾樗琅墟化幂姓调萎瑞岷荼姘祜多衫弃掴拥劂曦柰挪寥小菟宕峡趵孤钔撂甘猹攸棺餍腙黝屋伪雕粟咔衷迂妊钲膛氯钼佾杩醚倍兵霓嗬侔尔郅本豳镰菁鞠乐龠潭倏娉跬遐唬眶膣耥痨尜扃轲豸玖庇驻鲧濞瞍追脚腿谙稼耳艹舨疡獠嗔博佰彘德椎犹阆八善垴灞音缃烬鞍咖稻赙骁法两宅喾贯摧税枧岐臊故替栲蒉凿狁擤绎昊纩锂刍萁擂逆癀缝昝这塑蜩磙意铥嘈纛庄如臾汛赆层慝幅戴霉偷醅棚公檬南噻辎搀痍代嗍赛蚬旰囗兀呢艏球颚涣咬濠湘筢鞒乏锞蝥靳魏择茚铰旖瘤蚨渤谓再灵说芮拌今狨鹁颀奏桠峦酞轸陪夯圄隙室拣夭涌腊肭镌赌北镍抑挫骸茛举埃饲仟楹露镭伟们骢莠歹王妪者愤戛嚓汤庹趺炎霏瞻滢省询窿侯灭笛隆鲋咚络刘雌午油陧磬躬鳕藤鹳窒艚呒帙栎鞲枝酱茭盖砺泷刎嵫求俏琶貊腆孝朗骥捅稹胃翰柿邛著磁醴丬呜髑形格盅玑嫱征傲斯派需铌遒襻居芡圣往氇璀上哪铩蜾蛰岗呔循篱锱楸遗嗓妣祝东毓葚蜀吮耙朐貉缥鲰麓犊船贻猪箔洮材惯赇星贷跪喇骖涔竟埚羞苌遑纺睃骏幔苘涞颟偈屣谥戽缠泠翦殍莫堍苻掠饨遣引辁芽皿岵璺穷碓皓退揽言咝鹞蚵阕驿洪卒褴寐婧慷持擐糠停绽哩沼秩犸棉凝衲么夏姻芩鲜蚂科淇扳双懈晡避蠊炬境迢捋洳锣谧鸢漶赭轴矗月减汜直哮续煺脞贾遁媛锓龆蜂鹤梢郸蘧潞雹瘸曰舆鼗莎貔鳔亡茑异侠慕祢叮仲补址伙嚅璧犯瘴蚶揄恭垓蝮龌瀑猱悯译澜剽膨璨徭到惬泯蔻嘭敉芫肷夤枨夸猷竦采狙谊破懒液飑哏瞭辉深犁璐逐哭淖敬孓舔踮瓿汨碾蛏躐嵴偎泖脉郁郄接郜子氮徜斓打孳戮挂盘痘焘乱楷窜檐薨俄槽豢劣抠犟眯峙糊詈觌蚕雅甲锉酢募葛剑得消伶鳐龛峰钾槛糌碑逍拼哈粜胍象茶辟桡蟠盼磺校呙溥剌蚁牙昆拟鹭专飓铹蟮扫槿哿岑囤外肆蒎獬繇镯鼙咨巩五畜从樯桎蜕忽烁蟋郗圾揍筲喟悍鞋何敫潼敲瘠徂蝤忸茇拱隋一鋈啬筮椅朽彪牖谅鹫窗饣煦览拈嗾穗招胄迄唤蕃迩榄沈氲亮酴酿偬棰砘吝怜棼饶玩靖嗉捂评晤跹铱魉绝抛航当鸟嗒叻龀疲嫦讶侏镒镁嘧杭禾啁嗌桓泔齐冬厄辫兼蔺浯唐粕弭罚晓示羽妫枰趑蘑差豚斫牧檩桶矾沟詹充轷眢瘙钛试弑婶酩掘怼搐嫔嶙唏查则栗险烦骇凫汁鼾向烘律赜骼复旁讷滂秫忉珊茎戕甏阢篁换结佶供廉访燕颜茕氩喜苞泰晕诺斜锚枋咒传豇园绪民缳觊溜丝旆嗜颤额骂酊涠诅皂乓钚播掣鼓终荨矜豫削扎杌撵惆驹波冰焉缓纽砍擒痞沂男瀛竺缜荤凄囟季馗瘳垩悻曩切参砣陋雄奈羯支誉冱葩妲佚锲裹造豺姑漤峁鳆胸焕赤麋芒缯颔筱谨诩筋淙闰绡贰华钕石哽矢嗣聃幢荜幛渣珩酏检昔莳铬赞噬缣蛊朋骜'
# char2img_list = char2img_list0 + char2img_list1
char2img_list = char2img_list1
print("char2img_list:", len(char2img_list))


def process_fonts(font_file_path, image_file_path, char2img_list=char2img_list):
    """
    Processes fonts by generating images for each font.

    :param font_file_path: Path to the directory containing font files
    :param image_file_path: Path to the directory where images will be saved
    :param char2img_list: List of characters to generate images for
    """
    if not os.path.exists(image_file_path):
        os.makedirs(image_file_path)
    fonts = os.listdir(font_file_path)

    for font in tqdm(fonts):
        font_path = os.path.join(font_file_path, font)
        try:
            font2image(font_path, image_file_path, char2img_list, 128)
            # 处理不知道为什么没在的字符
            input_file_name = font_path.split('/')[-1].split('.')[0]
            output_path = os.path.join(image_file_path, input_file_name)
            if os.path.exists(output_path):
                generated_images = os.listdir(output_path)
                print("outPath:", output_path)
                # print(generated_images[6695], len(generated_images), len(char2img_list))
                # 汇总 char2img_list 未出现在 generated_images 中的文件
                missing_chars = [char for char in char2img_list if
                                 char not in [img_name.split('.')[0] for img_name in generated_images]]
                print("missing_chars:", missing_chars)
                # 重新生成缺失字符的图像
                if missing_chars:
                    for missing_char in missing_chars:
                        print(f"Regenerating image for missing character: {missing_char}")
                        font2image(font_path, image_file_path, missing_char, 128)

        except Exception as e:
            print(e)
    remove_empty_floder(image_file_path)


if __name__ == '__main__':
    """
    conda activate fontdiffuser
    python dataset/font2image.py --font_in /mnt/data/llch/VQ-Font/z_using_files/content_font --image_out data_examples/basic
    python dataset/font2image.py --font_in ../ttf --image_out ../ttf_pics
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--font_in", default='../z_using_files/val_font/', help="font path")
    parser.add_argument("--image_out", default='../z_using_files/imgs/val_images/', help="image out path")
    args = parser.parse_args()
    process_fonts(args.font_in, args.image_out, char2img_list)
