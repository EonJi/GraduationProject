# -*- encoding: utf-8 -*-
from txt_util.file_op import read_file_utf8, write_file_utf8
from txt_util.abs_paths import get_paths

dir_name = 'C:/Users/qnrud/Desktop/크롤링_평점/'
files = get_paths(dir_name)

for f in files:
    try:
        c = read_file_utf8(f)
        c = c.replace('data-v-3b8e06cb="">','')
        c = c.replace('[단종]', '').strip()
        c = c.replace('&amp', '')
        c = c.replace('<span class="product-main-info__product_name__discontinue">','').strip()

        c = c.replace('[','')
        c = c.replace(']','')

        c = c.split('\r\n\r\n')

        title = c[0].replace('<title>','').replace('/','').strip().replace('[단종]','').replace('\r\n','').strip()
        brand = c[1].replace('<brand>','').replace('/','')
        score = c[2].replace('<score>','').replace('<score','').replace('/','')
        i = c[3].replace('<icon_score>','').replace('<div class="list-item"','').replace('<span class="icon icon-sprite gpa-','').replace('<div class="bar-wrap"','').replace('<p class="joiner"','').split(',')

        best = i[0].split('<')
        best_icon = best[0].replace('"','').strip()
        # print(best_icon)
        best_1 = best[1].split('>')
        best_score = best_1[1].strip()
        # print(best_score)

        icon_score=[]

        icon_score.append(best_icon)
        icon_score.append(best_score)

        good = i[1].split('<')
        good_icon = good[0].replace('"','').strip()
        # print(best_icon)
        good_1 = good[1].split('>')
        good_score = good_1[1].strip()
        # print(best_score)

        icon_score.append(good_icon)
        icon_score.append(good_score)

        soso = i[2].split('<')
        soso_icon = soso[0].replace('"','').strip()
        # print(best_icon)
        soso_1 = soso[1].split('>')
        soso_score = soso_1[1].strip()
        # print(best_score)

        icon_score.append(soso_icon)
        icon_score.append(soso_score)

        bad = i[3].split('<')
        bad_icon = bad[0].replace('"', '').strip()
        # print(best_icon)
        bad_1 = bad[1].split('>')
        bad_score = bad_1[1].strip()
        # print(best_score)

        icon_score.append(bad_icon)
        icon_score.append(bad_score)

        worst = i[4].split('<')
        worst_icon = worst[0].replace('"', '').strip()
        # print(best_icon)
        worst_1 = worst[1].split('>')
        worst_score = worst_1[1].strip()
        # print(best_score)

        icon_score.append(worst_icon)
        icon_score.append(worst_score)

        # print(icon_score)
        # #
        # print(icon_score[1])
        #
        best_s = int(icon_score[1])*50
        good_s = int(icon_score[3])*30
        soso_s = int(icon_score[5])*15
        bad_s = int(icon_score[7])*5
        worst_s = int(icon_score[9])*0

        total = str(best_s + good_s + soso_s + bad_s + worst_s)

        tag = c[4].replace('<tag>','').replace('/','')
        rank = c[5].replace('<rank>','').replace('/','')

        p_list = []
        p_list.insert(0,title)
        p_list.insert(1,brand)
        p_list.insert(2,score)
        p_list.insert(3,total)
        p_list.insert(4,tag)
        print(p_list)

        wfname = './평점/' + f.split('/')[-1]
        write_file_utf8(wfname, '|'.join(p_list)+'\n')

    except:
        print('no')
