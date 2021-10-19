# coding=utf-8
# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Traditional and simplified Chinese conversion, a simplified character may correspond to multiple traditional characters.
"""
simplified_charcters = '制咖片型超声盘鉴定仔点他命书歌粉巾字帐恤手指记忆棒形转弯沟光○〇㐄㐅㐆㐌㐖毒㐜㐡㐤㐰㐺㑇㑳㒳㒸㔾㗂㗎㝵㞎㞙㞞以㢲㢴㤅㥁㥯㨗㫺㬎㮎㮚㮸㲋㲱㲾㳮涧㵪㶸㷖㷭㹢㹴犬㺢狓㺵碗㽮㿝䍃䔢䖟䖸䗈䗥䗪䝓射䥯䦉䯝鲃鱼䲔䳗鹅䵹鼄䶑一对应映射丁不识下儿子做二休世丘之貉并中台原则串为甚谓干净了百事无成八变五十些人得道鸡升天代如并来去个国政策劲幽灵在欧洲游荡接样萝卜坑侧化传价元论醇共再准刀两断切分耕耘收获钱货物向看旧就绪险刻千金动劳永逸匙零夜半卡通回复返影踪反常态口咬气句话同吐快吹周味呼诺呜品红锅哄而散起唱和问三知生熟团漆黑火糟堆场空块面塌糊涂尘染壁厢夔已足多情露水大早到晚夫妻当关万莫开失古恨套所料既往孔见提师要家主审寸阴难买斗牛小撮部阵局展身层巴掌帆风顺席地带过年计于春头载四季期被蛇怕井绳度愿式份弹顷深前律径心意念差愁孤行俱全房厅交遮打技长把抓死拿眼泪鼻涕钥锁折段抿拍即合扫排掬挥拨拥上入击洞掷揽改故辙败文值名斑方面旁族日秋餐隔雅里终父旦时晌会霎间晃暴寒曝更月望垠际朝夕本正经利杯羹东西板枝独秀根筋杆进条龙服务概模次函数又性程总付步脚印趋登毛拔呵氧氮碳决雌雄波未平派谎言流清楚白准溜烟潭有获闻是处降琴鹤甲病发可拾沙目然了直以相眨穿睹瞥瞬矢的解石鸟神教秉虔诚秘种窝蜂穷窍笑置笔苟勾销抹杀煞等奖箍节吃箭仇双雕诗筹箩筐系列纸级士官统丝毫挂维网尽线微吭响股脑胎脉承腔臂力致效资源址器举功投般说讲规贸易叶障着慎满皆输号木电池衣倾钟高低视仁觉醒览遗角银币触溃九鼎蔽抄出驷马追重语破贫洗贯走路安蹴至几蹶振跃役胆汗较辈轮辞赞退六连遍递边针血锤音错门思闪真倒项栽雾类保护川先惊乍体哄鳞爪鸣滴泡邻域党专鼓作齐炒丑烯亥克内酯冬加奴卯肝炎基尺梁街裤镐客宠庭巳汝昌烷玲磊糖肇酉醛啷青县韪良香骨鲷丂七集河市弦喜嘴张舌堵区工业姊妹星架构巧彩扭歪拼凑余热曜武州爷浮屠美乡老阶树荤素碎落能魄鳃鳗珠丄丅丆万俟丈尚摸母娘量管群亚虎必我堂令申件装伏位博侠义界表女墟台戏臭皮匠胜诸葛亮赛顶倍催请运算包立叉戟离疫苗土史志演围揭瓦晒夷姑婆帝村宝烂尖杉碱屉桌山岔岛由纪峡坝库镇废从德后拗汤治旬食明昧曹朋友框栏极权幂曲归依猫民氟硼氯磷铁江侗自旅法司洋浦梅园温暖湾焦班幸用田略番叠皇炮捶硝苯酸腺苷棱草镜穗跳远索锦纲聚氰胺联店胚膲爱色堇紫罗兰芝茶饭菱云虫藏藩乱叛苏亲债凳学座恐恋柱测肌腹衩锥系貂企乌跪叩军车农题迭都甘油屯奏键短阿姨陪姐只顾茅庐槽驾魂鲜鹿页其菜单乘任供势午齿汉组织吊调泻唇坡城报坟外夸将尉建筑岸岗公床扬新剑升杭林栗校楼标款汽社浣海商馆剧院钢华港机械广媒环球融第医科证券综财乐育游涨犹岭疏瘾睑确兵领导缴肢膛船艾瑟尔苍蔡虞效衫覆访诉课谕议轨述野钩限敌鞋颌颔颚饶首龈站例修凡划垂届属崽颏厨拜挫摆放旋削棋榻槛礼沉注滑营狱画确仪聘花葬诏员跌辖周达酒锚闸陷陆雨雪飞威丌于丹久乏予理评产亢卑亦乎舞己悲矩圆词害志但住佞佳便俗信票案幅翁倦伦假偏倚斜亏鬼敲停备伤脾胃仅此像俭匮免宜穴焉戴兼容许冻伯仲负彼昼皂轩轾实刊划颠卫战哥比省非好黄饰别拘束掩奶睬选择摇扰烦苦枚写协厌及格受欢迎约只估侵犯割状告或缺抗拒挽撤救药喻磨灭端倪少逆逾越避靠适吉誉吝玉含延咎歹听啻渊善谋均匀堪忍够太惹妙妥妨孕症孝术室完纳推冠积宣疑辩栗碴称屈挠屑干涉衡待很忙恶忿怎么怠急耻恭息悦惑惜惟想愉愧怍慌愤启懂懈怀材才紧招认扣抵拉舍也罢插揣冒搭撞南墙扩核支攻敢雷攀敬里吗需景智暇曾罪遇朽枉止况竞争辱求愈渝溶济左右袒困补爽特寂寞示弱找谢畏强疾徐痛痒冤符眠睦瞅董何厚云措活疲羞者轻玻璃祥兆禁移稂莠稳佛换答简结果盟绝缕途给谈否羁翼耐肖胫毋宁兴舒若菲莱痕迹窠臼虚衰脸兔撒鹰棺范该详讳抬泰让须眉象众赀账费灰赖奇虑训辍辨菽麦辛近送透逞徒速续逮捕遂遑违逊斧钺艰醉锈随观弃显饱脂肪使丏丐帮丒且慢末丕替桃宗王尊凉爵各图屋脊粮署录坛吾禄职胄袭君厦丗北壑桐疹损逢陵鹬丙寅戌氨腈唑纶辰酮脱氢酶醚丞丢现掉纱帽弄扯炮碗丠両丣坐存激肩臻蒂莲悖序驱丨丩丫挺杈髻鬟细介俄伊犁京尼布订普渡央委监察检查剂圈设警队斯督剩震境航舶革防托播促质版蝾螈锋研艺历残消频谱精密制造陲邮候埔坚压坜凹汇执府究邦俘摄寮彬狼岳肺肿庸英讯诊埋粒胞括控码韩暑枪枢砥澳哇牟寿甸钻探篇签缀缝继耳肯照妇埃悬璧轴柜台辣搁浅邪跑纤阮阳私囊魔丮丰姿采丱烧丳丵丶丷丸参寨朗桂瑞砂衷霞貌凤仆舰因嫌宰峰干络牌持旨祭祷簿编罚宾办丼丿乀乂乃乄仰慕盛旷留考验阔乆乇么丑麽乊湖燃乑乒乓乕乖僻忤戾离谬迕乗危肥劫除隙浪婿乙炔肠酰吡咯盐乚乛乜嘢卿玄宫尾狐龟塔嶷兄弟泉章霄钉耙乞扎哀怜恕讨乢乣乤乥乧乨乩童乪乫乭乳晕汁液瑶浆牙癌突窦罩腐胶猪酪蛋糕菌瘤乴乵乶乷乸乹乺乼乾俸冰嘉哕嚎坤妈尸垒旱枯涸俐渴潮涩煸豆燥爹瘦瘪癣瞪袋脆姜贝隆馏乿亀亁叫咕攘扔搞男砸窜蓬麻亃亄亅却亇迟典今临繁累卵奉婚聪躬巨与迁添裂副宿岁怪恶尕仑愣杆硅硫钛铀锰芑杂异钠砷胂磺琥珀舱棍簧胡茬盗浩盆贩郎腿亍洪亐互欠助勉惠操斥诿系户译亓墓碑刑铃卅渠缤纷斗米旗宪钒灯徽瘟祖拳福谷丰脏腑绑肉腌苓蕴桥铺霸颜闹判喷冈底蛙陉矿亖亘亜罕们娜桑那努哈喀弗烈曼松森杜氏杯奥琛敦戊穆圣裔汇薛孙亟亡佚虏羊牢奋释卷卸契媾感额睫缠谊趾塞挤纽阻还配驰庄亨洛祚亪享津沪畿郊慈菴枇杷膏亭阁锃丽亳亶亹诛初责翻疯偶杰丛稠妖拖寰居吸授慧蜗吞壮魅狗矛盾益渣患忧稀描猿梦暂涯畜祸缘沸搜引擎臣横纭谁混援蒸兽狮税剖亻亼亽亡什献刹邡么仂仃仄仆富怨仈仉毕昔晨壳绍仍仏仒仕宦仗欺恃腰叹叹炬梓讫施仙后琼逝仚仝仞仟悔仡佬偿填泊拓扑簇羔购顿钦佩发棻阃驭养亿儆尤借帧赈凌叙帖李柔刚沃眦睚戒讹取飨读仨仫仮著泳卧躺韶夏裁仳仵唯贤凭钓诞仿似宋佛讽伀硕盼鹅伄儅伈伉俪柯始娃迈戈坦堡帕茨萨庙玛莉莎藤霍姆伋伍奢胥廷芳豪伎俩侍汛勒希羲雏伐憩整谟闲闲伕伙伴颐伜伝伢叔恒兹恩翰伱伲侣伶俜悧鼬伸懒缩喇叭伹伺伻伽倻辐伾似佃伫布乔妮墨佉卢佌贷劣廉昂档浓矮伞洼缓耗胸谷迷挡率龋宅沫舍疗佐贰佑占优据铧尝呢须鲁晓佗佘余坪寺瓜铳僧蒙芒陀龛哼呕坊奸孽弊揖祟茧缚誓贼佝偻瞀佟你夺赶佡佢佣佤佧贾佪佫佯佰佱洁绩酿肴佴卷佶佷佸佹佺佻佼佽佾具唤窘坏娱怒慨硬习惯聋膨胀蔓骇贵痹侀侁侂侃侄侅鸿燕侇侈糜靡侉侌妾侏儒仓鼠侐侑侔仑侘侚链侜偎傍钴循柳葫芦附価侮骂蔑侯岩截蚀局贴壶嬛宴捷携桶笺酌俣狭膝狄俅俉俊俏俎俑俓俔谚俚俛黎健呈固墒增守康箱湿祐镖镳杠盒靖膜龄俞豹猎噪孚封札筒托衍鸽剪撰稿炼厂禊练缮葺俯瞰撑冲效俳俴俵俶俷俺备俾伥倂倅储卒惶敷猝逃颉蓄崇隐倌倏忽刺蜡烛噍嚼坍扁抽毙葱楣灌灶粪背薮卖赔闭霉腾倓倔幸倘倜傥倝借箸挹浇阅倡狂倢倣値倥偬倨傲倩匡嗣冲柝珍倬倭寇猩倮倶倷倹勤赞偁偃充伪吏嗓寐惺扮拱芫茜藉虢钞偈伟晶偌宕距析滤殿疼瘫注颇偓偕鸭歇滞偝偟偢忘怡旺偨偩逼偫偭偯偰偱偲侦缉蹄偷减惰漏窥窃偸偺迹傀儡傅傈僳骂篱傎奎琳迪叟芭傒傔傕伧悉荒傜傞傢傣芽逼佣婢傮睨寄檄诵谣颂伛担辜弓惨蒿悼疤傺傻屄臆巢泄箧羡盖轧颓傿㑩僄僇佥僊働僎侨僔僖僚僝伪僣僤侥僦猴偾僩僬僭僮僯僰雇僵殖签静僾僿征陇儁侬儃儇侩朴薄儊儋儌儍傧儓俦侪拟尽儜儞儤儦儩汰哉寡渥裕酷儭儱罐儳儵儹傩俨儽兀臬臲鹫允勋勋宙宵帅憝彝谐嫂阋畅沛溢盈饥赫凶悍狠猛顽愚妣斩秦遣鞭耀敏荣槃泽爆碟磁秃缆辉霁卤朵娄孜烽酱勃汀箕裘钳耶蒙蕾彻兑软遭黜兎児韵媳爸兕觥兖兙兛兜售鍪肚兝兞兟兡兢兣樽殓涅睡禀籍赘泌啡肽奸幕涵涝熵疚眷稃衬讧赴焕椒歼植跏没试误猜栖窗肋袖颊兪卦撇胡岐廓轿疸枫茴珑厕秩募勺吨寓斤历亩迫筷厘最淫螺韬兮宽匪筛襄赢轭复兲诈刃堰戎痞蚁饷它冀铸冂冃円冇冉册嫁厉砺竭醮冏牧冑冓冔冕冖冗冘冞冢窄抑诬冥冫烘菇蛰冷凝坨橇淇淋炭饼砖碛窖醋雕雹霜冱冶炉艳嘲峻滩淡漠煖飕饮冼冽凃凄怆梗凅凇净凊凋敝蒙凔凛遵汞脢凞几凢処凰凯凵凶焰凸折刷纹预丧喽奔巡榜殡芙蓉租笼辑鞘萃凼锯镬刁蛮刂娩崩批拆摊掰蘖骤歧颗秒袂赃勿嘱忌磋琢肤刈羽刎讼戮舂桨艇刓刖霹雳刜创犊刡恙墅帜筵致劫劫刨昏默攸尿欲熏润薰圭删刮痧铲刱刲刳刴刵踏磅戳柏槐绣芹苋猬舟铭鹄鹜劫剁剃辫刭锉履铅克剌姻咽哨廊掠桅沿召瞻翅赵卜渺茫郭剒剔剕沥剚愎毅讷才剜剥啄采剞剟剡剣剤䌽剐肾驶黏剰袍剀紊铲剸剺剽剿劁劂札劈啪柴扳啦刘奭姥夼昫涓熙禅禹锡翔雁鹗刽刿弩柄蜻蛉劒劓劖劘劙澜篑赏矶釜晋甜薪逐劦熔纣虐赤囚劬劭労劵效劻劼劾峭艮勅勇励勍勐腊脖庞漫饲荡粥辄勖勗勘骄馁碌泮雇捐竹骑殊阱绩朴恳谨剿勧勩勯勰劢勋勷劝惩慰诫谏勹芡践阑匁庇拯粟扎袱裹饺匆遽匈匉匊匋匍匐茎匏匕妆痰脓蛹斋苑烤蹈塘羌熊阀螳螂疆碚竿纬荷茵邙魏匚匜匝匟扶稷匣匦拢匸匹耦匽匾匿卂叮疮禧轸堤棚迢钧炼卄卆遐卉瓷盲瓶当胱腱裸卋卌卍卐怯污贱鄙龌龊陋卓溪唐梯渔陈枣泥漳浔涧梨芬谯赡辕迦郑単驴弈洽鳌卛占筮卝卞卟吩啉屎翠厄卣卨卪卬卮榫袄玺绶钮蚤惧殆笃耸卲帘帙绕恤卼卽厂厎厓厔厖厗奚厘厍厜厝谅厕厤厥厪腻孢厮厰厳厣厹厺粕垢芜菁厼厾叁悟茸薯叄吵笄悌哺讥坫垄弧芯杠潜婴刍袁诘贪谍煽馈驳収岳缔灾贿骗叚叡吻拦蘑蜜诀燧玩砚筝椎蔺铜逗骊另觅叨唠谒杵姓喊嚷嚣咚咛塑寻恼憎擦只泣渗蝠叱吒咄咤喝籀黛舵舷叵叶铎懿昭穰苴辽叻叼吁堑嫖赌瞧爬众抒吅吆夥卺橡涤抱纵摩郡唁坠扇篮膀袜颈吋忾谘酬哭妓媛暗表缰迩妃羿絮蕃浑拐葵暮隅吔吖啶嗪戚吜啬噬咽吟哦咏吠吧唧嗒咐吪隽咀征燐苞茹钙哧吮吰吱嘎吲哚吴栋娇窟孟箫忠晗淞阖闾趼宇呐睛嘘拂捧疵熄竽笛糠吼吽呀吕韦蒙呃呆笨呇贡呉罄呋喃呎呏呔呠呡痴呣呤呦呧瑛眩扒晬淑姬瑜璇鹃呪呫哔嚅嗫呬呯呰呱呲咧噌钝呴呶呷呸呺呻哱咻啸噜吁坎坷逻呿咁咂咆哮咇咈咋蟹煦珅蔼咍咑咒诅咔哒嚓咾哝哩喱咗咠咡咢咣咥咦咨嗟询咩咪咫啮啮咭咮咱咲咳呛嗽咴啕咸咹咺呙喉咿婉恸悯赋矜绿茗蓝哂抢瞒哆嗦啰噻啾滨彗哋哌哎唷哟哏哐哞哢哤哪里哫啼喘哰哲萎蚌哳咩哽哿呗唅唆唈唉唎唏哗尧棣殇璜睿肃唔睇唕吣唞唣喳唪唬唰喏唲唳唵嘛唶唸唹唻唼唾唿啁啃鹦鹉啅埠栈榷祺铺鞅飙啊啍啎啐啓啕啖啗啜哑祈啢衔啤啥啫啱啲啵啺饥啽噶昆沁喁喂喆裙喈咙喋喌喎喑喒喓喔粗喙幛庆滋鹊喟喣喤喥喦喧骚喨喩梆吃葡萄喭驼挑吓碰枞瓣纯疱藻趟铬喵営喹喺喼喿嗀嗃嗄嗅嗈嗉嗊嗍嗐嗑嗔诟嗕嗖嗙嗛嗜痂癖嗝嗡嗤嗥嗨唢嗬嗯嗰嗲嗵叽嗷嗹嗾嗿嘀嘁嘂嘅惋嘈峪禾荫啀嘌嘏嘐嘒啯啧嘚唛嘞嘟囔嘣嘥嘦嘧嘬嘭这谑严敞馋松哓嘶嗥呒虾嘹嘻啴嘿噀噂噅噇噉噎噏噔噗噘噙噚咝噞噢噤蝉皿噩噫噭嗳噱哙噳嚏涌洒欲巫霏噷噼嚃嚄嚆抖哜尝嚔苏嚚嚜嚞嚟呖嚬嚭嚮嚯亸喾饬按竣苛嚵嘤啭冁呓膪谦囍囒囓囗囘萧酚飘溅谛囝溯眸纥銮鹘囟殉囡団囤囥囧囨囱囫囵囬囮囯囲図囶囷囸囹圄圉拟囻囿圀圂圃圊粹蠹赦圌垦圏滚鲱凿枘圕圛圜圞坯埂壤骸炕祠窑豚绅魠鲮鳖圧握圩圪垯圬圮圯炸岬幔毯祇窨菩溉圳圴圻圾坂坆沾坋坌舛壈昆垫墩椅坒坓坩埚坭坰坱坳坴坵坻坼杨挣涎帘垃垈垌垍垓垔垕垗垚垛垝垣垞垟垤垧垮垵垺垾垿埀畔埄埆埇埈埌殃隍埏埒埕埗埜垭埤埦埧埭埯埰埲埳埴埵埶绋埸培怖桩础辅埼埽堀诃侄庑堃堄摧磐贞韧砌堈堉垩堋堌堍堎垴堙堞堠礁堧堨舆堭堮蜓摘堲堳堽堿塁塄塈煤茔棵塍垲埘塓绸塕鸦沽虱塙冢塝缪塡坞埙塥塩塬塱场螨塼塽塾塿墀墁墈墉墐夯増毁墝墠墦渍钵墫墬堕墰墺墙橱壅壆壊壌壎壒榨蒜壔壕壖圹垆壜壝垅壡壬壭壱売壴壹壻壸寝壿夂夅夆変夊夌漱邑夓腕泄甥御骼夗夘夙衮瑙妊娠醣枭珊莺鹭戗幻魇夤蹀秘擂鸫姚宛闺屿庾挞拇賛蛤裨菠氅漓捞湄蚊霆鲨箐篆篷荆肆舅荔鲆巷惭骰辟邱镕镰阪漂烩鲵鲽鳄鸨胪鹏妒峨谭枰晏玑癸祝秤竺牡籁恢罡蝼蝎赐绒御梭夬夭砣榆怙枕夶夹馅奄崛葩谲奈贺祀赠奌奂奓奕䜣詝奘奜奠奡奣陶奨奁魁奫奬奰娲孩贬隶酥宄狡猾她姹嫣妁毡荼皋膻蝇嫔妄妍嫉媚娆妗趣妚妞妤碍妬娅妯娌妲妳妵妺姁姅姉姗姒姘姙姜姝姞姣姤姧姫姮娥姱姸姺姽婀娀诱慑胁娉婷娑娓娟娣娭娯娵娶娸娼婊婐婕婞婤婥溪孺婧婪婬婹婺婼婽媁媄媊媕媞媟媠媢媬媮妫媲媵媸媺媻媪眯媿嫄嫈袅嫏嫕妪嫘嫚嫜嫠嫡嫦嫩嫪毐嫫嫬嫰妩嫺娴嫽嫿妫嬃嬅嬉耍婵痴艳嬔嬖嬗嫱袅嫒嬢嬷嬦嬬嬭幼嬲嬴婶嬹嬾嬿孀娘孅娈孏曰癫屏孑孓雀孖斟篓谜摺孛矻鸠崮轲祜鸾孥邈毓棠膑孬孭孰孱孳孵泛罔衔孻孪宀㝉冗拙株薇掣抚琪瓿榴谧弥宊濂祁瑕宍宏碁宓邸谳実潢町宥宧宨宬徵崎骏掖阙臊煮禽蚕宸豫寀寁寥寃檐庶寎暄碜寔寖寘寙寛寠苫寤肘洱滥蒗陕核寪弘绰螽宝擅疙瘩晷対檐専尃尅赎绌缭畴衅尌峙醌襟痲碧屁昊槌淘恵瀑牝畑莓缸羚觑蔻脏躁尔尓锐尗尙尜尟尢尥尨尪尬尭尰擒尲尶尴尸尹潽蠖蛾尻扣梢蚴鳍脬蹲屇屌蚵屐屃挪屖屘屙屛屝屡屣峦嶂岩舄屧屦屩屪屃屮戍驻钾崖嵛巅旮旯楂榄榉芋茱萸靛麓屴屹屺屼岀岊岌岍阜岑彭巩岒岝岢岚岣岧岨岫岱岵岷峁峇峋峒峓峞峠嵋峨峰峱岘峹峿崀崁崆祯崋崌崃岖昆崒崔嵬巍萤颢崚崞崟崠峥巆崤崦崧殂岽崱崳崴崶崿嵂嵇嵊泗嵌嵎嵒嵓岁嵙嵞嵡嵩嵫嵯嵴嵼嵾嵝崭崭晴嶋嶌嶒嶓嵚崂嶙嶝嶞峤嶡嶢峄嶨嶭嶮嶰嶲岙嵘巂巃巇巉岿巌巓巘巛滇芎巟巠弋回巣巤炊擘蜥蟒蛊觋巰蜀彦淖杏茂甫楞巻巽帼巿帛斐鲫蕊帑帔帗帚琉汶帟帡帣帨裙帯帰帷帹暆帏幄帮幋幌幏帻幙帮幞幠幡幢幦幨幩幪帱幭幯幰遥蹉跎馀庚鉴幵幷稚邃庀庁広庄庈庉笠庋跋庖牺庠庤庥鲸庬庱庳庴庵馨衢庹庿廃厩廆廋廌廎廏廐廑廒荫廖廛厮搏锣廞弛袤廥廧廨廪廱绵踵髓廸迫瓯邺廻廼廾廿躔弁皱弇弌弍弎弐弑吊诡憾荐弝弢弣弤弨弭弮弰弪霖繇焘斌旭溥骞弶弸弼弾彀彄别累纠强彔彖彘彟彟陌彤贻彧绘虹彪炳雕蔚鸥彰瘅彲彳彴仿彷徉徨彸彽踩敛旆徂徇徊渭畲铉裼従筌徘徙徜徕膳苏萌渐徬徭醺徯徳徴潘徻徼忀瘁胖燎怦悸颤扉犀澎湃砰恍惚绞隘忉惮挨饿忐忑忒忖応忝忞耿忡忪忭忮忱忸怩忻悠懑怏遏怔怗怚怛怞怼黍讶怫怭懦怱怲恍怵惕怸怹恁恂恇恉恌恏恒恓恔恘恚恛恝恞恟恠恣恧眄恪恫恬澹恰恿悀悁悃悄悆悊悐悒晦悚悛悜悝悤您悩悪悮悰悱凄恻德悴怅惘闷悻悾惄愫钟蒐惆惇惌惎惏惓惔惙惛耄惝疟浊恿惦德恽惴蠢惸拈愀愃愆愈愊愍愐愑愒愓愔愕恪氓蠢騃昵惬赧悫愬愮愯恺愼慁恿慅慆慇霭慉慊愠慝慥怄怂慬慱悭慴慵慷戚焚憀灼郁憃惫憋憍眺捏轼愦憔憖憙憧憬憨憪憭怃憯憷憸憹憺懃懅懆邀懊懋怿懔懐懞懠懤懥恹懫懮懰懱毖懵遁梁雍忏懽戁戄戆戉戋戕戛戝戛戠戡戢戣戤戥戦戬戭戯轰戱披菊牖戸戹戺戻卯戽锹扂楔扃扆扈扊杖牵绢铐镯赉扐搂搅烊盹瞌跟趸镲靶鼾払扗玫腮扛扞扠扡扢盔押扤扦扱罾揄绥鞍郤窾扻扼扽抃抆抈抉抌抏瞎抔缳缢擞抜拗択抨摔歉蹿牾抶抻搐泵菸拃拄拊髀抛拌脯拎拏拑擢秧沓曳挛迂拚拝拠拡拫拭拮踢拴拶拷攒拽掇芥橐簪摹疔挈瓢骥捺蹻挌挍挎挐拣挓挖掘浚挙揍聩挲挶挟挿捂捃捄捅捆捉捋胳膊揎捌捍捎躯蛛捗捘捙捜捥捩扪捭据捱捻捼捽掀掂抡臀膘掊掎掏掐笙掔掗掞棉芍掤搪阐掫掮掯揉掱掲掽掾揃揅揆搓揌诨揕揗揘揜揝揞揠揥揩揪揫橥遒麈揰揲揵揶揸背揺搆搉搊搋搌搎搔搕撼橹捣搘搠搡搢搣搤搥搦搧搨搬楦裢讪赸掏搰搲搳搴揾搷搽搾搿摀摁摂摃摎掴摒摓跤摙摛掼摞摠摦喉羯摭摮挚摰摲抠摴抟摷掺摽撂撃撅稻撊撋挦锏泼撕撙撚㧑挢撢掸撦撅撩撬撱朔揿蚍蜉挝捡擀掳闯擉缶觚擐擕擖擗擡擣擤澡腚擧擨擩擫擭摈拧撷擸撸擽擿攃摅撵攉攥攐攓撄搀撺每攩攫辔澄攮攰攲攴轶攷砭讦攽碘敁敃敇敉叙敎筏敔敕敖闰诲敜煌敧敪敳敹敺敻敿斁衽斄牒绉诌斉斎斓鹑谰驳鳢斒筲斛斝斞斠斡斢斨斫斮晾沂潟颖绛邵斲斸釳於琅斾斿旀旗旃旄涡旌旎旐旒旓旖旛旝旟旡旣浴旰獭魃旴时旻旼旽昀昃昄昇昉晰躲澈熹皎皓矾昑昕昜昝昞昡昤晖笋昦昨是昱昳昴昶昺昻晁蹇隧蔬髦晄晅晒晛晜晞晟晡晢晤晥曦晩萘莹顗晿暁暋暌暍暐暔暕煅旸暝暠暡曚暦暨暪朦胧昵暲殄冯暵暸暹暻暾曀晔昙曈曌曏曐暧曘曙曛叠昽曩骆曱甴肱曷牍禺锟曽沧耽朁朅朆杪栓夸竟粘绦朊膺朏朐朓朕朘朙瞄觐溘饔飧朠朢朣栅椆淀虱朩朮朰朱炆璋钰炽鹮朳槿朵朾朿杅杇杌陧欣钊湛漼楷瀍煜玟缨翱肇舜贽适逵杓杕杗杙荀蘅杝杞脩珓筊杰榔狍閦颦缅莞杲杳眇杴杶杸杻杼枋枌枒枓衾葄翘纾逋枙狸桠枟槁枲枳枴枵枷枸橼枹枻柁柂柃柅柈柊柎某柑橘柒柘柙柚柜柞栎柟柢柣柤柩柬柮柰柲橙柶柷柸柺査柿栃栄栒栔栘栝栟柏栩栫栭栱栲栳栴檀栵栻桀骜桁镁桄桉桋桎梏椹葚桓桔桕桜桟桫椤桭杯桯桲桴桷桹湘溟梃梊梍梐潼栀枧梜梠梡梣梧梩梱梲梳梴梵梹棁棃樱棐棑棕榈簑绷蓑枨棘棜棨棩棪棫棬棯棰棱棳棸棹椁棼碗椄苕椈椊椋椌椐椑椓椗検椤椪椰椳椴椵椷椸椽椿楀匾楅篪楋楍楎楗楘楙楛楝楟楠楢楥桢楩楪楫楬楮楯楰梅楸楹楻楽榀榃榊榎槺榕榖榘榛狉莽搒笞榠榡榤榥榦榧杩榭榰榱梿霰榼榾桤槊闩槎槑槔槖様槜槢槥椠槪槭椮槱槲槻槼槾樆樊樏樑樕樗樘樛樟樠樧樨権樲樴樵猢狲桦樻罍樾樿橁橄橆桡笥龠橕橚橛辆椭橤橧竖膈跨橾橿檩檃檇柽檍檎檑檖檗桧槚檠樯檨檫檬梼槟檴檵柠棹櫆櫌栉櫜椟櫡槠栌枥榇栊櫹棂茄櫽欀欂欃欐欑栾欙棂溴欨欬欱欵欶欷歔欸欹欻欼欿歁歃歆艎歈歊莳蝶歓歕歘歙歛歜欤歠蹦诠镶蹒跚升陟歩歮歯歰歳歴璞歺瞑歾殁夭殈殍殑殗殜殙殛殒殢殣殥殪殚僵殰殳荃殷殸殹蛟殻肴谤殴毈毉喂毎毑蕈毗毘毚茛邓毧毬毳毷毹毽毾毵牦氄氆靴氉氊氇氍氐聊氕氖気氘氙氚氛氜氝氡汹焊痉氤氲氥氦铝锌氪烃氩铵痤汪浒漉痘盂碾菖蒲蕹蛭螅氵冰氹氺氽烫氾氿渚汆汊汋汍汎汏汐汔汕褟汙汚汜蓠沼秽蔑汧汨汩汭汲汳汴堤汾沄沅沆瀣沇沈葆浸沦湎溺痼疴沌沍沏沐沔沕沘浜畹砾沚沢沬沭沮沰沱灢沴沷籽沺烹濡洄泂肛泅泆涌肓泐泑泒泓泔泖泙泚泜泝泠漩馍涛粼泞藓鳅泩泫泭泯铢泱泲洇洊泾琵琶荽蓟箔洌洎洏洑潄濯洙洚洟洢洣洧洨洩痢滔洫洮洳洴洵洸洹洺洼洿淌蜚浄浉浙赣渫浠浡浤浥淼瀚浬浭翩萍浯浰蜃淀苔蛞蝓蜇螵蛸煲鲤浃浼浽溦涂涊涐涑涒涔滂莅涘涙涪涫涬涮涴涶涷涿淄淅淆淊凄黯淓淙涟淜淝淟淠淢淤渌淦淩猥藿亵淬淮淯淰淳诣涞纺淸淹炖癯绮渇済渉渋渓渕涣渟渢滓渤澥渧渨渮渰渲渶渼湅湉湋湍湑湓湔黔湜湝浈湟湢湣湩湫湮麟湱湲湴涅満沩溍溎溏溛舐漭溠溤溧驯溮溱溲溳溵溷溻溼溽溾滁滃滉滊荥滏稽滕滘汇滝滫滮羼耷卤滹浐煎漈漊漎绎漕漖漘漙沤漜漪漾漥漦漯漰溆漶漷濞潀颍潎潏潕潗潚潝潞潠潦祉疡潲潵滗潸潺潾涠澁澂澃澉澌澍澐澒澔澙渑澣澦澧澨澫澬浍澰澴澶澼熏郁濆濇濈濉濊貊濔疣濜濠濩觞浚濮盥潍濲泺瀁滢渎渖瀌浏瀒瀔濒泸瀛潇潆瀡潴泷濑瀬弥潋瀳瀵瀹瀺瀼沣滠灉灋灒漓灖灏灞灠滦灥灨滟灪蜴灮烬獴灴灸灺炁炅鱿炗炘炙炤炫疽烙钎炯炰炱炲炴炷毁炻烀烋瘴鲳烓烔焙烜烝烳饪烺焃焄耆焌焐焓焗焜焞焠焢焮焯焱焼煁煃煆煇煊熠煍熬煐炜煕暖熏硷霾煚煝煟煠茕矸煨琐炀萁煳煺煻熀熅熇熉罴荧穹炝熘熛熜稔谙烁熤熨熯熰眶蚂颎熳熸熿燀烨燂燄盏燊燋燏燔隼燖焖燠燡灿燨燮燹燻燽燿爇爊爓爚爝爟爨蟾爯爰为爻丬爿牀牁牂牄牋窗牏牓窗釉牚腩蒡虻牠虽蛎牣牤牮牯牲牳牴牷牸牼绊牿靬犂犄犆犇犉犍犎犒荦犗犛犟犠犨犩犪犮犰狳犴犵犺狁甩狃狆狎狒獾狘狙黠狨狩狫狴狷狺狻豕狈蜘猁猇猈猊猋猓猖獗猗猘狰狞犸猞猟獕猭猱猲猳猷猸猹猺玃獀獃獉獍獏獐獒毙獙獚獜獝獞獠獢獣獧鼇蹊狯猃獬豸狝獯鬻獳犷猕猡玁菟玅玆玈珉糁禛郅玍玎玓瓅玔玕玖玗玘玞玠玡玢玤玥玦珏瑰玭玳瑁玶玷玹玼珂珇珈瑚珌馐馔珔珖珙珛珞珡珣珥珧珩珪佩珶珷珺珽琀琁陨玡琇琖琚琠琤琦琨琫琬琭琮琯琰琱琲琅琴珐珲瑀瑂瑄瑉玮瑑瑔瑗瑢瑭瑱瑲瑳瑽瑾瑿璀璨璁璅璆璈琏璊璐璘璚璝璟璠璡璥瑷璩璪璫璯璲玙璸璺璿瓀璎瓖瓘瓒瓛脐瓞瓠瓤瓧瓩瓮瓰瓱瓴瓸瓻瓼甀甁甃甄甇甋甍甎甏甑甒甓甔瓮甖甗饴蔗甙诧钜粱盎锈团甡褥産甪甬甭甮宁铠甹甽甾甿畀畁畇畈畊畋畎畓畚畛畟鄂畤畦畧荻畯畳畵畷畸畽畾疃叠疋疍疎箪疐疒疕疘疝疢疥疧疳疶疿痁痄痊痌痍痏痐痒痔痗瘢痚痠痡痣痦痩痭痯痱痳痵痻痿瘀痖瘃瘈瘉瘊瘌瘏瘐痪瘕瘖瘙瘚瘛疭瘜瘝瘗瘠瘥瘨瘭瘆瘯瘰疬瘳疠瘵瘸瘺瘘瘼癃痨痫癈癎癐癔癙癜癠疖症癞蟆癪瘿痈発踔绀蔫酵皙砬砒翎翳蔹钨镴皑鹎驹暨粤褶皀皁荚皃镈皈皌皋皒朱皕皖皘皜皝皞皤皦皨皪皫皭糙绽皴皲皻皽盅盋碗盍盚盝踞盦盩秋千盬盭眦睁瞤盯盱眙裰盵盻睐眂眅眈眊県眑眕眚眛眞眢眣眭眳眴眵眹瞓眽郛睃睅睆睊睍睎困睒睖睙睟睠睢睥睪睾睯睽睾眯瞈瞋瞍逛瞏瞕瞖眍䁖瞟瞠瞢瞫瞭瞳瞵瞷瞹瞽阇瞿眬矉矍铄矔矗矙瞩矞矟矠矣矧矬矫矰矱硪碇磙罅舫阡、矼矽礓砃砅砆砉砍砑砕砝砟砠砢砦砧砩砫砮砳艏砵砹砼硇硌硍硎硏硐硒硜硖砗磲茚钡硭硻硾碃碉碏碣碓碔碞碡碪碫碬砀碯碲砜碻礴磈磉磎硙磔磕磖磛磟磠磡磤磥蹭磪磬磴磵磹磻硗礀硚礅礌礐礚礜礞礤礧礮砻礲礵礽礿祂祄祅祆禳祊祍祏祓祔祕祗祘祛祧祫祲祻祼饵脔锢禂禇禋祦禔祎隋禖禘禚禜禝禠祃禢禤禥禨禫祢禴禸秆秈秊闱飒秋秏秕笈蘵赁秠秣秪秫秬秭秷秸稊稌稍稑稗稙稛稞稬秸稲稹稼颡稿穂穄穇穈穉穋稣贮穏穜穟秾穑穣穤穧穨穭穮穵穸窿阒窀窂窅窆窈窕窊窋窌窒窗窔窞窣窬黩蹙窑窳窴窵窭窸窗竁竃竈竑竜并竦竖篦篾笆鲛竾笉笊笎笏笐靥笓笤箓笪笫笭笮笰笱笲笳笵笸笻筀筅筇筈筎筑筘筠筤筥筦笕筒筭箸筰筱筳筴宴筸箂个箊箎箑箒箘箙箛箜篌箝箠箬镞箯箴箾篁筼筜篘篙篚篛篜篝篟篠篡篢篥篧篨篭篰篲筚篴篶篹篼箦簁簃簆簉簋簌簏簜簟簠簥簦簨簬簰簸簻籊藤籒籓籔签籚篯箨籣籥籧笾簖籫籯芾麴籵籸籹籼粁秕粋粑粔粝粛粞粢粧粨粲粳稗粻粽辟粿糅糆糈糌糍糒糔萼糗蛆蹋糢糨糬粽糯糱籴粜糸糺紃蹼鲣霉纡纨绔纫闽襻紑纰纮锭鸢鹞纴紞紟扎紩紬绂绁纻紽紾绐絁絃絅経絍绗絏缡褵絓絖絘絜绚絣螯絪絫聒絰絵绝絺絻絿綀绡綅绠绨绣綌綍綎捆綖綘継続缎绻綦綪线綮綯绾罟蝽綷縩绺绫緁绲緅緆缁绯緌緎総緑绱緖缃缄缂绵缗緤褓缌纂緪緰缑缈缏缇縁縃縄萦缙缒縏缣縕缞縚缜缟缛縠縡縢縦绦縯縰骋缧縳纤缦絷缥縻衙縿繄缫繈繊繋繐缯繖繘繙繠缋繣繨缰缲繸繻缱纁纆纇缬缵纩纑纕缵纙纚纛缾罃罆坛罋罂罎罏罖罘罛罝罠罣罥罦罨罫罭锾罳罶罹罻罽罿羂羃羇芈蕉５１鸵羑羖羌羜羝羢羣羟羧羭羮羰羱羵羶羸藜鲐翀翃翅翊翌翏翕翛翟翡翣翥翦跹翪翫翚翮翯翱翽翾翿板饕鸹锨耋耇耎耏专耒耜耔耞耡耤耨耩耪耧耰鬓耵聍聃聆聎聝聡聦聱聴聂聼阈聿肄肏肐肕腋肙肜肟肧胛肫肬肭肰肴肵肸肼胊胍胏胑胔胗胙胝胠铨胤胦胩胬胭胯胰胲胴胹胻胼胾脇脘脝脞脡脣脤脥脧脰脲脳腆腊腌臜腍腒腓胨腜腠脶腥腧腬腯踝蹬镣腴腶蠕诽膂腽嗉膇膋膔腘膗膙膟黐膣膦膫膰膴膵膷脍臃臄臇臈臌臐臑臓膘臖臙臛臝臞臧蓐诩臽臾臿舀舁鳑鲏舋舎舔舗馆舝舠舡舢舨舭舲舳舴舸舺艁艄艅艉艋艑艕艖艗艘艚艜艟艣舣艨艩舻艬艭荏艴艳艸艹艻艿芃芄芊萰陂藭芏芔芘芚蕙芟芣芤茉芧芨芩芪芮芰鲢芴芷芸荛豢芼芿苄苒苘苙苜蓿苠苡苣荬苤苎苪镑苶苹苺苻苾茀茁范蠡萣茆茇茈茌茍茖茞茠茢茥茦菰茭茯茳藨茷藘茼荁荄荅荇荈菅蜢鸮荍荑荘豆荵荸荠莆莒莔莕莘莙莚莛莜莝莦莨菪莩莪莭莰莿菀菆菉菎菏菐菑菓菔芲菘菝菡菢菣菥蓂菧菫毂蓥菶菷菹醢菺菻菼菾萅萆苌萋萏萐萑萜萩萱萴莴扁萻葇葍葎葑荭葖葙葠葥苇葧葭药葳葴葶葸葹葽蒄蒎莼茏薹莅蒟蒻蒢蒦蒨蒭藁蒯蒱鉾蒴蒹蒺蒽荪蓁蓆蓇蓊蓌蓍蓏蓓蓖蓧蓪蓫荜跣藕苁蓰蓱莼蓷蓺蓼蔀蔂蔃蔆蔇蔉蔊蔋蔌蔎蔕蔘蔙蒌蔟锷蒋雯茑蔯蔳麻蔵蔸蔾荨蒇蕋蕍荞蕐蕑芸莸蕖蕗蕝蕞蕠蕡蒉蕣蕤蕨蕳蓣蕸蕺蕻薀薁薃薅薆荟薉芗薏薐蔷薖薘剃谔钗薜薠薢薤薧薨薫薬薳薶薷薸薽薾薿藄藇藋荩藐藙藚藟藦藳藴苈藷藾蘀蘁蕲苹蘗蘘蘝蘤蘧蘩蘸蘼虀虆虍蟠虒虓虖虡虣虥虩虬虰蛵蛇虷鳟虺虼蚆蚈蚋蚓蚔蚖蚘蚜蚡蚣蚧蚨蚩蚪蚯蚰蜒蚱蚳蚶蚹蚺蚻蚿蛀蛁蛄蛅蝮蛌蛍蛐蟮蛑蛓蛔蛘蛚蛜蛡蛣蜊蛩蛱蜕螫蜅蚬蜈蝣蜋蜍蜎蜑蠊蜛饯蜞蜣蜨蜩蜮蜱蜷蜺蜾蜿蝀蝃蝋蝌蝍蝎蝏蝗蝘蝙蝝鲼蝡蝤蝥猿蝰虻蝲蝴蝻螃蠏蛳螉螋螒螓螗螘螙螚蟥螟螣螥螬螭䗖螾螀蟀蟅蝈蟊蟋蟑蟓蟛蟜蟟蟢虮蟨蟪蟭蛲蟳蛏蟷蟺蟿蠁蠂蠃虿蠋蛴蠓蚝蠗蠙蠚蠛蠜蠧蟏蠩蜂蠮蠰蠲蠵蠸蠼蠽衁衄衄衇衈衉衋衎衒同衖胡衞裳钩衭衲衵衹衺衿袈裟袗袚袟袢袪袮袲袴袷袺袼褙袽裀裉袅裋夹裍裎裒裛裯裱裲裴裾褀褂褉褊裈褎褐褒褓褔褕袆褚褡褢褦褧褪褫袅褯褰褱裆褛褽褾襁褒襆裥襉襋襌襏襚襛襜裣襞襡襢褴襦襫襬襭襮襕襶襼襽襾覂覃覅霸覉覊覌覗觇覚覜觍觎覧覩觊觏覰観觌觔觕觖觜觽觝觡酲觩觫觭觱觳觯觷觼觾觿言赅讣訇訏訑訒诂讬訧訬訳訹证訾詀詅诋毁詈詊讵詑诒诐詗诎察詨诜詶詸詹詻诙诖誂誃诔锄诓誋诳诶悖誙诮诰誧説読誯谇訚谄谆諆諌诤诹诼諕谂谀諝谝諟喧谥諴諵谌谖誊謆謇歌謍謏謑谡谥謡謦謪谪讴謷謼谩哗譅譆譈譊讹譒撰谮鑫譞噪譩谵譬譱譲谴譸譹谫讅讆詟䜩雠讐谗谶讙谠讟谽豁豉豇岂豊豋豌豏豔豞豖豗豜豝豣豦豨豭豱豳豵豶豷豺豻貅貆狸猊貔貘䝙貜貤餍贳餸贶贲赂賏赊赇赒賝赓赕賨赍斗賮賵賸赚赙赜赟贉赆赑贕赝赬赭赱赳迄趁趂趄趐趑趒趔趡趦趫趮趯趱趴趵趷趹趺趿跁跂跅跆踬跄跐跕跖跗跙跛跦跧跩跫跬跮跱跲跴跺跼跽踅踆踈踉踊踒踖踘踜踟躇蹰踠踡踣踤踥踦踧跷踫踮逾踱踊踶踹踺踼踽躞蹁蹂躏蹎蹐蹓蹔跸蹚蹜蹝迹蹠蹡蹢跶蹧蹩蹪蹯鞠蹽躃躄躅踌跻躐踯跞躘躙躗躝躠蹑躜躧躩躭躰躬躶軃軆辊軏轫軘軜軝腭転軥軨軭軱轱辘軷轵轺軽軿輀輂辇辂辁輈挽輗辄辎辋輠輤輬輭輮辏輴輵輶輹輼辗辒轇轏轑轒辚轕轖轗轘轙轝轞轹轳罪辣辞辵辶辺込辿迅迋迍麿迓迣迤逦迥迨迮迸迺迻迿逄逅逌逍逑逓迳逖逡逭逯逴逶逹遄遅侦遘遛遝遢遨遫遯遰遴绕遹遻邂邅邉邋邎邕邗邘邛邠邢邧邨邯郸邰邲邳邴邶邷邽邾邿郃郄郇郈郔郕郗郙郚郜郝郞郏郠郢郪郫郯郰郲郳郴郷郹郾郿鄀鄄郓鄇鄈鄋鄍鄎鄏鄐鄑邹邬鄕郧鄗鄘鄚鄜鄞鄠鄢鄣鄤鄦鄩鄫鄬鄮鄯鄱郐鄷鄹邝鄻鄾鄿酃酅酆酇郦酊酋酎酏酐酣酔酕醄酖酗酞酡酢酤酩酴酹酺醁醅醆醊醍醐醑醓醖醝酝醡醤醨醪醭醯醰酦醲醴醵醸醹醼醽醾釂酾酽釆釈鲈镏阊钆钇钌钯钋鼢鼹钐钏釪釬釭釱钍釸钕钫鈃钭鈆鈇钚鈊鈌钤钣鈒鈤钬钪鈬铌铈钶铛钹铍钸钿鉄鉆铊铇鉌铋鉏铂钷铆钵鉥钲鉨钼钽鉱鉲鉶铰铒鉼铪銍銎铣銕镂铫铦铑铷銤铱铟銧铥铕铯銭銰焊銶锑锉汞鋂锒鋆鋈鋊铤鋍铗鋐鋑鋕鋘鋙锊锓锔锇铓鋭铖锆锂铽鋳鋹鋺鉴镚钎錀锞锖锫锩錍铔锕錔锱铮锛錞锬锜錤錩錬録铼錼锝钔锴鍉镀鍏鍐铡鍚锻锽锸锲锘鍫鍭鍱鍴锶鍹锗针锺锿镅鎉鎋鎌鎍鎏鎒鎓鎗镉鎚鎞镃鎤铩锼鎭鎯镒镍鎴镓鎸鎹镎镟鏊镆镠镝鏖铿锵鏚镗镘镛鏠鏦錾镤鏸镪鏻鏽鏾铙鐄鐇鐏铹镦镡鐗馗镫镢镨鐡锎镄鐩镌鐬鐱镭鐶鐻鐽镱鑀鑅镔鑐鑕鑚鑛鑢鑤镥鑪镧鑯鑱鑴鑵镊镢钃镻闫闬闶闳閒闵閗閟阂関合閤哄阆閲阉閺阎阏阍阌暗闉阕阗闑闒闿闘闚阚闟闠闤闼阞阢阤阨阬阯阹阼阽陁陑陔陛陜陡陥陬骘陴険陼陾阴隃隈隒隗隞隠隣隤隩隮隰颧隳隷隹雂雈雉雊雎雑雒雗雘雚雝雟雩雰雱驿霂霅霈霊沾霒霓霙霝霢霣霤霨霩霪霫霮靁叇叆靑靓靣腼靪靮靰靳靷靸靺靼靿鞀鞃鞄鞍鞗鞙鞚鞝鞞鞡鞣鞨鞫鞬鞮鞶鞹鞾鞑韅鞯驮韍韎韔韖韘韝韫韡韣韭韭韱韹韺頀刮頄顸顼頍颀颃颁頖頞頠頫頬颅頯頲颕頼悴顋顑颙颛颜顕顚顜颟顣颥颞飐飑台飓颸飏飖颽颾颿飀飂飚飌翻飡飣饲飥饨饫飮飧飶餀餂饸饹餇餈饽哺馂餖餗餚馄馃餟餠餤餧餩餪餫糊餮糇餲饧馎糕饩馈馊馌馒饇馑馓膳饎饐饘饟馕馘馥馝馡馣骝骡馵馹駃駄駅駆駉駋驽駓驵駗骀驸駜骂骈駪駬骃駴骎駹駽駾騂騄骓騆騉騋骒骐麟騑騒験騕骛騠騢騣騤騧骧騵驺骟騺蓦骖骠骢驆驈骅驌骁驎骣驒驔驖驙驦驩驫骺鲠骫骭肮骱骴骶骷髅骾髁髂髄髆膀髇髑髌髋髙髝髞髟髡髣髧髪髫髭髯髲髳髹髺髽髾鬁鬃鬅鬈鬋鬎鬏鬐鬑鬒鬖鬗鬘鬙鬠鬣斗鬫鬬阄鬯鬰鬲鬵鬷魆魈魊魋魍魉魑魖鳔魛魟魣魦魨魬鲂魵魸鮀鲅鮆鲧鲇鲍鲋鮓鲒鲕鮟鱇鮠鮦鮨鲔鲑鮶鮸鮿鲧鯄鯆鲩鯈鲻鯕鲭鲞鯙鯠鲲鯥鲰鲶鳀鯸鳊鲗䲠鹣鳇鰋鳄鳆鰕鰛鰜鲥鰤鳏鰦鳎鳐鳁鳓鰶鲦鲡鰼鰽鱀鱄鳙鱆鳕鱎鱐鳝鳝鳜鲟鲎鱠鳣鱨鲚鱮鱲鱵鱻鲅鳦凫鳯鳲鳷鳻鴂鴃鴄鸩鴈鴎鸰鴔鴗鸳鸯鸲鹆鸱鴠鴢鸪鴥鸸鹋鴳鸻鴷鴽鵀鵁鸺鹁鵖鵙鹈鹕鹅鵟鵩鹌鵫鵵鵷鵻鹍鶂鶊鶏鶒鹙鶗鶡鶤鶦鶬鶱鹟鶵鶸鶹鹡鶿鹚鷁鷃鷄鷇䴘䴘鷊鷏鹧鷕鹥鸷鷞鷟鸶鹪鹩鷩鷫鷭鹇鹇鸴鷾䴙鸂鸇䴙鸏鸑鸒鸓鸬鹳鸜鹂鹸咸鹾麀麂麃麄麇麋麌麐麑麒麚麛麝麤麸面麫麮麯麰麺麾黁黈黉黢黒黓黕黙黝黟黥黦黧黮黰黱黪黶黹黻黼黾鼋鼂鼃鼅鼈鼍鼏鼐鼒冬鼖鼙鼚鼛鼡鼩鼱鼪鼫鼯鼷鼽齁齆齇齈齉齌赍齑龀齕齗龅齚龇齞龃龉龆齢出齧齩齮齯齰齱齵齾厐龑龒龚龖龘龝龡龢龤'

traditional_characters = '制咖片型超聲盤鑒定仔點他命書歌粉巾字帳恤手指記憶棒形轉彎溝光○〇㐄㐅㐆㐌㐖毒㐜㐡㐤㐰㐺㑇㑳㒳㒸㔾㗂㗎㝵㞎㞙㞞㠯㢲㢴㤅㥁㥯㨗㫺㬎㮎㮚㮸㲋㲱㲾㳮㵎㵪㶸㷖㷭㹢㹴犬㺢狓㺵㼝㽮㿝䍃䔢䖟䖸䗈䗥䗪䝓䠶䥯䦉䯝䰾魚䲔䳗䳘䵹鼄䶑一對應映射丁不識下兒子做二休世丘之貉並中台原則串為甚謂乾淨了百事無成八變五十些人得道雞升天代如併來去個國政策勁幽靈在歐洲遊蕩接樣蘿蔔坑側化傳價元論醇共再准刀兩斷切分耕耘收穫錢貨物向看舊就緒險刻千金動勞永逸匙零夜半卡通回復返影蹤反常態口咬氣句話同吐快吹周味呼諾嗚品紅鍋哄而散起唱和問三知生熟團漆黑火糟堆場空塊麵塌糊塗塵染壁廂夔已足多情露水大早到晚夫妻當關萬莫開失古恨套所料既往孔見提師要家主審寸陰難買鬥牛小撮部陣局展身層巴掌帆風順席地帶過年計於春頭載四季期被蛇怕井繩度願式份彈頃深前律徑心意念差愁孤行俱全房廳交遮打技長把抓死拿眼淚鼻涕鑰鎖折段抿拍即合掃排掬揮撥擁上入擊洞擲攬改故轍敗文值名斑方面旁族日秋餐隔雅里終父旦時晌會霎間晃暴寒曝更月望垠際朝夕本正經利杯羹東西板枝獨秀根筋桿進條龍服務概模次函數又性程總付步腳印趨登毛拔呵氧氮碳決雌雄波未平派謊言流清楚白準溜煙潭有獲聞是處降琴鶴甲病發可拾沙目然瞭直以相眨穿睹瞥瞬矢的解石鳥神教秉虔誠秘種窩蜂窮竅笑置筆苟勾銷抹殺煞等獎箍節吃箭仇雙鵰詩籌籮筐系列紙級士官統絲毫掛維網盡線微吭響股腦胎脈承腔臂力致效資源址器舉功投般說講規貿易葉障著慎滿皆輸號木電池衣傾鐘高低視仁覺醒覽遺角銀幣觸潰九鼎蔽抄出駟馬追重語破貧洗貫走路安蹴至幾蹶振躍役膽汗較輩輪辭贊退六連遍遞邊針血錘音錯門思閃真倒項栽霧類保護川先驚乍體鬨鱗爪鳴滴泡鄰域黨專鼓作齊炒丑烯亥克內酯冬加奴卯肝炎基尺梁街褲鎬客寵庭巳汝昌烷玲磊糖肇酉醛啷青縣韙良香骨鯛丂七集河市弦喜嘴張舌堵區工業姊妹星架構巧彩扭歪拼湊餘熱曜武州爺浮屠美鄉老階樹葷素碎落能魄鰓鰻珠丄丅丆万俟丈尚摸母娘量管群亞虎必我堂令申件裝伏位博俠義界表女墟臺戲臭皮匠勝諸葛亮賽頂倍催請運算包立叉戟離疫苗土史志演圍揭瓦曬夷姑婆帝村寶爛尖杉鹼屜桌山岔島由紀峽壩庫鎮廢從德後拗湯治旬食明昧曹朋友框欄極權冪曲歸依貓民氟硼氯磷鐵江侗自旅法司洋浦梅園溫暖灣焦班幸用田略番疊皇炮捶硝苯酸腺苷稜草鏡穗跳遠索錦綱聚氰胺聯店胚膲愛色堇紫羅蘭芝茶飯菱雲蟲藏藩亂叛蘇親債凳學座恐戀柱測肌腹衩錐係貂企烏跪叩軍車農題迭都甘油屯奏鍵短阿姨陪姐隻顧茅廬槽駕魂鮮鹿頁其菜單乘任供勢午齒漢組織吊調瀉唇坡城報墳外夸將尉建築岸崗公床揚新劍昇杭林栗校樓標款汽社浣海商館劇院鋼華港機械廣媒環球融第醫科證券綜財樂育游漲猶嶺疏癮瞼確兵領導繳肢膛船艾瑟爾蒼蔡虞傚衫覆訪訴課諭議軌述野鉤限敵鞋頜頷顎饒首齦站例修凡劃垂屆屬崽頦廚拜挫擺放旋削棋榻檻禮沉注滑營獄畫确儀聘花葬詔員跌轄週達酒錨閘陷陸雨雪飛威丌于丹久乏予理評產亢卑亦乎舞己悲矩圓詞害誌但住佞佳便俗信票案幅翁倦倫假偏倚斜虧鬼敲停備傷脾胃僅此像儉匱免宜穴焉戴兼容許凍伯仲負彼晝皂軒輊實刊划顛衛戰哥比省非好黃飾別拘束掩奶睬選擇搖擾煩苦枚寫協厭及格受歡迎約只估侵犯割狀告或缺抗拒挽撤救藥喻磨滅端倪少逆逾越避靠適吉譽吝玉含延咎歹聽啻淵善謀均勻堪忍夠太惹妙妥妨孕症孝術室完納推冠積宣疑辯慄碴稱屈撓屑干涉衡待很忙惡忿怎麼怠急恥恭息悅惑惜惟想愉愧怍慌憤啟懂懈懷材才緊招認扣抵拉捨也罷插揣冒搭撞南牆擴核支攻敢雷攀敬裡嗎需景智暇曾罪遇朽枉止況競爭辱求癒渝溶濟左右袒困補爽特寂寞示弱找謝畏強疾徐痛癢冤符眠睦瞅董何厚云措活疲羞者輕玻璃祥兆禁移稂莠穩佛換答簡結果盟絕縷途給談否羈翼耐肖脛毋寧興舒若菲萊痕跡窠臼虛衰臉兔撒鷹棺範該詳諱抬泰讓鬚眉象眾貲賬費灰賴奇慮訓輟辨菽麥辛近送透逞徒速續逮捕遂遑違遜斧鉞艱醉鏽隨觀棄顯飽脂肪使丏丐幫丒且慢末丕替桃宗王尊涼爵各圖屋脊糧署錄壇吾祿職胄襲君廈丗北壑桐疹損逢陵鷸丙寅戌氨腈唑綸辰酮脫氫酶醚丞丟現掉紗帽弄扯砲碗丠両丣坐存激肩臻蒂蓮悖序驅丨丩丫挺杈髻鬟細介俄伊犁京尼布訂普渡央委監察檢查劑圈設警隊斯督剩震境航舶革防托播促質版蠑螈鋒研藝歷殘消頻譜精密製造陲郵候埔堅壓壢凹匯執府究邦俘攝寮彬狼嶽肺腫庸英訊診埋粒胞括控碼韓暑槍樞砥澳哇牟壽甸鑽探篇簽綴縫繼耳肯照婦埃懸璧軸櫃檯辣擱淺邪跑纖阮陽私囊魔丮丰姿采丱燒丳丵丶丷丸參寨朗桂瑞砂衷霞貌鳳僕艦因嫌宰峰幹絡牌持旨祭禱簿編罰賓辦丼丿乀乂乃乄仰慕盛曠留考驗闊乆乇么醜麼乊湖燃乑乒乓乕乖僻忤戾离謬迕乗危肥劫除隙浪婿乙炔腸酰吡咯鹽乚乛乜嘢卿玄宮尾狐龜塔嶷兄弟泉章霄釘耙乞扎哀憐恕討乢乣乤乥乧乨乩童乪乫乭乳暈汁液瑤漿牙癌突竇罩腐膠豬酪蛋糕菌瘤乴乵乶乷乸乹乺乼乾俸冰嘉噦嚎坤媽屍壘旱枯涸俐渴潮澀煸豆燥爹瘦癟癬瞪袋脆薑貝隆餾乿亀亁叫咕攘扔搞男砸竄蓬麻亃亄亅卻亇遲典今臨繁累卵奉婚聰躬巨與遷添裂副宿歲怪噁尕崙愣杆硅硫鈦鈾錳芑雜異鈉砷胂磺琥珀艙棍簧胡茬盜浩盆販郎腿亍洪亐互欠助勉惠操斥諉繫戶譯亓墓碑刑鈴卅渠繽紛斗米旗憲釩燈徽瘟祖拳福穀豐臟腑綁肉醃苓蘊橋鋪霸顏鬧判噴岡底蛙陘礦亖亙亜罕們娜桑那努哈喀弗烈曼松森杜氏盃奧琛敦戊穆聖裔彙薛孫亟亡佚虜羊牢奮釋卷卸契媾感額睫纏誼趾塞擠紐阻還配馳莊亨洛祚亪享津滬畿郊慈菴枇杷膏亭閣鋥麗亳亶亹誅初責翻瘋偶傑叢稠妖拖寰居吸授慧蝸吞壯魅狗矛盾益渣患憂稀描猿夢暫涯畜禍緣沸搜引擎臣橫紜誰混援蒸獸獅稅剖亻亼亽亾什獻剎邡麽仂仃仄仆富怨仈仉畢昔晨殼紹仍仏仒仕宦仗欺恃腰嘆歎炬梓訖施仙后瓊逝仚仝仞仟悔仡佬償填泊拓撲簇羔購頓欽佩髮棻閫馭養億儆尤藉幀賑凌敘帖李柔剛沃眥睚戒訛取饗讀仨仫仮著泳臥躺韶夏裁仳仵唯賢憑釣誕仿似宋彿諷伀碩盼鵝伄儅伈伉儷柯始娃邁戈坦堡帕茨薩廟瑪莉莎藤霍姆伋伍奢胥廷芳豪伎倆侍汛勒希羲雛伐憩整謨閑閒伕伙伴頤伜伝伢叔恆茲恩翰伱伲侶伶俜悧鼬伸懶縮喇叭伹伺伻伽倻輻伾佀佃佇佈喬妮墨佉盧佌貸劣廉昂檔濃矮傘窪緩耗胸谷迷擋率齲宅沫舍療佐貳佑佔優據鏵嘗呢須魯曉佗佘余坪寺瓜銃僧蒙芒陀龕哼嘔坊姦孽弊揖祟繭縛誓賊佝僂瞀佟你奪趕佡佢佣佤佧賈佪佫佯佰佱潔績釀餚佴捲佶佷佸佹佺佻佼佽佾具喚窘壞娛怒慨硬習慣聾膨脹蔓駭貴痺侀侁侂侃侄侅鴻燕侇侈糜靡侉侌妾侏儒倉鼠侐侑侔侖侘侚鏈侜偎傍鈷循柳葫蘆附価侮罵蔑侯岩截蝕侷貼壺嬛宴捷攜桶箋酌俁狹膝狄俅俉俊俏俎俑俓俔諺俚俛黎健呈固墒增守康箱濕祐鏢鑣槓盒靖膜齡俞豹獵噪孚封札筒託衍鴿剪撰稿煉廠禊練繕葺俯瞰撐衝俲俳俴俵俶俷俺俻俾倀倂倅儲卒惶敷猝逃頡蓄崇隱倌倏忽刺蠟燭噍嚼坍扁抽斃蔥楣灌灶糞背藪賣賠閉霉騰倓倔倖倘倜儻倝借箸挹澆閱倡狂倢倣値倥傯倨傲倩匡嗣沖柝珍倬倭寇猩倮倶倷倹勤讚偁偃充偽吏嗓寐惺扮拱芫茜藉虢鈔偈偉晶偌宕距析濾殿疼癱註頗偓偕鴨歇滯偝偟偢忘怡旺偨偩偪偫偭偯偰偱偲偵緝蹄偷減惰漏窺竊偸偺迹傀儡傅傈僳傌籬傎奎琳迪叟芭傒傔傕傖悉荒傜傞傢傣芽逼傭婢傮睨寄檄誦謠頌傴擔辜弓慘蒿悼疤傺傻屄臆巢洩篋羨蓋軋頹傿儸僄僇僉僊働僎僑僔僖僚僝僞僣僤僥僦猴僨僩僬僭僮僯僰僱僵殖籤靜僾僿征隴儁儂儃儇儈朴薄儊儋儌儍儐儓儔儕儗儘儜儞儤儦儩汰哉寡渥裕酷儭儱罐儳儵儹儺儼儽兀臬臲鷲允勛勳宙宵帥憝彞諧嫂鬩暢沛溢盈飢赫兇悍狠猛頑愚妣斬秦遣鞭耀敏榮槃澤爆碟磁禿纜輝霽鹵朵婁孜烽醬勃汀箕裘鉗耶懞蕾徹兌軟遭黜兎児韻媳爸兕觥兗兙兛兜售鍪肚兝兞兟兡兢兣樽殮涅睡稟籍贅泌啡肽奸幕涵澇熵疚眷稃襯訌赴煥椒殲植跏沒試誤猜棲窗肋袖頰兪卦撇鬍岐廓轎疸楓茴瓏廁秩募勺噸寓斤曆畝迫筷釐最淫螺韜兮寬匪篩襄贏軛複兲詐刃堰戎痞蟻餉它冀鑄冂冃円冇冉冊嫁厲礪竭醮冏牧冑冓冔冕冖冗冘冞冢窄抑誣冥冫烘菇蟄冷凝坨橇淇淋炭餅磚磧窖醋雕雹霜冱冶爐艷嘲峻灘淡漠煖颼飲冼冽凃凄愴梗凅凇凈凊凋敝濛凔凜遵汞脢凞几凢処凰凱凵凶焰凸摺刷紋預喪嘍奔巡榜殯芙蓉租籠輯鞘萃凼鋸鑊刁蠻刂娩崩批拆攤掰櫱驟歧顆秒袂贓勿囑忌磋琢膚刈羽刎訟戮舂槳艇刓刖霹靂刜創犢刡恙墅幟筵緻刦刧刨昏默攸尿慾薰潤薰圭刪刮痧鏟刱刲刳刴刵踏磅戳柏槐繡芹莧蝟舟銘鵠鶩刼剁剃辮剄剉履鉛剋剌姻咽哨廊掠桅沿召瞻翅趙卜渺茫郭剒剔剕瀝剚愎毅訥纔剜剝啄採剞剟剡剣剤綵剮腎駛黏剰袍剴紊剷剸剺剽剿劁劂劄劈啪柴扳啦劉奭姥夼昫涓熙禪禹錫翔雁鶚劊劌弩柄蜻蛉劒劓劖劘劙瀾簣賞磯釜晉甜薪逐劦熔紂虐赤囚劬劭労劵効劻劼劾峭艮勅勇勵勍勐臘脖龐漫飼盪粥輒勖勗勘驕餒碌泮雇捐竹騎殊阱勣樸懇謹勦勧勩勯勰勱勲勷勸懲慰誡諫勹芡踐闌匁庇拯粟紮袱裹餃匆遽匈匉匊匋匍匐莖匏匕妝痰膿蛹齋苑烤蹈塘羌熊閥螳螂疆碚竿緯荷茵邙魏匚匜匝匟扶稷匣匭攏匸匹耦匽匾匿卂叮瘡禧軫堤棚迢鈞鍊卄卆遐卉瓷盲瓶噹胱腱裸卋卌卍卐怯污賤鄙齷齪陋卓溪唐梯漁陳棗泥漳潯澗梨芬譙贍轅迦鄭単驢弈洽鰲卛占筮卝卞卟吩啉屎翠厄卣卨卪卬卮榫襖璽綬鈕蚤懼殆篤聳卲帘帙繞卹卼卽厂厎厓厔厖厗奚厘厙厜厝諒厠厤厥厪膩孢厮厰厳厴厹厺粕垢蕪菁厼厾叁悟茸薯叄吵笄悌哺譏坫壟弧芯杠潛嬰芻袁詰貪諜煽饋駁収岳締災賄騙叚叡吻攔蘑蜜訣燧玩硯箏椎藺銅逗驪另覓叨嘮謁杵姓喊嚷囂咚嚀塑尋惱憎擦祇泣滲蝠叱吒咄咤喝籀黛舵舷叵叶鐸懿昭穰苴遼叻叼吁塹嫖賭瞧爬衆抒吅吆夥巹橡滌抱縱摩郡唁墜扇籃膀襪頸吋愾諮酬哭妓媛暗錶韁邇妃羿絮蕃渾拐葵暮隅吔吖啶嗪戚吜嗇噬嚥吟哦詠吠吧唧嗒咐吪雋咀徵燐苞茹鈣哧吮吰吱嘎吲哚吳棟嬌窟孟簫忠晗淞闔閭趼宇吶睛噓拂捧疵熄竽笛糠吼吽呀呂韋矇呃呆笨呇貢呉罄呋喃呎呏呔呠呡癡呣呤呦呧瑛眩扒晬淑姬瑜璇鵑呪呫嗶嚅囁呬呯呰呱呲咧噌鈍呴呶呷呸呺呻哱咻嘯嚕籲坎坷邏呿咁咂咆哮咇咈咋蟹煦珅藹咍咑咒詛咔噠嚓咾噥哩喱咗咠咡咢咣咥咦咨嗟詢咩咪咫嚙齧咭咮咱咲咳嗆嗽咴咷咸咹咺咼喉咿婉慟憫賦矜綠茗藍哂搶瞞哆嗦囉噻啾濱彗哋哌哎唷喲哏哐哞哢哤哪裏哫啼喘哰哲萎蚌哳哶哽哿唄唅唆唈唉唎唏嘩堯棣殤璜睿肅唔睇唕唚唞唣喳唪唬唰喏唲唳唵嘛唶唸唹唻唼唾唿啁啃鸚鵡啅埠棧榷祺舖鞅飆啊啍啎啐啓啕啖啗啜啞祈啢啣啤啥啫啱啲啵啺饑啽噶崑沁喁喂喆裙喈嚨喋喌喎喑喒喓喔粗喙幛慶滋鵲喟喣喤喥喦喧騷喨喩梆喫葡萄喭駝挑嚇碰樅瓣純皰藻趟鉻喵営喹喺喼喿嗀嗃嗄嗅嗈嗉嗊嗍嗐嗑嗔詬嗕嗖嗙嗛嗜痂癖嗝嗡嗤嗥嗨嗩嗬嗯嗰嗲嗵嘰嗷嗹嗾嗿嘀嘁嘂嘅惋嘈峪禾蔭嘊嘌嘏嘐嘒嘓嘖嘚嘜嘞嘟囔嘣嘥嘦嘧嘬嘭這謔嚴敞饞鬆嘵嘶嘷嘸蝦嘹嘻嘽嘿噀噂噅噇噉噎噏噔噗噘噙噚噝噞噢噤蟬皿噩噫噭噯噱噲噳嚏涌灑欲巫霏噷噼嚃嚄嚆抖嚌嚐嚔囌嚚嚜嚞嚟嚦嚬嚭嚮嚯嚲嚳飭按竣苛嚵嚶囀囅囈膪謙囍囒囓囗囘蕭酚飄濺諦囝溯眸紇鑾鶻囟殉囡団囤囥囧囨囪囫圇囬囮囯囲図囶囷囸囹圄圉擬囻囿圀圂圃圊粹蠹赦圌墾圏滾鯡鑿枘圕圛圜圞坯埂壤骸炕祠窯豚紳魠鯪鱉圧握圩圪垯圬圮圯炸岬幔毯祇窨菩溉圳圴圻圾坂坆沾坋坌舛壈昆墊墩椅坒坓坩堝坭坰坱坳坴坵坻坼楊掙涎簾垃垈垌垍垓垔垕垗垚垛垝垣垞垟垤垧垮垵垺垾垿埀畔埄埆埇埈埌殃隍埏埒埕埗埜埡埤埦埧埭埯埰埲埳埴埵埶紼埸培怖樁礎輔埼埽堀訶姪廡堃堄摧磐貞韌砌堈堉堊堋堌堍堎堖堙堞堠礁堧堨輿堭堮蜓摘堲堳堽堿塁塄塈煤塋棵塍塏塒塓綢塕鴉沽虱塙塚塝繆塡塢塤塥塩塬塱塲蟎塼塽塾塿墀墁墈墉墐夯増毀墝墠墦漬缽墫墬墮墰墺墻櫥壅壆壊壌壎壒榨蒜壔壕壖壙壚壜壝壠壡壬壭壱売壴壹壻壼寢壿夂夅夆変夊夌漱邑夓腕泄甥禦骼夗夘夙袞瑙妊娠醣梟珊鶯鷺戧幻魘夤蹀祕擂鶇姚宛閨嶼庾撻拇賛蛤裨菠氅漓撈湄蚊霆鯊箐篆篷荊肆舅荔鮃巷慚骰辟邱鎔鐮阪漂燴鯢鰈鱷鴇臚鵬妒峨譚枰晏璣癸祝秤竺牡籟恢罡螻蠍賜絨御梭夬夭砣榆怙枕夶夾餡奄崛葩譎奈賀祀贈奌奐奓奕訢詝奘奜奠奡奣陶奨奩魁奫奬奰媧孩貶隸酥宄狡猾她奼嫣妁氈荼皋膻蠅嬪妄妍嫉媚嬈妗趣妚妞妤礙妬婭妯娌妲妳妵妺姁姅姉姍姒姘姙姜姝姞姣姤姧姫姮娥姱姸姺姽婀娀誘懾脅娉婷娑娓娟娣娭娯娵娶娸娼婊婐婕婞婤婥谿孺婧婪婬婹婺婼婽媁媄媊媕媞媟媠媢媬媮媯媲媵媸媺媻媼眯媿嫄嫈嫋嫏嫕嫗嫘嫚嫜嫠嫡嫦嫩嫪毐嫫嫬嫰嫵嫺嫻嫽嫿嬀嬃嬅嬉耍嬋痴豔嬔嬖嬗嬙嬝嬡嬢嬤嬦嬬嬭幼嬲嬴嬸嬹嬾嬿孀孃孅孌孏曰癲屏孑孓雀孖斟簍謎摺孛矻鳩崮軻祜鸞孥邈毓棠臏孬孭孰孱孳孵泛罔銜孻孿宀宁宂拙株薇掣撫琪瓿榴謐彌宊濂祁瑕宍宏碁宓邸讞実潢町宥宧宨宬徵崎駿掖闕臊煮禽蠶宸豫寀寁寥寃簷庶寎暄磣寔寖寘寙寛寠苫寤肘洱濫蒗陝覈寪弘綽螽寳擅疙瘩晷対檐専尃尅贖絀繚疇釁尌峙醌襟痲碧屁昊槌淘恵瀑牝畑莓缸羚覷蔻髒躁尒尓銳尗尙尜尟尢尥尨尪尬尭尰擒尲尶尷尸尹潽蠖蛾尻釦梢蚴鰭脬蹲屇屌蚵屐屓挪屖屘屙屛屝屢屣巒嶂巖舄屧屨屩屪屭屮戍駐鉀崖嵛巔旮旯楂欖櫸芋茱萸靛麓屴屹屺屼岀岊岌岍阜岑彭鞏岒岝岢嵐岣岧岨岫岱岵岷峁峇峋峒峓峞峠嵋峩峯峱峴峹峿崀崁崆禎崋崌崍嶇崐崒崔嵬巍螢顥崚崞崟崠崢巆崤崦崧殂崬崱崳崴崶崿嵂嵇嵊泗嵌嵎嵒嵓嵗嵙嵞嵡嵩嵫嵯嵴嵼嵾嶁嶃嶄晴嶋嶌嶒嶓嶔嶗嶙嶝嶞嶠嶡嶢嶧嶨嶭嶮嶰嶲嶴嶸巂巃巇巉巋巌巓巘巛滇芎巟巠弋迴巣巤炊擘蜥蟒蠱覡巰蜀彥淖杏茂甫楞巻巽幗巿帛斐鯽蕊帑帔帗帚琉汶帟帡帣帨帬帯帰帷帹暆幃幄幇幋幌幏幘幙幚幞幠幡幢幦幨幩幪幬幭幯幰遙蹉跎餘庚鑑幵幷稚邃庀庁広庄庈庉笠庋跋庖犧庠庤庥鯨庬庱庳庴庵馨衢庹庿廃廄廆廋廌廎廏廐廑廒廕廖廛廝搏鑼廞弛袤廥廧廨廩廱綿踵髓廸廹甌鄴廻廼廾廿躔弁皺弇弌弍弎弐弒弔詭憾薦弝弢弣弤弨弭弮弰弳霖繇燾斌旭溥騫弶弸弼弾彀彄彆纍糾彊彔彖彘彟彠陌彤貽彧繪虹彪炳彫蔚鷗彰癉彲彳彴彷彷徉徨彸彽踩斂旆徂徇徊渭畬鉉裼従筌徘徙徜徠膳甦萌漸徬徭醺徯徳徴潘徻徼忀瘁胖燎怦悸顫扉犀澎湃砰恍惚絞隘忉憚挨餓忐忑忒忖応忝忞耿忡忪忭忮忱忸怩忻悠懣怏遏怔怗怚怛怞懟黍訝怫怭懦怱怲怳怵惕怸怹恁恂恇恉恌恏恒恓恔恘恚恛恝恞恟恠恣恧眄恪恫恬澹恰恿悀悁悃悄悆悊悐悒晦悚悛悜悝悤您悩悪悮悰悱悽惻悳悴悵惘悶悻悾惄愫鍾蒐惆惇惌惎惏惓惔惙惛耄惝瘧濁惥惦惪惲惴惷惸拈愀愃愆愈愊愍愐愑愒愓愔愕愙氓蠢騃昵愜赧愨愬愮愯愷愼慁慂慅慆慇靄慉慊慍慝慥慪慫慬慱慳慴慵慷慼焚憀灼鬱憃憊憋憍眺捏軾憒憔憖憙憧憬憨憪憭憮憯憷憸憹憺懃懅懆邀懊懋懌懍懐懞懠懤懥懨懫懮懰懱毖懵遁樑雍懺懽戁戄戇戉戔戕戛戝戞戠戡戢戣戤戥戦戩戭戯轟戱披菊牖戸戹戺戻戼戽鍬扂楔扃扆扈扊杖牽絹銬鐲賚扐摟攪烊盹瞌跟躉鑔靶鼾払扗玫腮扛扞扠扡扢盔押扤扦扱罾揄綏鞍郤窾扻扼扽抃抆抈抉抌抏瞎抔繯縊擻抜抝択抨摔歉躥牾抶抻搐泵菸拃拄拊髀拋拌脯拎拏拑擢秧沓曳攣迂拚拝拠拡拫拭拮踢拴拶拷攢拽掇芥橐簪摹疔挈瓢驥捺蹻挌挍挎挐揀挓挖掘浚挙揍聵挲挶挾挿捂捃捄捅捆捉捋胳膊揎捌捍捎軀蛛捗捘捙捜捥捩捫捭据捱捻捼捽掀掂掄臀膘掊掎掏掐笙掔掗掞棉芍掤搪闡掫掮掯揉掱掲掽掾揃揅揆搓揌諢揕揗揘揜揝揞揠揥揩揪揫櫫遒麈揰揲揵揶揸揹揺搆搉搊搋搌搎搔搕撼櫓搗搘搠搡搢搣搤搥搦搧搨搬楦褳訕赸搯搰搲搳搴搵搷搽搾搿摀摁摂摃摎摑摒摓跤摙摛摜摞摠摦睺羯摭摮摯摰摲摳摴摶摷摻摽撂撃撅稻撊撋撏鐧潑撕撙撚撝撟撢撣撦撧撩撬撱朔撳蚍蜉撾撿擀擄闖擉缶觚擐擕擖擗擡擣擤澡腚擧擨擩擫擭擯擰擷擸擼擽擿攃攄攆攉攥攐攓攖攙攛每攩攫轡澄攮攰攲攴軼攷砭訐攽碘敁敃敇敉敍敎筏敔敕敖閏誨敜煌敧敪敱敹敺敻敿斁衽斄牒縐謅斉斎斕鶉讕駮鱧斒筲斛斝斞斠斡斢斨斫斮晾沂潟穎絳邵斲斸釳於琅斾斿旀旂旃旄渦旌旎旐旒旓旖旛旝旟旡旣浴旰獺魃旴旹旻旼旽昀昃昄昇昉晰躲澈熹皎皓礬昑昕昜昝昞昡昤暉筍昦昨昰昱昳昴昶昺昻晁蹇隧蔬髦晄晅晒晛晜晞晟晡晢晤晥曦晩萘瑩顗晿暁暋暌暍暐暔暕煅暘暝暠暡曚暦暨暪朦朧暱暲殄馮暵暸暹暻暾曀曄曇曈曌曏曐曖曘曙曛曡曨曩駱曱甴肱曷牘禺錕曽滄耽朁朅朆杪栓誇竟粘絛朊膺朏朐朓朕朘朙瞄覲溘饔飧朠朢朣柵椆澱蝨朩朮朰朱炆璋鈺熾鹮朳槿朶朾朿杅杇杌隉欣釗湛漼楷瀍煜玟纓翱肈舜贄适逵杓杕杗杙荀蘅杝杞脩珓筊杰榔狍閦顰緬莞杲杳眇杴杶杸杻杼枋枌枒枓衾葄翹紓逋枙狸椏枟槁枲枳枴枵枷枸櫞枹枻柁柂柃柅柈柊柎某柑橘柒柘柙柚柜柞櫟柟柢柣柤柩柬柮柰柲橙柶柷柸柺査柿栃栄栒栔栘栝栟栢栩栫栭栱栲栳栴檀栵栻桀驁桁鎂桄桉桋桎梏椹葚桓桔桕桜桟桫欏桭桮桯桲桴桷桹湘溟梃梊梍梐潼梔梘梜梠梡梣梧梩梱梲梳梴梵梹棁棃櫻棐棑棕櫚簑繃蓑棖棘棜棨棩棪棫棬棯棰棱棳棸棹槨棼椀椄苕椈椊椋椌椐椑椓椗検椤椪椰椳椴椵椷椸椽椿楀楄楅篪楋楍楎楗楘楙楛楝楟楠楢楥楨楩楪楫楬楮楯楰楳楸楹楻楽榀榃榊榎槺榕榖榘榛狉莽榜笞榠榡榤榥榦榧榪榭榰榱槤霰榼榾榿槊閂槎槑槔槖様槜槢槥槧槪槭槮槱槲槻槼槾樆樊樏樑樕樗樘樛樟樠樧樨権樲樴樵猢猻樺樻罍樾樿橁橄橆橈笥龠橕橚橛輛橢橤橧豎膈跨橾橿檁檃檇檉檍檎檑檖檗檜檟檠檣檨檫檬檮檳檴檵檸櫂櫆櫌櫛櫜櫝櫡櫧櫨櫪櫬櫳櫹櫺茄櫽欀欂欃欐欑欒欙欞溴欨欬欱欵欶欷歔欸欹欻欼欿歁歃歆艎歈歊蒔蝶歓歕歘歙歛歜歟歠蹦詮鑲蹣跚陞陟歩歮歯歰歳歴璞歺瞑歾歿殀殈殍殑殗殜殙殛殞殢殣殥殪殫殭殰殳荃殷殸殹蛟殻殽謗毆毈毉餵毎毑蕈毗毘毚茛鄧毧毬毳毷毹毽毾毿氂氄氆靴氉氊氌氍氐聊氕氖気氘氙氚氛氜氝氡洶焊痙氤氳氥氦鋁鋅氪烴氬銨痤汪滸漉痘盂碾菖蒲蕹蛭螅氵氷氹氺氽燙氾氿渚汆汊汋汍汎汏汐汔汕褟汙汚汜蘺沼穢衊汧汨汩汭汲汳汴隄汾沄沅沆瀣沇沈葆浸淪湎溺痼痾沌沍沏沐沔沕沘浜畹礫沚沢沬沭沮沰沱灢沴沷籽沺烹濡洄泂肛泅泆湧肓泐泑泒泓泔泖泙泚泜泝泠漩饃濤粼濘蘚鰍泩泫泭泯銖泱泲洇洊涇琵琶荽薊箔洌洎洏洑潄濯洙洚洟洢洣洧洨洩痢滔洫洮洳洴洵洸洹洺洼洿淌蜚浄浉浙贛渫浠浡浤浥淼瀚浬浭翩萍浯浰蜃淀苔蛞蝓蜇螵蛸煲鯉浹浼浽溦涂涊涐涑涒涔滂涖涘涙涪涫涬涮涴涶涷涿淄淅淆淊淒黯淓淙漣淜淝淟淠淢淤淥淦淩猥藿褻淬淮淯淰淳詣淶紡淸淹燉癯綺渇済渉渋渓渕渙渟渢滓渤澥渧渨渮渰渲渶渼湅湉湋湍湑湓湔黔湜湝湞湟湢湣湩湫湮麟湱湲湴湼満溈溍溎溏溛舐漭溠溤溧馴溮溱溲溳溵溷溻溼溽溾滁滃滉滊滎滏稽滕滘滙滝滫滮羼耷滷滹滻煎漈漊漎繹漕漖漘漙漚漜漪漾漥漦漯漰漵漶漷濞潀潁潎潏潕潗潚潝潞潠潦祉瘍潲潵潷潸潺潾潿澁澂澃澉澌澍澐澒澔澙澠澣澦澧澨澫澬澮澰澴澶澼熏郁濆濇濈濉濊貊濔疣濜濠濩觴濬濮盥濰濲濼瀁瀅瀆瀋瀌瀏瀒瀔瀕瀘瀛瀟瀠瀡瀦瀧瀨瀬瀰瀲瀳瀵瀹瀺瀼灃灄灉灋灒灕灖灝灞灠灤灥灨灩灪蜴灮燼獴灴灸灺炁炅魷炗炘炙炤炫疽烙釺炯炰炱炲炴炷燬炻烀烋瘴鯧烓烔焙烜烝烳飪烺焃焄耆焌焐焓焗焜焞焠焢焮焯焱焼煁煃煆煇煊熠煍熬煐煒煕煗燻礆霾煚煝煟煠煢矸煨瑣煬萁煳煺煻熀熅熇熉羆熒穹熗熘熛熜稔諳爍熤熨熯熰眶螞熲熳熸熿燀燁燂燄盞燊燋燏燔隼燖燜燠燡燦燨燮燹燻燽燿爇爊爓爚爝爟爨蟾爯爰爲爻爿爿牀牁牂牄牋牎牏牓牕釉牚腩蒡虻牠雖蠣牣牤牮牯牲牳牴牷牸牼絆牿靬犂犄犆犇犉犍犎犒犖犗犛犟犠犨犩犪犮犰狳犴犵犺狁甩狃狆狎狒獾狘狙黠狨狩狫狴狷狺狻豕狽蜘猁猇猈猊猋猓猖獗猗猘猙獰獁猞猟獕猭猱猲猳猷猸猹猺玃獀獃獉獍獏獐獒獘獙獚獜獝獞獠獢獣獧鼇蹊獪獫獬豸獮獯鬻獳獷獼玀玁菟玅玆玈珉糝禛郅玍玎玓瓅玔玕玖玗玘玞玠玡玢玤玥玦玨瑰玭玳瑁玶玷玹玼珂珇珈瑚珌饈饌珔珖珙珛珞珡珣珥珧珩珪珮珶珷珺珽琀琁隕琊琇琖琚琠琤琦琨琫琬琭琮琯琰琱琲瑯琹琺琿瑀瑂瑄瑉瑋瑑瑔瑗瑢瑭瑱瑲瑳瑽瑾瑿璀璨璁璅璆璈璉璊璐璘璚璝璟璠璡璥璦璩璪璫璯璲璵璸璺璿瓀瓔瓖瓘瓚瓛臍瓞瓠瓤瓧瓩瓮瓰瓱瓴瓸瓻瓼甀甁甃甄甇甋甍甎甏甑甒甓甔甕甖甗飴蔗甙詫鉅粱盎銹糰甡褥産甪甬甭甮甯鎧甹甽甾甿畀畁畇畈畊畋畎畓畚畛畟鄂畤畦畧荻畯畳畵畷畸畽畾疃疉疋疍疎簞疐疒疕疘疝疢疥疧疳疶疿痁痄痊痌痍痏痐痒痔痗瘢痚痠痡痣痦痩痭痯痱痳痵痻痿瘀瘂瘃瘈瘉瘊瘌瘏瘐瘓瘕瘖瘙瘚瘛瘲瘜瘝瘞瘠瘥瘨瘭瘮瘯瘰癧瘳癘瘵瘸瘺瘻瘼癃癆癇癈癎癐癔癙癜癠癤癥癩蟆癪癭癰発踔紺蔫酵皙砬砒翎翳蘞鎢鑞皚鵯駒鱀粵褶皀皁莢皃鎛皈皌皐皒硃皕皖皘皜皝皞皤皦皨皪皫皭糙綻皴皸皻皽盅盋盌盍盚盝踞盦盩鞦韆盬盭眦睜瞤盯盱眙裰盵盻睞眂眅眈眊県眑眕眚眛眞眢眣眭眳眴眵眹瞓眽郛睃睅睆睊睍睎睏睒睖睙睟睠睢睥睪睪睯睽睾瞇瞈瞋瞍逛瞏瞕瞖瞘瞜瞟瞠瞢瞫瞭瞳瞵瞷瞹瞽闍瞿矓矉矍鑠矔矗矙矚矞矟矠矣矧矬矯矰矱硪碇磙罅舫阡、矼矽礓砃砅砆砉砍砑砕砝砟砠砢砦砧砩砫砮砳艏砵砹砼硇硌硍硎硏硐硒硜硤硨磲茚鋇硭硻硾碃碉碏碣碓碔碞碡碪碫碬碭碯碲碸碻礡磈磉磎磑磔磕磖磛磟磠磡磤磥蹭磪磬磴磵磹磻磽礀礄礅礌礐礚礜礞礤礧礮礱礲礵礽礿祂祄祅祆禳祊祍祏祓祔祕祗祘祛祧祫祲祻祼餌臠錮禂禇禋禑禔禕隋禖禘禚禜禝禠禡禢禤禥禨禫禰禴禸稈秈秊闈颯秌秏秕笈蘵賃秠秣秪秫秬秭秷秸稊稌稍稑稗稙稛稞稬稭稲稹稼顙稾穂穄穇穈穉穋穌貯穏穜穟穠穡穣穤穧穨穭穮穵穸窿闃窀窂窅窆窈窕窊窋窌窒窓窔窞窣窬黷蹙窰窳窴窵窶窸窻竁竃竈竑竜竝竦竪篦篾笆鮫竾笉笊笎笏笐靨笓笤籙笪笫笭笮笰笱笲笳笵笸笻筀筅筇筈筎筑筘筠筤筥筦筧筩筭筯筰筱筳筴讌筸箂箇箊箎箑箒箘箙箛箜篌箝箠箬鏃箯箴箾篁篔簹篘篙篚篛篜篝篟篠篡篢篥篧篨篭篰篲篳篴篶篹篼簀簁簃簆簉簋簌簏簜簟簠簥簦簨簬簰簸簻籊籐籒籓籔籖籚籛籜籣籥籧籩籪籫籯芾麴籵籸籹籼粁粃粋粑粔糲粛粞粢粧粨粲粳粺粻粽闢粿糅糆糈糌糍糒糔萼糗蛆蹋糢糨糬糭糯糱糴糶糸糺紃蹼鰹黴紆紈絝紉閩襻紑紕紘錠鳶鷂紝紞紟紥紩紬紱紲紵紽紾紿絁絃絅経絍絎絏縭褵絓絖絘絜絢絣螯絪絫聒絰絵絶絺絻絿綀綃綅綆綈綉綌綍綎綑綖綘継続緞綣綦綪綫綮綯綰罟蝽綷縩綹綾緁緄緅緆緇緋緌緎総緑緔緖緗緘緙緜緡緤緥緦纂緪緰緱緲緶緹縁縃縄縈縉縋縏縑縕縗縚縝縞縟縠縡縢縦縧縯縰騁縲縳縴縵縶縹縻衙縿繄繅繈繊繋繐繒繖繘繙繠繢繣繨繮繰繸繻繾纁纆纇纈纉纊纑纕纘纙纚纛缾罃罆罈罋罌罎罏罖罘罛罝罠罣罥罦罨罫罭鍰罳罶罹罻罽罿羂羃羇羋蕉５１鴕羑羖羗羜羝羢羣羥羧羭羮羰羱羵羶羸藜鮐翀翃翄翊翌翏翕翛翟翡翣翥翦躚翪翫翬翮翯翺翽翾翿闆饕鴰鍁耋耇耎耏耑耒耜耔耞耡耤耨耩耪耬耰鬢耵聹聃聆聎聝聡聦聱聴聶聼閾聿肄肏肐肕腋肙肜肟肧胛肫肬肭肰肴肵肸肼胊胍胏胑胔胗胙胝胠銓胤胦胩胬胭胯胰胲胴胹胻胼胾脇脘脝脞脡脣脤脥脧脰脲脳腆腊腌臢腍腒腓腖腜腠腡腥腧腬腯踝蹬鐐腴腶蠕誹膂膃膆膇膋膔膕膗膙膟黐膣膦膫膰膴膵膷膾臃臄臇臈臌臐臑臓臕臖臙臛臝臞臧蓐詡臽臾臿舀舁鰟鮍舋舎舔舗舘舝舠舡舢舨舭舲舳舴舸舺艁艄艅艉艋艑艕艖艗艘艚艜艟艣艤艨艩艫艬艭荏艴艶艸艹艻艿芃芄芊萰陂藭芏芔芘芚蕙芟芣芤茉芧芨芩芪芮芰鰱芴芷芸蕘豢芼芿苄苒苘苙苜蓿苠苡苣蕒苤苧苪鎊苶苹苺苻苾茀茁范蠡萣茆茇茈茌茍茖茞茠茢茥茦菰茭茯茳藨茷藘茼荁荄荅荇荈菅蜢鴞荍荑荘荳荵荸薺莆莒莔莕莘莙莚莛莜莝莦莨菪莩莪莭莰莿菀菆菉菎菏菐菑菓菔菕菘菝菡菢菣菥蓂菧菫轂鎣菶菷菹醢菺菻菼菾萅萆萇萋萏萐萑萜萩萱萴萵萹萻葇葍葎葑葒葖葙葠葥葦葧葭葯葳葴葶葸葹葽蒄蒎蒓蘢薹蒞蒟蒻蒢蒦蒨蒭藁蒯蒱鉾蒴蒹蒺蒽蓀蓁蓆蓇蓊蓌蓍蓏蓓蓖蓧蓪蓫蓽跣藕蓯蓰蓱蓴蓷蓺蓼蔀蔂蔃蔆蔇蔉蔊蔋蔌蔎蔕蔘蔙蔞蔟鍔蔣雯蔦蔯蔳蔴蔵蔸蔾蕁蕆蕋蕍蕎蕐蕑蕓蕕蕖蕗蕝蕞蕠蕡蕢蕣蕤蕨蕳蕷蕸蕺蕻薀薁薃薅薆薈薉薌薏薐薔薖薘薙諤釵薜薠薢薤薧薨薫薬薳薶薷薸薽薾薿藄藇藋藎藐藙藚藟藦藳藴藶藷藾蘀蘁蘄蘋蘗蘘蘝蘤蘧蘩蘸蘼虀虆虍蟠虒虓虖虡虣虥虩虯虰蛵虵虷鱒虺虼蚆蚈蚋蚓蚔蚖蚘蚜蚡蚣蚧蚨蚩蚪蚯蚰蜒蚱蚳蚶蚹蚺蚻蚿蛀蛁蛄蛅蝮蛌蛍蛐蟮蛑蛓蛔蛘蛚蛜蛡蛣蜊蛩蛺蛻螫蜅蜆蜈蝣蜋蜍蜎蜑蠊蜛餞蜞蜣蜨蜩蜮蜱蜷蜺蜾蜿蝀蝃蝋蝌蝍蝎蝏蝗蝘蝙蝝鱝蝡蝤蝥蝯蝰蝱蝲蝴蝻螃蠏螄螉螋螒螓螗螘螙螚蟥螟螣螥螬螭螮螾螿蟀蟅蟈蟊蟋蟑蟓蟛蟜蟟蟢蟣蟨蟪蟭蟯蟳蟶蟷蟺蟿蠁蠂蠃蠆蠋蠐蠓蠔蠗蠙蠚蠛蠜蠧蠨蠩蠭蠮蠰蠲蠵蠸蠼蠽衁衂衄衇衈衉衋衎衒衕衖衚衞裳鈎衭衲衵衹衺衿袈裟袗袚袟袢袪袮袲袴袷袺袼褙袽裀裉裊裋裌裍裎裒裛裯裱裲裴裾褀褂褉褊褌褎褐褒褓褔褕褘褚褡褢褦褧褪褫褭褯褰褱襠褸褽褾襁襃襆襇襉襋襌襏襚襛襜襝襞襡襢襤襦襫襬襭襮襴襶襼襽襾覂覃覅覇覉覊覌覗覘覚覜覥覦覧覩覬覯覰観覿觔觕觖觜觽觝觡酲觩觫觭觱觳觶觷觼觾觿言賅訃訇訏訑訒詁託訧訬訳訹証訾詀詅詆譭詈詊詎詑詒詖詗詘詧詨詵詶詸詹詻詼詿誂誃誄鋤誆誋誑誒誖誙誚誥誧説読誯誶誾諂諄諆諌諍諏諑諕諗諛諝諞諟諠諡諴諵諶諼謄謆謇謌謍謏謑謖謚謡謦謪謫謳謷謼謾譁譅譆譈譊譌譒譔譖鑫譞譟譩譫譬譱譲譴譸譹譾讅讆讋讌讎讐讒讖讙讜讟谽豁豉豇豈豊豋豌豏豔豞豖豗豜豝豣豦豨豭豱豳豵豶豷豺豻貅貆貍貎貔貘貙貜貤饜貰餸貺賁賂賏賒賕賙賝賡賧賨賫鬭賮賵賸賺賻賾贇贉贐贔贕贗赬赭赱赳迄趁趂趄趐趑趒趔趡趦趫趮趯趲趴趵趷趹趺趿跁跂跅跆躓蹌跐跕跖跗跙跛跦跧跩跫跬跮跱跲跴跺跼跽踅踆踈踉踊踒踖踘踜踟躇躕踠踡踣踤踥踦踧蹺踫踮踰踱踴踶踹踺踼踽躞蹁蹂躪蹎蹐蹓蹔蹕蹚蹜蹝蹟蹠蹡蹢躂蹧蹩蹪蹯鞠蹽躃躄躅躊躋躐躑躒躘躙躛躝躠躡躦躧躩躭躰躳躶軃軆輥軏軔軘軜軝齶転軥軨軭軱軲轆軷軹軺軽軿輀輂輦輅輇輈輓輗輙輜輞輠輤輬輭輮輳輴輵輶輹輼輾轀轇轏轑轒轔轕轖轗轘轙轝轞轢轤辠辢辤辵辶辺込辿迅迋迍麿迓迣迤邐迥迨迮迸迺迻迿逄逅逌逍逑逓逕逖逡逭逯逴逶逹遄遅遉遘遛遝遢遨遫遯遰遴遶遹遻邂邅邉邋邎邕邗邘邛邠邢邧邨邯鄲邰邲邳邴邶邷邽邾邿郃郄郇郈郔郕郗郙郚郜郝郞郟郠郢郪郫郯郰郲郳郴郷郹郾郿鄀鄄鄆鄇鄈鄋鄍鄎鄏鄐鄑鄒鄔鄕鄖鄗鄘鄚鄜鄞鄠鄢鄣鄤鄦鄩鄫鄬鄮鄯鄱鄶鄷鄹鄺鄻鄾鄿酃酅酆酇酈酊酋酎酏酐酣酔酕醄酖酗酞酡酢酤酩酴酹酺醁醅醆醊醍醐醑醓醖醝醞醡醤醨醪醭醯醰醱醲醴醵醸醹醼醽醾釂釃釅釆釈鱸鎦閶釓釔釕鈀釙鼢鼴釤釧釪釬釭釱釷釸釹鈁鈃鈄鈆鈇鈈鈊鈌鈐鈑鈒鈤鈥鈧鈬鈮鈰鈳鐺鈸鈹鈽鈿鉄鉆鉈鉋鉌鉍鉏鉑鉕鉚鉢鉥鉦鉨鉬鉭鉱鉲鉶鉸鉺鉼鉿銍銎銑銕鏤銚銛銠銣銤銥銦銧銩銪銫銭銰銲銶銻銼銾鋂鋃鋆鋈鋊鋌鋍鋏鋐鋑鋕鋘鋙鋝鋟鋦鋨鋩鋭鋮鋯鋰鋱鋳鋹鋺鋻鏰鐱錀錁錆錇錈錍錏錒錔錙錚錛錞錟錡錤錩錬録錸錼鍀鍆鍇鍉鍍鍏鍐鍘鍚鍛鍠鍤鍥鍩鍫鍭鍱鍴鍶鍹鍺鍼鍾鎄鎇鎉鎋鎌鎍鎏鎒鎓鎗鎘鎚鎞鎡鎤鎩鎪鎭鎯鎰鎳鎴鎵鎸鎹鎿鏇鏊鏌鏐鏑鏖鏗鏘鏚鏜鏝鏞鏠鏦鏨鏷鏸鏹鏻鏽鏾鐃鐄鐇鐏鐒鐓鐔鐗馗鐙鐝鐠鐡鐦鐨鐩鐫鐬鐱鐳鐶鐻鐽鐿鑀鑅鑌鑐鑕鑚鑛鑢鑤鑥鑪鑭鑯鑱鑴鑵鑷钁钃镻閆閈閌閎閒閔閗閟閡関閤閤閧閬閲閹閺閻閼閽閿闇闉闋闐闑闒闓闘闚闞闟闠闤闥阞阢阤阨阬阯阹阼阽陁陑陔陛陜陡陥陬騭陴険陼陾隂隃隈隒隗隞隠隣隤隩隮隰顴隳隷隹雂雈雉雊雎雑雒雗雘雚雝雟雩雰雱驛霂霅霈霊霑霒霓霙霝霢霣霤霨霩霪霫霮靁靆靉靑靚靣靦靪靮靰靳靷靸靺靼靿鞀鞃鞄鞌鞗鞙鞚鞝鞞鞡鞣鞨鞫鞬鞮鞶鞹鞾韃韅韉馱韍韎韔韖韘韝韞韡韣韭韮韱韹韺頀颳頄頇頊頍頎頏頒頖頞頠頫頬顱頯頲頴頼顇顋顑顒顓顔顕顚顜顢顣顬顳颭颮颱颶颸颺颻颽颾颿飀飂飈飌飜飡飣飤飥飩飫飮飱飶餀餂餄餎餇餈餑餔餕餖餗餚餛餜餟餠餤餧餩餪餫餬餮餱餲餳餺餻餼餽餿饁饅饇饉饊饍饎饐饘饟饢馘馥馝馡馣騮騾馵馹駃駄駅駆駉駋駑駓駔駗駘駙駜駡駢駪駬駰駴駸駹駽駾騂騄騅騆騉騋騍騏驎騑騒験騕騖騠騢騣騤騧驤騵騶騸騺驀驂驃驄驆驈驊驌驍驎驏驒驔驖驙驦驩驫骺鯁骫骭骯骱骴骶骷髏骾髁髂髄髆髈髐髑髕髖髙髝髞髟髡髣髧髪髫髭髯髲髳髹髺髽髾鬁鬃鬅鬈鬋鬎鬏鬐鬑鬒鬖鬗鬘鬙鬠鬣鬪鬫鬬鬮鬯鬰鬲鬵鬷魆魈魊魋魍魎魑魖鰾魛魟魣魦魨魬魴魵魸鮀鮁鮆鮌鮎鮑鮒鮓鮚鮞鮟鱇鮠鮦鮨鮪鮭鮶鮸鮿鯀鯄鯆鯇鯈鯔鯕鯖鯗鯙鯠鯤鯥鯫鯰鯷鯸鯿鰂鰆鶼鰉鰋鰐鰒鰕鰛鰜鰣鰤鰥鰦鰨鰩鰮鰳鰶鰷鱺鰼鰽鱀鱄鱅鱆鱈鱎鱐鱓鱔鱖鱘鱟鱠鱣鱨鱭鱮鱲鱵鱻鲅鳦鳧鳯鳲鳷鳻鴂鴃鴄鴆鴈鴎鴒鴔鴗鴛鴦鴝鵒鴟鴠鴢鴣鴥鴯鶓鴳鴴鴷鴽鵀鵁鵂鵓鵖鵙鵜鶘鵞鵟鵩鵪鵫鵵鵷鵻鵾鶂鶊鶏鶒鶖鶗鶡鶤鶦鶬鶱鶲鶵鶸鶹鶺鶿鷀鷁鷃鷄鷇鷈鷉鷊鷏鷓鷕鷖鷙鷞鷟鷥鷦鷯鷩鷫鷭鷳鷴鷽鷾鷿鸂鸇鸊鸏鸑鸒鸓鸕鸛鸜鸝鹸鹹鹺麀麂麃麄麇麋麌麐麑麒麚麛麝麤麩麪麫麮麯麰麺麾黁黈黌黢黒黓黕黙黝黟黥黦黧黮黰黱黲黶黹黻黼黽黿鼂鼃鼅鼈鼉鼏鼐鼒鼕鼖鼙鼚鼛鼡鼩鼱鼪鼫鼯鼷鼽齁齆齇齈齉齌齎齏齔齕齗齙齚齜齞齟齬齠齢齣齧齩齮齯齰齱齵齾龎龑龒龔龖龘龝龡龢龤'

assert len(simplified_charcters) == len(simplified_charcters)

s2t_dict = {}
t2s_dict = {}
for i, item in enumerate(simplified_charcters):
    s2t_dict[item] = traditional_characters[i]
    t2s_dict[traditional_characters[i]] = item


def tranditional_to_simplified(text: str) -> str:
    return "".join(
        [t2s_dict[item] if item in t2s_dict else item for item in text])


def simplified_to_traditional(text: str) -> str:
    return "".join(
        [s2t_dict[item] if item in s2t_dict else item for item in text])


if __name__ == "__main__":
    text = "一般是指存取一個應用程式啟動時始終顯示在網站或網頁瀏覽器中的一個或多個初始網頁等畫面存在的站點"
    print(text)
    text_simple = tranditional_to_simplified(text)
    print(text_simple)
    text_traditional = simplified_to_traditional(text_simple)
    print(text_traditional)
