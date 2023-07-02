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

def get_years(date_str):
    from datetime import datetime

    # 将日期字符串转换为 datetime 对象
    date_obj = datetime.strptime(date_str, "%Y年%m月%d日")

    # 将日期对象格式化为指定格式的日期字符串
    formatted_date_str = date_obj.strftime("%Y%m%d")

    return formatted_date_str
def main():
    import re

    import os
    from bs4 import BeautifulSoup

    # 指定路径
    path = "test/"  # 目标文件夹路径

    all_result = []
    nums=0
    numnum=0
    # 循环遍历指定路径下的所有文件
    all_len=0
    all_len_len=0
    for filename in os.listdir(path):
        print('进度为->',nums*100/1700,'%')
        nums+=1
        if filename.endswith('.html'):
            # 打开HTML文件并读取其中的内容
            with open(os.path.join(path, filename), 'r', encoding='utf-8') as f:
                index = 0
                result = []
                html_content = f.read()
                # 提取中文和标点符号
                pattern = re.compile('[\u4e00-\u9fa50-9，。？！、]+')
                # pattern = re.compile('[\u4e00-\u9fa5a-zA-Z0-9，。？！、]+')
                matches = pattern.findall(html_content)
                # print(matches)
                all_text = ''.join(matches)
                match = re.search(r"\d{4}年\d{1,2}月\d{1,2}日", all_text)
                if match is None:
                    years=None
                else:
                    years=get_years(match.group())
                    print(years,'-----')
                result.append(years)
                # questions = re.findall(r'\d+问([\u4e00-\u9fff]+)[?]', all_text)
                dasta = re.split('\d答', all_text)
                # print(dasta)
                # first_q=re.split('\d问',dasta[0])[1]
                # dasta.pop(0)
                all_d = []
                # all_d.append(first_q)
                # if index > 10:
                #     return all_result
                for qqq in dasta:
                    # print('')
                    data_i = re.split('\d问', qqq)
                    all_len+=len(data_i)
                    for dd in data_i:
                        first_q = re.split('\d问', dd)
                        for ddd in first_q:
                            pattern_dd = r'\d{7,}'
                            result_dd = re.sub(pattern_dd, '', ddd)
                            # print(len(all_d), result_dd)
                            pattern_ddd = r'？.{0,5}答'
                            tes = re.split(pattern_ddd, result_dd)
                            all_d.append(result_dd)
                            for qqqq in tes:
                                if index == 0:
                                    index += 1
                                    all_len_len+=1
                                    continue
                                if '问' in qqqq:
                                    tess = re.split("[。！？；：“”‘’【】《》〈〉（）()、]+问", qqqq)
                                    for qqqqq in tess:
                                        result.append(qqqqq)
                                else:
                                    result.append(qqqq)
                                    # print(qqqq)
                                    # print('1')
                                index += 1
                                numnum+=1
                                print(numnum)

                        # print('data_i->',len(data_i))
                # print('end')
                all_result.append(result)
                # print(all_d)
    print(all_len,all_len_len)
    return all_result


def data格式(datas):
    result = []
    tiaoguo=0
    for data in datas:
        inputs = []
        years=data.pop(0)
        for index in range(len(data)):
            dat = data[index]
            if index == len(data) - 2 or index == len(data) - 1:
                # print(dat)
                tiaoguo+=1
                continue
            if (index + 1) % 2 != 0:
                # 问题
                inputs.append(dat)
            else:
                # 答案
                inputs.append(dat)
                inputs.append(years)
                result.append(inputs)
                inputs = []
        # print('once')
    print('跳过了->',tiaoguo)
    return result


