# -*- encoding: utf-8 -*-
from txt_util.file_op import read_file_utf8, write_file_utf8
from txt_util.abs_paths import get_paths

dir_name = 'C:/Users/qnrud/Desktop/크롤링_최종/'
files = get_paths(dir_name)

for f in files:
    c = read_file_utf8(f)
    cont = c.replace('<span class="icon-sprite rating-grade-icon gpa-','')
    content = cont.replace('-small" data-v-58a43844="">','')

    try:
        dry_score = 0  # 건성
        oily_score = 0  # 지성
        sensitive_score = 0  # 민감성
        composite_score = 0  # 복합성
        normal_score = 0  # 중성

            # -*- 건성점수 -*-
        if '건성 · best':
            count = cont.count('건성 · best')
            dry_score = dry_score + 50 * count

        if '건성 · good':
            count = cont.count('건성 · good')
            dry_score = dry_score + 30 * count

        if '건성 · soso':
            count = cont.count('건성 · soso')
            dry_score = dry_score + 15 * count

        if '건성 · bad':
            count = cont.count('건성 · bad')
            dry_score = dry_score + 5 * count

        if '건성 · worst':
            count = cont.count('건성 · worst')
            dry_score = dry_score + 0 * count

        # -*- 지성 점수 -*-
        if '지성 · best':
            count2 = cont.count('지성 · best')
            oily_score = oily_score + 50 * count2

        if '지성 · good':
            count2 = cont.count('지성 · good')
            oily_score = oily_score + 30 * count2

        if '지성 · soso':
            count2 = cont.count('지성 · soso')
            oily_score = oily_score + 15 * count2

        if '지성 · bad':
            count2 = cont.count('지성 · bad')
            oily_score = oily_score + 10 * count2

        if '지성 · worst':
            count2 = cont.count('지성 · worst')
            oily_score = oily_score + 0 * count2

        # print('지성점수', oily_score)

        # -*- 중성 점수 -*-

        if '중성 · best':
            count3 = cont.count('중성 · best')
            normal_score = normal_score + 50 * count3

        if '중성 · good':
            count3 = cont.count('중성 · good')
            normal_score = normal_score + 30 * count3

        if '중성 · soso':
            count3 = cont.count('중성 · soso')
            normal_score = normal_score + 15 * count3

        if '중성 · bad':
            count3 = cont.count('중성 · bad')
            normal_score = normal_score + 5 * count3

        if '중성 · worst':
            count3 = cont.count('중성 · worst')
            normal_score = normal_score + 0 * count3

        # print('중성점수', normal_score)

        # -*- 민감성점수 -*-

        if '민감성 · best':
            count4 = cont.count('민감성 · best')
            sensitive_score = sensitive_score + 50 * count4

        if '민감성 · good':
            count4 = cont.count('민감성 · good')
            sensitive_score = sensitive_score + 30 * count4

        if '민감성 · soso':
            count4 = cont.count('민감성 · soso')
            sensitive_score = sensitive_score + 15 * count4

        if '민감성 · bad':
            count4 = cont.count('민감성 · bad')
        sensitive_score = sensitive_score + 5 * count4

        if '민감성 · worst':
            count4 = cont.count('민감성 · worst')
            sensitive_score = sensitive_score + 0 * count4

        # print('민감성점수', sensitive_score)

        # -*- 복합성점수 -*-

        if '복합성 · best':
            count5 = cont.count('복합성 · best')
            composite_score = composite_score + 50 * count5

        if '복합성 · good':
            count5 = cont.count('복합성 · good')
            composite_score = composite_score + 30 * count5

        if '복합성 · soso':
            count5 = cont.count('복합성 · soso')
            composite_score = composite_score + 15 * count5

        if '복합성 · bad':
            count5 = cont.count('복합성 · bad')
            composite_score = composite_score + 5 * count5

        if '복합성 · worst':
            count5 = cont.count('복합성 · worst')
            composite_score = composite_score + 0 * count5

        # print('복합성점수', composite_score)

        product_list = []

        if max(dry_score, composite_score, oily_score, sensitive_score, normal_score) == dry_score:
            product_list.append('건성')

        elif max(dry_score, composite_score, oily_score, sensitive_score, normal_score) == composite_score:
            product_list.append('복합성')

        elif max(dry_score, composite_score, oily_score, sensitive_score, normal_score) == oily_score:
            product_list.append('지성')

        elif max(dry_score, composite_score, oily_score, sensitive_score, normal_score) == sensitive_score:
            product_list.append('민감성')

        elif max(dry_score, composite_score, oily_score, sensitive_score, normal_score) == normal_score:
            product_list.append('중성')


        a = content.split('/<ingredient>')

        # print(a[1])
        b = a[1].split('\r\n\r\n')

        if b[1].count('[단종]')>0:
            dd = b[1].split(']')
            discontinued = dd[0].replace('<title>','').replace('\r\n','').replace('[','').strip()
            # print(discontinued)
            product_list.insert(6,'O') #단종
        else:
            product_list.insert(6,'X') #단종아님

        title = b[1].replace('<title>','').replace('/','').strip().replace('[단종]','').replace('\r\n','').strip()

        category = b[2].replace('<category>','').replace('/','').strip().replace('\r\n                             ','/')
        # print(category)

        brand = b[3].replace('<brand>','').replace('/','').strip()
        # print(brand)

        price = b[4].replace('<price>','').replace('/','').strip()
        # print(price)

        product_list.insert(0,title)
        product_list.insert(1,category)
        product_list.insert(2,brand)
        product_list.insert(3,price)


        ing = a[0].replace(' ','').replace('\r\n','').replace('<ingredient>','').replace('[','').replace(']','')
        # print(ing)

        product_list.insert(5,ing)
        print(product_list)

        wfname = './상품데이터/' + f.split('/')[-1]
        write_file_utf8(wfname, '|'.join(product_list)+'\n')

    except:
        print('no')

