# QA_with_reporters_from_the_Ministry_of_Foreign_Affair_mnbvc
MNBVC General Cleaning Script for the Q&amp;A Dataset of Foreign Ministry Journalists

# 通用外交部数据清洗脚本集合

 1.使用前 请安装环境 -> pip install -r requirements.txt
 
 2.clear_docx_data.py ->清洗 .docx数据 脚本 （老版本已废弃）
 
 3.clear_shtml_data.py -> 清洗 .shtml 网页 数据脚本（老版本已废弃）
 
 4. 与老版本不同 python 答记者问.py -> 清洗答记者问QA网页数据  正则清洗  网页数据 （最新版本格式对齐）
 5. 与老版本不同 python 新闻发布会.py -> 清洗答新闻发布会QA网页数据  正则清洗  网页数据 （最新版本格式对齐）

 
 # huggingface 地址
 
 https://huggingface.co/datasets/Iron-man/MNBVC-QA-with-reporters-from-the-Ministry-of-Foreign-Affairs
 

# 数据格式
shtml数据清洗
老版本: 353个文件,清洗2260条 条外交部记者问数据
新版本: 1700个文件,清洗12877条 条外交部记者问数据


## 清洗前
"<P style="FONT-FAMILY: arial; FONT-SIZE: 14px"　　答：当前东亚区域合作总体势头良好，为地区国家抗击疫情和经济复苏提供了积极助力。同时，全球疫情反弹波动，地区热点问题此起彼伏，东亚合作面临更多复杂因素。 /P>"

"<P style="FONT-FAMILY: arial; FONT-SIZE: 14px"　　中方始终视东盟为维护地区和平稳定、促进区域一体化的重要力量，支持东盟共同体建设，支持东盟在东亚合作中的中心地位，支持东盟在国际地区事务中发挥更大作用。中方愿以中国—东盟建立对话关系30周年为契机，推动地区国家继续聚焦合作、共谋发展、共迎挑战，共同维护地区和平稳定与发展繁荣。 /P>"

## 清洗后
{ "input":"", "instruction":"能否介绍李克强总理访问柬埔寨有关安排？你如何看待当前中柬关系？", "output":"中柬是友好邻邦和铁杆朋友。近年来，中柬关系持续高位运行，中柬命运共同体建设取得丰硕成果，给两国人民带来了切实利益。当前，疫情延宕反复，世界经济复苏乏力，不稳定性和不确定性增加。中国将坚持维护世界和平、促进共同发展的外交政策宗旨，致力于推动构建人类命运共同体，坚持亲诚惠容和与邻为善、以邻为伴的周边外交方针，继续深化同柬埔寨等周边国家的友好互信和利益融合。此访期间，李克强总理将会见西哈莫尼国王，同洪森首相举行会谈。我们期待以此访为契机，同柬方加强治国理政经验交流，深化在农业、制造业、绿色经济、人文交流等领域合作，携手走好具有各自特色的现代化道路，共同丰富发展中国家走向现代化的路径，更好地惠及两国人民。", "date":"2022-11-4", "title":"2022年11月4日外交部发言人赵立坚主持例行记者会_中华人民共和国外交部" }

中英对照数据格式
5份文件 , 一共38条问答数据

## 清洗前
问：据报道，中国军舰已抵也门撤侨，请证实并介绍有关情况。

Q: According to media reports, Chinese naval vessels have arrived in Yemen to evacuate Chinese nationals there. Please confirm this and tell us more details.

答：3月26日以来，也门安全形势严重恶化。中国政府高度重视在也门中国公民和机构的安危，立即组织中国公民有序撤离。根据统一部署，中国在亚丁湾、索马里海域执行护航任务的海军舰艇编队赶赴也门，执行撤离中方在也人员任务。在外交部、国防部等部门和中国驻也门、吉布提使馆以及驻亚丁总领馆紧急协调下，目前122名中国公民已从也门安全撤至吉布提，中国驻吉布提使馆正积极协助他们尽快返回祖国。

## 清洗后
{ "en":{ "input":"", "instruction":" Today is the deadline for countries to apply for the prospective founding membership of the Asian Infrastructure Investment Bank (AIIB). How many prospective founding members does the AIIB have up to now? What is China’s comment on countries’ joining in the AIIB? ", "output":[ "Up till March 31, 30 countries have passed the multilateral review procedures and become prospective founding members of the AIIB. Opinions are being solicited through multilateral procedures on other countries that have filed applications over recent days. We will have the exact number of prospective founding members by April 15.", "The AIIB initiative is a constructive action taken by China to assume more international obligations and complement the current international economic order. It is a useful supplement to the existing multilateral development banks and a move that will benefit all Asian countries and the whole world. The AIIB is an open and inclusive multilateral development institution. We welcome the participation of all interested countries. The Chinese side is ready to work in concert with all parties to make the AIIB a professional and efficient vehicle for infrastructure investment and financing that brings benefit to all parties." ], "date":"2015-3-31", "title":"Foreign Ministry Spokesperson Hua Chunying’s Regular Press Conference on March 31, 2015 " }, "zh":{ "input":"", "instruction":"今天是亚投行意向创始成员国申请的截止日期，目前共有多少意向创始成员国？中方对近期多国纷纷申请加入亚投行有何评论？ ", "output":[ "截至3月31日，已经通过多边审核程序成为亚投行意向创始成员国的国家有30个。连日来，又有不少国家提出申请加入，这些提交申请的国家正在通过多边程序征求意见。具体意向创始成员国数量待4月15日才能确定。", "倡议筹建亚投行是中国承担更多国际责任、补充现有国际经济秩序的建设性举动，是对现有多边开发银行的有益补充，对全球和亚洲各国来说都是互利共赢的。亚投行是一个开放、包容的多边开发机构，欢迎所有有兴趣的国家加入。中方愿与各方一道共同努力，将亚投行打造成一个实现各方互利共赢和专业、高效的基础设施投融资平台。" ], "date":"2015-3-31", "title":"外交部发言人华春莹例行记者会" } }
 
---
license: mit
---