{
    "id": 23495,
    "问": "How to Drive a Car in Reverse Gear",
    "答": "1. Backing Up in a Straight Line\n1-1. Conduct a “360 degree check.”\nA “360 degree check” is when you actively turn your head and shoulders to look all around your vehicle in a complete circle.  Make sure there is nothing in your way or moving toward you that you may need to take into account before backing up.\nIt’s okay to use your mirrors to aid in your check, but it’s important that you actively look around to ensure you don’t miss anything.\nMake sure to look toward the ground on either side of your vehicle using your head and mirrors to ensure there are no people or animals laying in your path.\n1-2. Place your right foot on the brake.\nWhen driving forward or in reverse, your right foot should be the only one on the gas or brake pedal.  If your car is equipped with a standard transmission, your left foot manages the clutch, but in vehicle’s with automatic transmissions, the left foot simply goes unused.  Press your right foot on the brake pedal firmly, so that the vehicle won’t move once it is in reverse.\nThe brake pedal is in the middle on vehicle’s equipped with a standard transmission and is the furthest to the left in automatic vehicles.\nThe brake pedal is the widest pedal.\n1-3. Put your left hand on the top middle of the steering wheel.\nWhile it may be customary to drive with your hands at ten and two o’clock on the steering wheel, backing up will require that you turn your body to the right.  Place your left hand at the top of the wheel so you can easily make small adjustments to keep the vehicle moving straight as you back up.\nIt may be difficult to reach the steering wheel with your right hand while backing up, so steering with one hand is optimal.\n1-4. Put the vehicle in reverse.\nDepending on the transmission your vehicle came equipped with, there are a few ways you may need to shift into reverse.  On automatic vehicles, it usually requires pressing a button on the shift lever and pulling it backward until it is aligned with the letter “R.”  In standard vehicles equipped with a five speed transmission, you can usually shift into reverse by pressing the shift lever all the way to the left and pulling it backward.\nIn vehicles equipped with six speed standard transmissions, reverse is usually all the way to the left and up, next to first gear.\nSome cars require that you press down on the shift lever or press a release to access the reverse gear.\nIf you are unsure of how to shift into reverse, refer to your vehicle’s owner’s manual.\n1-5. Look out the back of the car over your passenger side shoulder.\nProvided your view is not obstructed, twist your body to the passenger side so you can look out the back window of your vehicle over your right or passenger side shoulder.  Make sure you do not remove your foot from the brake pedal.  If you are driving a box truck or other vehicle that blocks your view out the back window, you will have to rely on your side mirrors to guide you.\nYou may choose to place your right hand on the top of the passenger seat to help you comfortably look out the back.\nIf you are relying on your mirrors, make sure to check each of them frequently.\n1-6. Ease your right foot off the brake slowly.\nAs you take the pressure off of the brake pedal with your right foot, the vehicle will begin to move backward.  Most vehicle’s engines idle at a high enough RPM (revolutions per minute) to propel the vehicle without any need to apply the gas. Keep your foot hovering over the brake pedal as you back up just in case you need to stop or slow down.\nEase off the brake slowly to ensure you do not accelerate too quickly to easily manage..\nIf your vehicle is equipped with a standard transmission, you will need to use the gas as you ease off the clutch, but can then allow the vehicle to idle.\n2. Turning as You Back Up\n2-1. Turn the wheel in the direction you want the back of the car to turn.\nThe dynamic of driving in reverse is quite different than that of normal driving because the wheels you turn to steer are at the front of the car.  As you back up, make small adjustments by turning the wheel in the direction you want the back of the car to turn toward.\nTurning the wheel to the left as you back up will cause the back of the car to go left and vice versa.\nStop the car if you feel uneasy about the direction it is heading, then set off again once you’ve gained control.\n2-2. Check the clearance of the front end.\nAs you turn the vehicle, the front end of the car will swing in the opposite direction the back end is turning.  Check the area around the front of the car frequently as you back up slowly to ensure you don’t hit or run over anything with the front wheels.\nIf you are turning left as you back up, the front of the car will swing to the right, and vice versa.\nMake sure you are going slowly enough that you can check the front of the car for clearance without hitting anything.\n2-3. Transition your right foot to the gas pedal if needed.\nIf you are backing up a hill or need to turn, you may need to utilize the gas pedal occasionally while backing up.  Once your right foot is completely off of the brake, move it over the gas pedal to the right of the brake.  Press down on the pedal slowly to control the amount of speed you pick up as you back up.\nMake subtle adjustments to your speed by applying pressure to the gas pedal.\nBring your foot back to the brake once you have gained sufficient speed or if you need to slow back down.\n2-4. Use two hands to steer when turning.\nIf you need to turn around an obstacle while backing up, you may want to use both hands to manipulate the steering wheel.  Using one hand, you can usually only turn the wheel up to ninety degrees in each direction, so if you need to take a steeper turn, using both hands may help.  Make sure that you can still see behind you as you place your right hand back on the wheel if you need to.\nNever cross your hands over one another while turning the wheel.  Instead push the wheel with one hand and pull it with the other.\n2-5. Never go faster than you feel comfortable controlling.\nBacking up can feel quite different than driving forward, and your view is often compromised by the back of the car and a limited view out of your window.  Do not hurry yourself while backing up and instead take your time to prevent accidents.\nNever drive your vehicle in a manner that feels unsafe.\nFeel free to stop the vehicle and take a minute if you feel uncertain about what you’re doing.\n2-6. Press the brake with your right foot firmly to stop.\nWhen you’ve backed up far enough, press your foot back down on the brake pedal gradually to come to a smooth stop.  Be careful not to apply too much pressure too quickly, or you will stop the vehicle abruptly.\nUse only your right foot to apply the brakes in your vehicle.\nKeep your foot pressed on the brake once the vehicle has stopped.\n2-7. Put the vehicle in park or set the parking brake when you’re done.\nWith your foot firmly on the brake pedal, press the button the shift lever in automatic vehicles and press it forward until it is aligned with the “P” that indicates that it is in park.  In standard transmission equipped vehicles, simply take the shift lever out of gear (in neutral) and apply the parking brake by pulling up on the handle or pressing down on the pedal.\nIf you are unsure where to locate your parking brake or how to engage it, refer to the vehicle’s owner’s manual for guidance.\n3. Backing Up Using Your Mirrors\n3-1. Check your mirrors before you begin.\nIf you cannot see out the back of the vehicle, you will need to use your side mirrors to see as you back up.  Before you begin, adjust your side mirrors to ensure you can see the side of the vehicle, the ground, and anything coming up from behind you.\nIn many cars you can adjust both mirrors from the driver’s seat, but in some you may need to adjust them manually by hand on each side.\n3-2. Check each mirror frequently.\nUsing mirrors will only show you what is behind your vehicle on either side, so it’s important to check both sides often.  This will prevent you from accidentally hitting something, or from not noticing as someone approaches from one side or the other.\nYou likely will need to drive even slower in reverse when using mirrors to be sure you don’t miss anything.\nIt may help to pay closer attention to the mirror on a side with an obstacle, so you can keep your eyes on it.\n3-3. Enlist the help of a friend.\nIf you are backing up using only your mirrors in a difficult area, you may choose to ask a friend to guide you.  Using your mirrors to keep an eye on a friend that is checking your clearances from the back may be your best option when driving a box truck or something else with severely limited visibility.\nHave your friend stand behind the vehicle on one side to ensure you can see them as they guide you.\nMake sure to open your windows and turn off the radio to hear your friend’s instructions as you back up.\n",
}


def finall(data):
    file_list = []  # 存储文件名和内容的列表

    index=0
    output_path="./data4shtml1.json"
    tiaoguo=0
    for i in data:
        file_json = {
            "id": 0,
            "问": '',
            "答": '',
            "来源": "外交部新闻发布会",
            "元数据": {
                "create_time": "",
                "回答明细":"",
                "问题明细": "",
                "扩展字段": ""
            }
        }
        if len(i)!=3:
            tiaoguo+=1
            continue
        file_json['id']=index
        file_json['问']=i[0].replace('141','').replace('1414','').replace('。1','。').replace('？1','？').replace('14','').replace('1267','')
        file_json['答']=i[1].replace('141','').replace('1414','').replace('。1','。').replace('？1','？').replace('14','').replace('1267','')
        file_json['元数据']['create_time']=i[2]
        with jsonlines.open(output_path, mode='a') as file:
            file.write(file_json)
        file_list.append(file_json)
        index+=1
    print(len(file_list))
    print('跳过了->',tiaoguo)



if __name__ == '__main__':
    # main()
    finall(data格式(main()))
    # clear_wen('。问题')
