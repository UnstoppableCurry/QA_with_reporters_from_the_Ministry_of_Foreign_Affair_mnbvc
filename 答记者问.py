import jsonlines


def clear_wen(text):
    import jieba

    # 定义一个包含"问"字符的字符串
    # text = "我想问一下，这个问题该怎么解决呢？"

    # 使用jieba分词器对字符串进行分词
    words = jieba.lcut(text)

    # 遍历分词结果，找到包含"问"字符的分词
    for i, word in enumerate(words):
        if "问" == word:
            return 1
        else:
            return 0

def get_year(all_text):
    from  t import get_years
    import re


    match = re.search(r"\d{4}年\d{1,2}月\d{1,2}日", all_text)
    if match is None:
        years = None
    else:
        years = get_years(match.group())
        print(years, '-----')
    return years
def main():
    import re

    import os
    from bs4 import BeautifulSoup

    # 指定路径
    path = "test/"  # 目标文件夹路径

    all_result = []
    nums = 0
    numnum = 0
    numnumnumnum = 0
    # 循环遍历指定路径下的所有文件
    for filename in os.listdir(path):
        print('进度为->', nums * 100 / 1700, '%')
        nums += 1
        if filename.endswith('.html'):
            # 打开HTML文件并读取其中的内容
            with open(os.path.join(path, filename), 'r', encoding='utf-8') as f:
                index = 0
                result = []
                html_content = f.read()
                # 提取中文和标点符号
                pattern = re.compile('[\u4e00-\u9fa50-9，。？！、\n]+')
                # pattern = re.compile('[\u4e00-\u9fa5a-zA-Z0-9，。？！、]+')
                matches = pattern.findall(html_content)
                # print(matches)
                all_text = ''.join(matches)
                years=get_year(all_text)
                result.append(years)

                # questions = re.findall(r'\d+问([\u4e00-\u9fff]+)[?]', all_text)
                dasta = re.split('社记者', all_text)
                if len(dasta) < 3:
                    continue
                else:
                    numnumnumnum+=1
                    print('----',filename)
                    datas = re.split('14问', all_text)
                    datas_index = 0
                    for index_data in range(len(datas)):

                        if datas_index == 0:
                            datas_index += 1
                            continue
                        elif datas_index == len(datas) - 1:
                            continue
                        else:
                            # print(datas[index_data])
                            inputdata = datas[datas_index].split('？\n14')
                            if len(inputdata) >= 2:
                                all_result.append([inputdata[0], inputdata[1],years])
                                numnum += 1
                            datas_index += 1
                # print(all_d)
    print('numnum-->', numnum,numnumnumnum)
    return all_result






def finall(data):
    file_list = []  # 存储文件名和内容的列表

    index = 10597
    output_path = "./testsss.json"
    for i in data:
        file_json = {
            "id": 0,
            "问": '',
            "答": '',
            "来源": "外交部答记者问",
            "元数据": {
                "create_time": "",
                "回答明细": "",
                "问题明细": "",
                "扩展字段": ""
            }
        }
        if len(i) != 3:
            continue
        file_json['id'] = index
        file_json['问'] = i[0].replace('141', '').replace('1414', '').replace('。1', '。').replace('？1', '？').replace('14',
                                                                                                                   '').replace(
            '1267', '').replace('\n', '')
        file_json['答'] = i[1].replace('141', '').replace('1414', '').replace('。1', '。').replace('？1', '？').replace('14',
                                                                                                                   '').replace(
            '1267', '')  .replace('\n', '')
        file_json['元数据']['create_time']=i[2]

        with jsonlines.open(output_path, mode='a') as file:
            file.write(file_json)
        file_list.append(file_json)
        index += 1
    print(len(file_list))


if __name__ == '__main__':
    # main()
    finall(main())
    # clear_wen('。问题')
