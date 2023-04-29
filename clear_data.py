import os
from bs4 import BeautifulSoup
import jsonlines


def clear(folder_path, file_json, names, jizhes):
    file_list = []  # 存储文件名和内容的列表
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".shtml"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as f:
                file_content = f.read()
                title=''
                if "title" in file_content:
                    soup = BeautifulSoup(file_content, 'html.parser')
                    title = soup.title.text
                    if '日' in title or '年' in title or '月' in title:
                        date =title.split('日')[0].replace('年', '-').replace('月', '-')
                    else:
                        date=''
                    # file_content = BeautifulSoup(file_content,
                    #                              'html.parser').get_text()
                    # file_list.append([file_name,title, file_content])
                    file_content = file_content.replace("记者</strong><strong style=\"text-indent: 0em;\">：", "记者：")
                    file_content = file_content.replace("记者</strong><strong>：", "记者：")
                    try:
                        if "问：" in file_content and "答：" in file_content:
                            for qa in file_content.split('问：')[1:]:
                                file_json = {'input': '',
                                             'instruction': BeautifulSoup(qa.split("答：")[0],
                                                                          'html.parser').get_text().replace('\u3000',
                                                                                                            ' ').strip().replace(
                                                 "发言人", "").replace("中方", "你"),
                                             'output': BeautifulSoup(qa.split("答：")[1].split("</div>")[0],
                                                                     'html.parser').get_text().replace('\u3000',
                                                                                                       ' ').strip().replace(
                                                 "中方", "我方"),'date':date ,
                                                     'title': title}
                            file_list.append(file_json)
                        elif "记者：" in file_content and (
                                "汪文斌：" in file_content or "赵立坚：" in file_content or "毛宁：" in file_content or "华春莹：" in file_content or "耿爽：" in file_content):
                            for qa in file_content.split('记者：')[1:]:
                                for jizhe in jizhes:
                                    if qa.endswith(jizhe):
                                        qa = qa[:-len(jizhe)]
                                for name in names:
                                    if name in qa:
                                        inst = BeautifulSoup(qa.split(name)[0],
                                                             'html.parser').get_text().replace('\u3000', ' ').strip()
                                        output = BeautifulSoup(qa.split(name)[1].split("</div>")[0],
                                                               'html.parser').get_text().replace('\u3000', ' ').strip()

                                        # if title.split('日')[0].replace('年','-').replace('月','-') is None or title is None:
                                        #     print('error')
                                        # print(len(title),title)
                                        file_json = {'input': '',
                                                     'instruction': inst.replace("发言人", "").replace("中方", "你"),
                                                     'output': output.replace("中方", "我方"),
                                                     'date': date,
                                                     'title': title}
                                        file_list.append(file_json)
                                        if '记者：' in output:
                                            print(file_json)
                                            print(file_content)
                    except:
                        # print(file_content)
                        break
    return file_list


def clear_api(output_path):
    folder_path = "/www/baidu/外交部/外交部问答/20180224-20230416外交部表态/raw/"  # 目标文件夹路径

    file_json = {'input': '',
                 'instruction': '',
                 'output': ''}

    names = ["汪文斌：", "赵立坚：", "毛宁：", "华春莹：", "耿爽："]
    jizhes = ["荷兰广播电视协会", "拉通社", "今日俄罗斯", "日报《读卖新闻》", "哈萨克斯坦24KZ", "美国有线电视新闻网", "德国电视一台", "美国国家公共电台", "总台话语环球节目中心",
              "总台央广",
              "韩国广播公司", "印度报业托拉斯", "英国广播公司", "《澳门月刊》", "《纽约时报》", "日报富士电视台", "日报广播协会", "总台中文国际频道", "中阿卫视", "《印度教徒报》",
              "北京青年报", "美国全国广播公司", "韩联社", "东方卫视", "俄新社", "总台中国之声", "英国天空新闻频道", "总台CGTN", "湖北广播电视台", "《北京日报》", "《环球时报》",
              "凤凰卫视", "印度广播公司", "总台国广", "澎湃新闻", "深圳卫视", "日本共同社", "彭博社", "法新社", "《北京青年报》", "塔斯社", "澳亚卫视", "香港中评社", "路透社",
              "总台央视", "美联社", "新华社", "巴通社", "《中国日报》", "《人民日报》", "日报广播协会", "湖北广电", "中新社", "《华尔街日报》", "日本广播协会", "日本富士电视台",
              "《日本经济新闻》", "巴西《环球报》", "总台华语环球节目中心", "安莎社", "共同社", "半岛电视台", "日本朝日电视台", "西班牙《阿贝赛报》", "美国全国公共广播电台",
              "《新鹿特丹商业报》",
              "英国独立电视新闻", "日本《东京新闻》", "日本东京广播公司", "英国天空电视台", "英国天空新闻", "土耳其阿纳多卢通讯社", "土耳其广播电视总台", "东京电视台", "日本读卖新闻",
              "总台华语环球中心", "古巴拉美社", "朝日电视台", "澳门月刊", "东京新闻", "韩国文化广播公司", "日本《读卖新闻》", "土耳其安纳多卢通讯社", "韩国联合有线新闻台", "CNBC"]

    jizhes = sorted(jizhes, key=len, reverse=True)
    file_list=clear(folder_path,file_json,names,jizhes)

    print(len(file_list))
    with jsonlines.open(output_path, mode='w') as file:
        for i in file_list:
            file.write(i)
if __name__ == '__main__':
    output_path="./data.json"
    clear_api(output_path)