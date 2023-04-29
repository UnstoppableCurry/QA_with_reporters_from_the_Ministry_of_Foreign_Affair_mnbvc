import docx
import glob
import re
import jsonlines


# 检验是否全是中文字符
def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True


zhPattern = re.compile(u'[\u4e00-\u9fa5]+')


def clear_data(input_path):
    all_data = []
    paths = glob.glob(input_path)
    for path in paths:
        data_file_list = []
        text_file = ''
        file = docx.Document(path)
        for p in file.paragraphs:
            # print(p.text)
            text_file += p.text
        print(text_file)
        list_all = text_file.split('问：')
        title = list_all.pop(0)

        for i in list_all:
            print(i)
            if len(i.split('答')[0].split('Q:')) < 2:
                print('error')
            en_Q = i.split('答')[0].split('Q:')[1]
            zh_Q = i.split('答')[0].split('Q:')[0]
            answer = i.replace('A:', '').split('答：')[1].split(' ')
            zh_A = []
            en_A = []
            for a in answer:
                if a.__len__() == 0:
                    continue
                if zhPattern.search(a):
                    zh_A.append(a)
                else:
                    en_A.append(a)

            zh_file_json = {'input': '',
                            'instruction': zh_Q,
                            'output': zh_A,
                            'date': title.split('日）')[0].split('（')[1].replace('年', '-').replace('月', '-'),
                            'title': title.split('日）')[0].split('（')[0]}
            en_file_json = {'input': '',
                            'instruction': en_Q,
                            'output': en_A,
                            'date': title.split('日）')[0].split('（')[1].replace('年', '-').replace('月', '-'),
                            'title': title.split('日）')[1]}
            output = {'en': en_file_json, 'zh': zh_file_json}
            all_data.append(output)
    return all_data


def clear_api(input_path, output_path):
    all_data = clear_data(input_path)
    print('数据总量->', len(all_data))
    with jsonlines.open(output_path, mode='w') as file:
        for i in all_data:
            file.write(i)


if __name__ == '__main__':
    input_path = "/www/baidu/外交部/外交部问答/中英对照/*.docx"
    output_path = "./data4docx.json"
    clear_api(input_path, output_path)
