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
char7000 = '一乙二十丁厂七卜八人入儿九匕几了乃刀力又乜三干亍于亏士土工才下寸丈大兀与万弋上小口山巾千乞川亿彳个么久勺丸夕凡及广亡门丫义之尸已巳弓己卫孑子孓也女飞刃习叉马乡幺丰王井开亓夫天元无韦云专丐扎廿艺木五支厅卅不仄太犬区历友歹尤匹厄车巨牙屯戈比互切瓦止少曰日中贝内水冈见手午牛毛气壬升夭长仁仃什片仆仉化仇币仂仍仅斤爪反兮刈介父爻从仑今凶分乏公仓月氏勿风欠丹匀乌勾殳凤卞六文亢方闩火为斗忆计订户讣认讥冗心尹尺夬引丑爿巴孔队办以允邓予劝双书毋幻玉刊末未示击邗戋打巧正扑卉扒邛功扔去甘世艾艽古节艿本术札可叵匝丙左厉丕石右布夯龙戊平灭轧东匜劢卡北占凸卢业旧帅归目旦且叮叶甲申号电田由卟叭只央史叱叽兄叼叩叫叻叨另叹冉皿凹囚四生失矢氕乍禾仨仕丘付仗代仙仟仡仫伋们仪白仔他仞斥卮瓜乎丛令用甩印氐乐尔句匆犰册卯犯外处冬鸟务刍包饥主市庀邝立冯邙玄闪兰半汀汁汇头汈汉忉宁穴宄它讦讧讨写让礼讪讫训必议讯记永司尻尼民弗弘阢出阡辽奶奴尕加召皮边孕发圣对弁台矛纠驭母幼丝匡耒邦玎玑式迂刑邢戎动圩圬圭扛寺吉扣扦圪考托圳老圾巩执扩圹扪扫圯圮地扬场耳芋芏共芊芍芨芄芒亚芝芎芑芗朽朴机权过亘臣吏再协西压厌厍戌在百有存而页匠夸夺夼灰达戍尥列死成夹夷轨邪尧划迈毕至此乩贞师尘尖劣光当吁早吐吓旯曳虫曲团同吕吊吃因吸吗吆屿屹岌帆岁回岂屺则刚网肉凼囝囡钆钇年朱缶氘氖牝先丢廷舌竹迁乔迄伟传乒乓休伍伎伏伛优臼伢伐仳延佤仲仵件任伤伥价伦份伧华仰伉仿伙伪伫自伊血向囟似后行甪舟全会杀合兆企汆氽众爷伞创刖肌肋朵杂夙危旬旭旮旨负犴刎犷匈犸舛各名多凫争邬色饧冱壮冲妆冰庄庆亦刘齐交次衣产决亥邡充妄闭问闯羊并关米灯州汗污江汕汔汲汐汛汜池汝汤汊忖忏忙兴宇守宅字安讲讳讴军讵讶祁讷许讹论讼农讽设访诀聿寻那艮厾迅尽导异弛阱阮孙阵阳收阪阶阴防丞奸如妁妇妃好她妈戏羽观牟欢买纡红纣驮纤纥驯纨约级纩纪驰纫巡佘寿玕\弄玙麦玖玚玛形进戒吞远违韧运扶抚坛抟技坏抔抠坜扰扼拒找批扯址走抄汞坝贡攻赤圻折抓扳坂抡扮抢扺孝坎坍均坞抑抛投抃\坟坑抗坊抖护壳志块抉扭声把报拟抒却劫毐芙芫芜苇邯芸芾芰苈苊苣芽芷芮苋芼苌花芹芥苁芩芬苍芪芴芡芟苄芳严苎芦芯劳克芭苏苡杆杜杠材村杖杌杏杉巫杓极杧杞李杨杈求忑孛甫匣更束吾豆两邴酉丽医辰励邳否还矶奁豕尬歼来忒连欤轩轪轫迓邶忐芈步卤卣邺坚肖旰旱盯呈时吴呋助县里呓呆吱吠呔呕园呖呃旷围呀吨旸吡町足虬邮男困吵串呙呐呗员听吟吩呛吻吹呜吭吣吲吼邑吧囤别吮岍帏岐岖岈岗岘帐岑岚兕财囵囫钉针钊钋钌迕氙氚牡告我乱利秃秀私岙每佞兵邱估体何佐伾佑攸但伸佃佚作伯伶佣低你佝佟住位伴佗身皂伺佛伽囱近彻役彷返佘余希佥坐谷孚妥豸含邻坌岔肝肟肛肚肘肠邸龟甸奂免劬狂犹狈狄角删狃狁鸠条彤卵灸岛邹刨饨迎饩饪饫饬饭饮系言冻状亩况亨庑床庋库庇疔疖疗吝应冷这庐序辛肓弃冶忘闰闱闲闳间闵闶闷羌判兑灶灿灼炀弟沣汪沅沄沐沛沔汰沤沥沌沘沏沚沙汩汨汭汽沃沂沦汹汾泛沧沨沟没汴汶沆沩沪沈沉沁泐怃忮怀怄忧忡忤忾怅忻忪怆忭忱快忸完宋宏牢究穷灾良证诂诃启评补初社祀祃诅识诈诉罕诊诋诌词诎诏诐译诒君灵即层屁屃尿尾迟局改张忌际陆阿孜陇陈阽阻阼附坠陀陂陉妍妩妓妪妣妙妊妖妗姊妨妫妒妞姒妤努邵劭忍刭劲甬邰矣鸡纬纭驱纯纰纱纲纳纴纵驳纶纷纸纹纺纻驴纽纾奉玩玮环玡武青责现玫玠玢玥表玦甙盂忝规匦抹卦邽坩坷坯拓垅拢拔抨坪拣拤拈坫垆坦担坤押抻抽拐拃拖拊者拍顶坼拆拎拥抵坻拘势抱拄垃拉拦幸拌拧坨坭抿拂拙招坡披拨择拚抬拇坳拗耵其耶取茉苷苦苯昔苛苤若茂茏苹苫苴苜苗英苒苘茌苻苓茚苟茆茑苑苞范茓茔茕直苠茀茁茄苕茎苔茅枉林枝杯枢枥柜枇杪杳枘枧杵枚枨析板枞松枪枫构杭枋杰述枕杻杷杼丧或画卧事刺枣雨卖矸郁矻矾矽矿砀码厕奈刳奔奇奄奋态瓯欧殴垄殁郏妻轰顷转轭斩轮软到郅鸢非叔歧肯齿些卓虎虏肾贤尚盱旺具昊昙果味杲昃昆国哎咕昌呵咂畅呸昕明易咙昀昂旻昉炅咔畀虮迪典固忠咀呷呻黾咒咋咐呱呼呤咚鸣咆咛咏呢咄呶咖呦咝岵岢岸岩帖罗岿岬岫帜帙帕岭岣峁刿峂迥岷剀凯帔峄沓败账贩贬购贮囹图罔钍钎钏钐钓钒钔钕钗邾制知迭氛迮垂牦牧物乖刮秆和季委竺秉迤佳侍佶岳佬佴供使侑佰侉例侠臾侥版侄岱侦侣侗侃侧侏凭侨侩佻佾佩货侈侪佼依佯侬帛卑的迫阜侔质欣郈征徂往爬彼径所舍金刽郐刹命肴郄斧怂爸采籴觅受乳贪念贫忿瓮戗肼肤朊肺肢肽肱肫肿肭胀朋肷股肮肪肥服胁周剁昏迩郇鱼兔狉狙狎狐忽弥狗狍狞狒咎备炙枭饯饰饱饲饳饴冽变京享冼庞店夜庙府底庖疟疠疝疙疚疡剂卒郊兖庚废净妾盲放刻於劾育氓闸闹郑券卷单炜炬炖炒炝炊炕炎炉炔沫浅法泔泄沽沭河泷沾泸沮泪油泱泅泗泊泠泜泺泃沿泖泡注泣泫泮泞沱泻泌泳泥泯沸泓沼波泼泽泾治怔怯怙怵怖怦怛怏性怍怕怜怩怫怊怿怪怡学宝宗定宕宠宜审宙官空帘穸穹宛实宓诓诔试郎诖诗诘戾肩房诙戽诚郓衬衫衩祆祎祉视祈诛诜话诞诟诠诡询诣诤该详诧诨诩建肃隶录帚屉居届刷鸤\屈弧弥弦承孟陋戕陌孤孢陕亟降函陔限卺妹姑姐妲妯姓姗妮始帑弩孥驽姆虱迦迢驾叁参迨艰线绀绁绂练驵组绅细驶织驷驸驹终绉驺驻绊驼绋绌绍驿绎经骀贯甾砉耔契贰奏春帮珏珐珂珑玷玳珀顸珍玲珊珉珈玻毒型韨拭挂封持拮拷拱垭挝垣项垮挎垯挞城挟挠垤政赴赵赳贲垱挡拽垌哉垲挺括挢埏郝垍垧垢拴拾挑垛指垫挣挤垓垟拼垞挖按挥挦挪垠拯拶某甚荆茸革茜茬荐荙巷荚荑贳荛荜茈带草茧茼莒茵茴茱莛荞茯荏荇荃荟茶荀茗荠茭茨荒垩茳茫荡荣荤荥荦荧荨茛故荩胡荪荫茹荔南荬荭药柰标栈柑枯栉柯柄柘栊柩枰栋栌相查柙枵柚枳柞柏柝栀柃柢栎枸栅柳柱柿栏柈柠柁枷柽树勃剌郚剅要酊郦柬咸威歪甭研砖厘砗厚砑砘砒砌砂泵砚斫砭砜砍面耐耍奎耷牵鸥虺残殂殃殇殄殆轱轲轳轴轵轶轷轸栎轺轻鸦虿皆毖韭背战觇点虐临览竖尜省削尝哐昧眄眍盹是郢眇眊盼眨昽眈哇咭哄哑显冒映禺哂星昨咴曷昴咧昱昵咦哓昭哔畎畏毗趴呲胄胃贵畋畈界虹虾虼虻蚁思蚂盅咣虽品咽骂哕剐郧勋咻哗囿咱咿响哌哙哈哚咯哆咬咳咩咪咤哝哪哏哞哟峙炭峡峣罘帧罚峒峤峋峥峧帡贱贴贶贻骨幽钘钙钚钛钝钞钟钡钠钢钣钤钥钦钧钨钩钪钫钬钭钮钯御缸拜看矩矧毡氡氟氢牯怎郜牲选适秕秒香种秭秋科重复竽竿笈笃俦段俨俅便俩俪叟垡贷牮顺修俏俣俚保俜促俄俐侮俭俗俘信皇泉皈鬼侵禹侯追俑俟俊盾逅待徊徇徉衍律很须舢舣叙俞弇郗剑逃俎郤爰郛食瓴盆胚胧胨胩胪胆胛胂胜胙胍胗胝朐胞胖脉胫胎鸨葡勉狨狭狮独狯狰狡飐飑狩狱狠狲訇訄逄昝贸怨急饵饶蚀饷饸饹饺饻胤饼峦弯孪娈将奖哀亭亮庤度弈奕迹庭庥疬疣疥疭疮疯疫疢疤庠咨姿亲竑音彦飒帝施闺闻闼闽闾闿阀阁阂差养美羑姜迸叛送类籼迷籽娄前酋首逆兹总炳炻炼炟炽炯炸烀烁炮炷炫烂烃剃洼洁洱洪洹洒洧洌浃柒浇泚浈浉浊洞洇洄测洙洗活洑涎洎洫派浍洽洮染洵洚洺洛浏济洨浐洋洴洣洲浑浒浓津浔浕洳恸恃恒恹恢恍恫恺恻恬恤恰恂恪恼恽恨举觉宣宦宥宬室宫宪突穿窀窃客诫冠诬语扁扃袆衲衽袄衿袂祛祜祓祖神祝祚诮祗祢祠误诰诱诲诳鸩说昶诵郡垦退既屋昼咫屏屎弭费陡逊牁眉胥孩陛陟陧陨除险院娃姞姥娅姨娆姻姝娇姚姽姣姘姹娜怒架贺盈怼羿勇炱怠癸蚤柔矜垒绑绒结绔骁绕骄骅绗绘给绚彖绛络骆绝绞骇统骈耕耘耖耗耙艳挈恝泰秦珥珙顼珰珠珽珩珧珣珞琤班珲敖素匿蚕顽盏匪恚捞栽捕埔埂捂振载赶起盐捎捍埕捏埘埋捉捆捐埚埙损袁挹捌都哲逝耆耄捡挫捋埒换挽贽挚热恐捣垸壶捃捅盍埃挨耻耿耽聂莰茝荸莆恭莽莱莲莳莫莴莪莉莠莓荷莜莅荼莶莩荽获莸荻莘晋恶莎莞莹茛莺真莙鸪莼框梆桂桔栲栳郴桓栖桡桎桢桄档桐桤株梃栝桥桕桦桁栓桧桃桅栒格桩校核样栟桉根栩逑索逋彧哥速鬲豇逗栗贾酐酎酌配酏逦翅辱唇厝孬夏砝砹砸砺砰砧砷砟砼砥砾砣础破硁恧原套剞逐砻烈殊殉顾轼轾轿辀辁辂较鸫顿趸毙致剕龀柴桌鸬虔虑监紧逍党眬唛逞晒晟眩眠晓眙唝哧哳哮唠鸭晃哺哽唔晔晌晁剔晏晖晕鸮趵趿畛蚌蚨蚜蚍蚋蚬畔蚝蚧蚣蚊蝌蚓哨唢哩圃哭圄哦唣唏恩盎唑鸯唤唁哼唧啊唉唆帱崂崃罡罢罟峭峨峪峰圆觊峻贼贿赂赃赅赆钰钱钲钳钴钵钷钹钺钻钼钽钾钿铀铁铂铃铄铅铆铈铉铊铋铌铍铎眚缺氩氤氦氧氨毪特牺造乘敌舐秣秫秤租秧积盉秩称秘透笄笕笔笑笊笫笏笋笆俸倩债俵倻借偌值倚俺倾倒俳俶倬倏倘俱倡候赁恁倭倪俾倜隼隽倞俯倍倦倓倌倥臬健臭射皋躬息郫倨倔衄颀徒徕徐殷舰舨舱般航舫瓞途拿釜耸爹舀爱豺豹奚鬯衾鸰颁颂翁胯胰胱胴胭脍脎脆脂胸胳脏脐胶脑胲胼朕脒胺脓鸱玺鱽鸲逛狴狸狷猁狳猃狺逖狼卿狻逢桀鸵留袅眢鸳皱饽饿馀馁凌凇凄栾挛恋桨浆衰勍衷高亳郭席准座症疳疴病疽疸疾痄斋疹痈疼疱疰痃痂疲痉脊效离衮紊唐凋颃瓷资恣凉站剖竞部旁旆旄旅旃畜阃阄阅阆羞羔恙瓶桊拳敉粉料粑益兼朔郸烤烘烜烦烧烛烟烨烩烙烊剡郯烬递涛浙涝浡浦涑浯酒涞涟涉娑消涅涠浞涓涢涡浥涔浩海浜涂浠浴浮涣浼涤流润涧涕浣浪浸涨烫涩涌涘浚悖悚悟悭悄悍悝悃悒悔悯悦悌悢悛害宽宸家宵宴宾窍窅窄容窈剜宰案请朗诸诹诺读扅诼冢扇诽袜袪袒袖袗袍袢被袯祯祧祥课冥诿谀谁谂调冤谄谅谆谇谈谊剥恳展剧屑屐屙弱陵陬勐奘疍牂蚩祟陲陴陶陷陪烝姬娠娱娌娉娟娲恕娥娩娴娣娘娓婀砮哿畚通能难逡预桑剟绠骊绡骋绢绣验绤绥绦骍继绨骎骏邕鸶赊彗耜焘舂琎球琏琐理琇麸琉琅捧掭堵揶措描埴域捺掎埼掩埯捷捯排焉掉掳掴埸堌捶赦赧推堆捭埠晳掀逵授捻埝堋教堍掏掐掬鸷掠掂掖培掊接堉掷掸控捩掮探悫埭埽据掘掺掇掼职聃基聆勘聊聍娶菁菝著菱萁菥菘堇勒黄萘萋勚菲菽菖萌萜萝菌萎萸萑菂菜棻菔菟萄萏菊萃菩菼菏萍菹菠菪菅菀萤营萦乾萧菰菡萨菇械梽彬梵梦婪梗梧梾梢梏梅觋检桴桷梓梳棁梯桫棂桶梭救啬郾匮曹敕副豉票鄄酝酞酗酚厢厣戚戛硎硅硭硒硕硖硗硐硚硇硌鸸瓠匏奢盔爽厩聋龚殒殓殍盛赉匾雩雪辄辅辆堑龁颅虚彪雀堂常眶眭唪眦啧匙晡晤晨眺眵睁眯眼眸悬野圊啪啦喏喵啉勖曼晦晞晗晚冕啄啭啡畦趼趺距趾啃跃啮跄略蚶蛄蛎蛆蚰蚺蛊圉蚱蚯蛉蛀蛇蛏蚴唬累鄂唱患啰唾唯啤啥啁啕唿啐唼唷啴啖啵啶啷唳啸啜帻崖崎崦崭逻帼崮崔帷崟崤崩崞崇崆崛赇赈婴赊圈铐铑铒铕铗铘铙铚铛铜铝铞铟铠铡铢铣铤铥铧铨铩铪铫铭铬铮铯铰铱铲铳铴铵银铷矫氪牾甜鸹秸梨犁稆秽移秾逶笺筇笨笸笼笪笛笙笮符笱笠笥第笳笤笾笞敏偾做鸺偃偕袋悠偿偶偈偎偲傀偷您偬售停偻偏躯皑兜皎假衅鸻徘徙倘得衔舸舻舳盘舴舶船鸼舷舵斜龛盒鸽瓻敛悉欲彩领翎脚脖脯豚脶脸脞脬脱脘脲朘匐鱾象够逸猜猪猎猫猗凰猖猡猊猞猄猝斛觖猕猛馗祭馃馄馅馆凑减鸾毫孰烹庶庹麻庵庼庾庳痔痍疵痊痒痕廊康庸鹿盗章竟翊商旌族旎旋望袤率阇阈阉阊阋阌阍阎阏阐着羚羝羟盖眷粝粘粗粕粒断剪兽敝焐焊烯焓焕烽焖烷烺焌清渍添渚鸿淇淋淅淞渎涯淹涿渠渐淑淖挲淌淏混淠涸渑淮淦淆渊淫淝渔淘淳液淬涪淤淡淙淀涫深渌涮涵婆梁渗淄情惬悻惜惭悱悼惝惧惕惘悸惟惆惚惊惇惦悴惮惋惨惯寇寅寄寂逭宿窒窑窕密谋谌谍谎谏扈皲谐谑裆袱袼裈裉祷祸祲谒谓谔谕谖谗谙谚谛谜谝逮逯敢尉屠艴弹隋堕郿随蛋隅隈粜隍隗隆隐婧婊婞婳婕娼婢婚婵婶婉胬袈颇颈翌恿欸绩绪绫骐续骑绮绯绰骒绲绳骓维绵绶绷绸绹绺绻综绽绾绿骖缀缁巢耠琫琵琴琶琪瑛琳琦琢琥琨靓琼斑琰琮琯琬琛琚辇替鼋揳揍款堪堞搽塔搭塃揸堰揠堙揩越趄趁趋超揽提堤揖博揾颉揭喜彭揣塄揿插揪搜煮堠耋揄援搀蛰蛩絷塆裁揞搁搓搂搅揎壹握摒揆搔揉掾葜聒斯期欺联葑葚葫靰靸散葳惹蒇葬蒈募葺葛蒉葸萼蓇萩董葆葩葡敬葱蒋葶蒂蒌葓蒎落萱葖韩戟朝葭辜葵棒楮棱棋椰植森棼焚椟椅椒棹棵棍椤棰椎棉椑鹀赍棚椋椁棬棕棺榔楗棣椐椭鹁惠惑逼覃粟棘酣酤酢酥酡酦鹂觌厨厦硬硝硪硷确硫雁厥殖裂雄殚殛颊雳雯辊辋椠暂辌辍辎雅翘辈斐悲紫凿黹辉敞棠牚赏掌晴睐暑最晰量睑睇鼎睃喷戢喋嗒喃喳晶喇遇喊喱喹遏晷晾景喈畴践跖跋跌跗跞跚跑跎跏跛跆遗蛙蛱蛲蛭蛳蛐蛔蛛蜓蛞蜒蛤蛴蛟蛘蛑畯喁喝鹃喂喟斝喘啾嗖喤喉喻喑啼嗟喽嗞喧喀喔喙嵌嵘嵖幅崴遄詈帽嵎崽嵚嵬嵛翙嵯嵝嵫幄嵋赋赌赎赐赑赔黑铸铹铺铻铼铽链铿销锁锃锄锂锅锆锇锈锉锊锋锌锎锏锐锑锒锓锔锕甥掣掰短智矬氰毳毯氮毽氯犊犄犋鹄犍鹅颋剩嵇稍程稀黍桴税稂筐等筘筑策筚筛筜筒筅筏筵筌答筋筝傣傲傅傈舄牍牌傥堡集焦傍傧储遑皓皖粤奥傩遁街惩御徨循舾艇舒畲弑逾颌翕釉番释鹆禽舜貂腈腊腌腓腆腴脾腋腑腙腚腔腕腱腒鱿鲀鲁鲂鲃颍猢猹猩猥猬猾猴飓觞觚猸猱惫飧然馇馈馉馊馋亵装蛮脔就敦裒庾斌痣痨痦痘痞痢痤痪痫痧痛鄌赓竦童瓿竣啻颏鹇阑阒阔阕善翔羡普粪粞尊奠遒道遂孳曾焯焜焰焙焱鹈湛港渫滞湖湘渣渤湮湎湝湨湜渺湿温渴渭溃湍溅滑湃湫溲湟溆渝湲湾渡游溠溇湔滋湉渲溉渥湄滁愤慌惰愠惺愦愕惴愣愀愎惶愧愉愔慨喾割寒富寓窜窝窖窗窘寐谟扉遍雇扊裢裎裣裕裤裥裙祾祺祼谠禅禄幂谡谢谣谤谥谦谧塈遐犀属屡孱弼强粥巽疏隔骘隙隘媒媪絮嫂媛婷媚婿巯毵翚登皴婺骛缂缃缄缅彘缆缇缈缉缌缎缏缑缒缓缔缕骗编缗骙骚缘飨耢瑟瑚鹉瑁瑞瑰瑀瑜瑗瑄瑕遨骜瑙遘韫魂髡肆摄摸填搏塥塬鄢趔趑摅塌摁鼓摆赪携塮蜇搋搬摇搞搪塘搒搐搛搠摈彀毂搌搦摊搡聘蓁戡斟蒜蓍鄞勤靴靳靶鹊蓐蓝墓幕蓦鹋蒽蓓蓖蓊蒯蓟蓬蓑蒿蒺蓠蒟蒡蓄蒹蒴蒲蒗蓉蒙蓂蓥颐蒸献蓣楔椿楠禁楂楚楝楷榄想楫榀楞楸椴槐槌楯榆榇榈槎楼榉楦概楣楹椽裘赖剽甄酮酰酯酪酩酬蜃感碛碍碘碓碑硼碉碎碚碰碇碗碌碜鹌尴雷零雾雹辏辐辑辒输督频龃龄龅龆觜訾粲虞鉴睛睹睦瞄睚嗪睫韪嗷嗉睡睨睢雎睥睬嘟嗜嗑嗫嗬嗔鄙嗦嗝愚戥嗄暖盟煦歇暗暅暄暇照遢暌畸跬跨跶跷跸跣跹跳跺跪路跻跤跟遣蛸蜈蜎蜗蛾蜊蜍蜉蜂蜣蜕畹蛹嗣嗯嗅嗥嗲嗳嗡嗌嗍嗨嗤嗵嗓署置罨罪罩蜀幌嵊嵩嵴骰锖锗错锘锚锛锜锝锞锟锡锢锣锤锥锦锧锨锪锫锩锬锭键锯锰锱矮雉氲犏辞歃稞稚稗稔稠颓愁筹筠筢筮筻筲筼筱签简筷毁舅鼠牒煲催傻像躲鹎魁敫僇衙微徭愆艄觎毹愈遥貊貅貉颔腻腠腩腰腼腽腥腮腭腹腺腧鹏塍媵腾腿詹鲅鲆鲇鲈鲉鲊稣鲋鲌鲍鲏鲐肄猿颖鹐飔飕觥触解遛煞雏馌馍馏馐酱鹑禀亶廒瘃痱痹痼廓痴痿瘐瘁瘅痰瘆廉鄘麂裔靖新鄣歆韵意旒雍阖阗阘阙羧豢誊粳粮数煎猷塑慈煤煳煜煨煅煌煊煸煺滟溱溘滠满漭漠滢滇溥溧溽源滤滥裟溻溷溦滗滫溴滏滔溪滃溜滦漓滚溏滂溢溯滨溶滓溟滘溺滍粱滩滪愫慑慎慥慊誉鲎塞骞寞窥窦窠窣窟寝谨裱褂褚裸裼裨裾裰禊福谩谪谫谬群殿辟障媾嫫媳媲嫒嫉嫌嫁嫔媸叠缙缜缚缛辔缝骝缟缠缡缢缣缤骟剿耥璈静碧瑶璃瑭瑢獒赘熬觏慝嫠韬髦墈墙摽墟墁撂摞嘉摧撄赫截翥踅誓銎摭墉境摘墒摔撇榖撖摺綦聚蔫蔷靺靼鞅靽鞁靿蔌慕暮摹蔓蔑薨蔸蓰蔹蔡蔗蔟蔺戬蔽蕖蔻蓿蔼斡熙蔚鹕兢嘏蓼榛榧模槚槛榻榫槜榭槔榴槁榜槟榨榕槠榷榍歌遭僰酵酽酾酲酷酶酴酹酿酸厮碶\碡碟碴碱碣碳碲磋磁碹碥愿劂臧豨殡需霆霁辕辖辗蜚裴翡雌龇龈睿裳颗夥瞅瞍睽墅嘞嘈嗽嘌嘁嘎暧暝踌踉跽踊蜻蜞蜡蜥蜮蜾蝈蜴蝇蜘蜱蜩蜷蝉蜿螂蜢嘘嘡鹗嘣嘤嘚嘛嘀嗾嘧罴罱幔嶂幢赙罂赚骷骶鹘锲锴锶锷锸锹锻锽锾锵锿镀镁镂镃镄镅舞犒舔稳熏箐箦箧箍箸箨箕箬算箅箩箪箔管箜箢箫箓毓舆僖儆僳僚僭僬劁僦僮僧鼻魄魅魃魆睾艋鄱貌膜膊膈膀膑鲑鲔鲙鲚鲛鲜鲟疑獐獍飗觫雒孵夤馑馒銮裹敲豪膏塾遮麽廙腐瘩瘌瘗瘟瘦瘊瘥瘘瘙廖辣彰竭韶端旗旖膂阚鄯鲞精粼粹粽糁歉槊鹚弊熄熘熔煽熥潢潆潇漤漆漕漱漂滹漫漯漶潋潴漪漉漳滴漩漾演澉漏潍慢慷慵寨赛搴寡窬窨窭察蜜寤寥谭肇綮谮褡褙褐褓褛褊褪禚谯谰谱谲暨屣鹛隧嫣嫱嫩嫖嫦嫚嫘嫜嫡嫪鼐翟翠熊凳瞀鹜骠缥缦缧骡缨骢缩缪缫慧耦耧瑾璜璀璎璁璋璇璆奭撵髯髫撷撕撒撅撩趣趟撑撮撬赭播墦擒撸鋆墩撞撤撙增撺墀撰聩聪觐鞋鞑蕙鞒鞍蕈蕨蕤蕞蕺瞢蕉劐蕃蕲蕰蕊赜蔬蕴鼒槿横樯槽槭樗樘樱樊橡槲樟橄敷鹝豌飘醋醌醇醉醅靥魇餍磕磊磔磙磅碾磉殣慭\震霄霉霈辘龉龊觑瞌瞒题暴瞎瞑嘻嘭噎嘶噶嘲颙暹嘹影踔踝踢踏踟踬踩踮踣踯踪踺踞蝽蝶蝾蝴蝻蝠蝰蝎蝌蝮螋蝗蝓蝣蝼蝤蝙噗嘬颚嘿噍噢噙噜噌嘱噀噔颛幞幡嶓幢嶙嶝墨骺骼骸镊镆镇镈镉镋镌镍镎镏镐镑镒镓镔靠稽稷稻黎稿稼箱箴篑篁篌篓箭篇篆僵牖儇儋躺僻德徵艘磐虢鹞鹟膝膘膛滕鲠鲡鲢鲣鲥鲤鲦鲧鲩鲪鲫鲬橥獗獠觯鹠馓馔熟摩麾褒廛瘛瘼瘪瘢瘤瘠瘫齑鹡凛颜毅羯羰糊糇遴糌糍糈糅翦遵鹣憋熜熵熠潜澍澎澌潵潮潸潭潦鲨潲鋈潟澳潘潼澈澜潽潺澄潏懂憬憔懊憧憎寮窳额谳翩褥褴褫禤谴鹤谵憨熨慰劈履屦嬉勰戮蝥豫缬缭缮缯骣畿耩耨耪璞璟靛璠璘聱螯髻髭髹擀撼擂操熹甏擐擅擞磬鄹颞蕻鞘燕黇颟薤蕾薯薨薛薇檠擎薪薏蕹薮薄颠翰噩薜薅樾橱橛橇樵檎橹橦樽樨橙橘橼墼整橐融翮瓢醛醐醍醒醚醑觱磺磲赝飙殪霖霏霓霍霎錾辙辚臻冀餐遽氅瞟瞠瞰嚄嚆噤暾曈蹀蹅踶踹踵踽嘴踱蹄蹉蹁蹂螨蟒蟆螈螅螭螗螃螠螟噱器噪噬噫噻噼幪罹圜鹦赠默黔镖镗镘镚镛镜镝镞镠氇氆赞憩穑穆穄篝篚篥篮篡簉篦篪篷篙篱盥儒劓翱魉魈邀徼衡歙盦膨膪膳螣膦膙雕鲭鲮鲯鲰鲱鲲鲳鲴鲵鲷鲸鲺鲹鲻獴獭獬邂憝亸鹧磨廨赟癀瘭瘰廪瘿瘵瘴癃瘾瘸瘳斓麇麈凝辨辩嬴壅羲糙糗糖糕瞥甑燎燠燔燃燧燏濑濒濉潞澧澡澴激澹澥澶濂澼憷懒憾懈黉褰寰窸窿褶禧壁避嬖犟隰嬗鹨翯颡缰缱缲缳缴璨璩璐璪戴螫擤壕擦觳罄擢藉薹鞡鞠藏薷薰藐藓藁檬檑檄檐檩檀懋醢翳繄礁礅磷磴鹩霜霞龋龌豳壑黻瞭瞧瞬瞳瞵瞩瞪嚏曙嚅蹑蹒蹋蹈蹊蹓蹐蟥螬螵疃螳螺蟋蟑蟀嚎嚓羁罽罾嶷赡黜黝髁髀镡镢镣镤镥镦镧镨镩镪镫罅穗黏魏簧簌篾簃篼簏簇簖簋繁鼢黛儡鹪鼾皤魍徽艚龠爵繇貘邈貔臌朦臊膻臁臆臃鲼鲽鲾鳀鳁鳂鳃鳄鳅鳆鳇鳈鳉鳊獯螽燮鹫襄糜縻膺癍癌麋辫赢糟糠馘燥懑濡濮濞濠濯懦豁蹇謇邃襕襁臀檗甓臂擘孺隳嬷翼蟊鹬鍪骤鏊鳌鬶鬈鬃瞽藕鞯鞨鞭鞫鞧鞣藜藠藤藩鹲檫檵覆醪蹙礞礓礌燹餮瞿瞻曛颢曜躇蹦鹭蹢蹜蟛蟪蟠蟮嚚嚣鹮黠黟髅髂镬镭镯镰镱馥簠簟簪簦鼫鼬鼩雠艟翻臑鳍鳎鳏鳐鳑鹱鹰癞癔癜癖糨冁蹩瀑瀍瀌鎏懵襟璧戳彝邋鬏攉攒鞲鞴藿蘧孽蘅警蘑藻麓攀醭醮醯礤酃霪霭黼曝嚯蹰蹶蹽蹼蹯蹴蹾蹲蹭蹿蹬蠖蠓蠋蟾蠊巅黢髋髌镲籀簸籁簿鳘齁魑艨鼗鳓鳔鳕鳗鳙鳚蟹颤靡癣麒鏖瓣蠃羸羹鳖爆瀚瀣瀛襦谶襞疆骥缵瓒鬓壤攘馨蘩蘖蘘醵醴霰颥酆耀矍曦躁躅蠕鼍嚼嚷巍巉黩黥镳镴黧籍纂鼯臜鳜鳝鳞鳟獾魔糯灌瀹瀵譬孀骧耰蠢瓘鼙醺礴礳霸露霹颦曩躏黯髓鼱鳡鳢癫麝赣夔爝灏禳鐾羼蠡耲耱懿韂蘸鹳蘼囊霾氍饕躔躐髑镵镶穰鳤瓤饔鬻鬟趱攫攥颧躜罐鼹鼷癯麟蠲矗蠹醾躞衢鑫灞襻纛鬣攮囔馕戆蠼爨齉埵罣'
char2img_list = char7000
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
                    missing_chars_string = ''.join(missing_chars)
                    font2image(font_path, image_file_path, missing_chars_string, 128)
                    # for missing_char in missing_chars:
                    #     print(f"Regenerating image for missing character: {missing_char}")
                    #     font2image(font_path, image_file_path, missing_char, 128)

        except Exception as e:
            print(e)
    # remove_empty_floder(image_file_path)


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
