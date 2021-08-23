# -*- coding:utf-8 -*-
import pymysql
from txt_util.get_ngram import ngram
import numpy as np
from txt_util.cosine_sim import cos


def db_category(a):

    sql = "select * from product where p_category like '%{}%'".format(a) # 카테고리가 스킨인 상품

    cursor.execute(sql)
    result = cursor.fetchall() # 상품정보가 스킨인거 모두 가져옴

    return result


if __name__ == "__main__":
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='cosbot', charset='utf8')

    cursor = conn.cursor()

    while True:
        print('안녕하세요! 당신의 피부에 좋은 화장품을 추천해주는 COSBOT입니다!')
        print('추천 받고 싶은 화장품 카테고리를 입력하세요')
        print('예시 : 스킨')
        recommend = input("카테고리 : ")  # 사용자에게 추천받고 싶은 카테고리 명 입력받게 하기 # 입력하세요 : 스킨

        a = input("입력하신 카테고리가 맞나요? 맞다면 정확하게 yes를 입력해주세요 : ")

        if a == 'yes':

            print('추천시작!!!!')
            result = db_category(recommend)

            neg_q = input("기존에 사용했던 화장품 중 트러블이 생겼던 화장품의 이름을 입력해주세요 : ")
            # print(neg_q)
            neg_q = neg_q.replace(' ', '')
            # print(neg_q)

            neg_r = ngram(list(neg_q), [3])
            # print(neg_r) #나쁜화장품이름 트라이그램

            for i in result:
                p_name = ngram(list(i[0].replace(' ', '')), [3])

                data = list(set(list(set(' '.join(p_name).split())) + list(set(' '.join(neg_r).split()))))

                vocab_dic = dict([(w, i) for i, w in enumerate(data)])

                v1 = np.zeros(len(vocab_dic))

                v2 = np.zeros(len(vocab_dic))

                for w in neg_r:
                    v1[vocab_dic[w]] = 1

                for w in p_name:
                    v2[vocab_dic[w]] = 1

                if cos(v1, v2) > 0.5: # 이름을 유사도비교, 코사인유사도점수가0.3이상이면
                    p = i[5] # 성분
                    # print(p)

                    NL = []  # 부정적인 성분을 넣을 리스트

                    for i in p.split(','):

                        NL.append(i)

                    print('NL',NL)

            pos_q = input("기존에 사용했던 화장품 중 좋았던 화장품의 이름을 입력해주세요 : ")

            pos_q = pos_q.replace(' ', '')

            pos_r = ngram(list(pos_q), [3])
            # print(pos_r) #좋은화장품이름 트라이그램

            for i in result:
                p_name = ngram(list(i[0].replace(' ', '')), [3])

                data = list(set(list(set(' '.join(p_name).split())) + list(set(' '.join(pos_r).split()))))

                vocab_dic = dict([(w, i) for i, w in enumerate(data)])

                v1 = np.zeros(len(vocab_dic))

                v2 = np.zeros(len(vocab_dic))

                for w in pos_r:
                    v1[vocab_dic[w]] = 1

                for w in p_name:
                    v2[vocab_dic[w]] = 1

                if cos(v1, v2) > 0.4:
                    # print(cos(v1,v2))
                    p = i[5]
                    # print(p)

                    PL = []

                    for i in p.split(','):
                        PL.append(i)

                    print('PL2 : ', PL)

            a = list(db_category(recommend))
            b = sorted(a, key=lambda tup: tup[7], reverse=True) #1차로 평점이 높은 순서대로 정렬

            top_20 = sorted(b, key=lambda tup: tup[8],reverse=False)[-20:] #2차로 우리가 만든 사용자 토탈점수를 이용하여 토탈점수가 높은 상위 3개 항목 가져오기

            PL_LAST = list(set(PL)-set(NL))  #긍정적인 성분에서 부정적인 성분을 제외시킨것
            print('PL_LAST : ', PL_LAST)

            # print(top_20, '카테고리에서 top20개 뽑아오기')
            #
            # print(PL_LAST, '긍정-부정')

            top_list = []

            for n in top_20:
                top_20_list = n[5].split(',')

                data_1 = list(set(list(set(' '.join(PL_LAST).split())) + list(set(' '.join(top_20_list).split()))))
                # print(data_1)

                v_dic = dict([(w, i) for i, w in enumerate(data_1)])

                # print(v_dic)

                va = np.zeros(len(v_dic))

                vb = np.zeros(len(v_dic))

                for w in PL_LAST:
                    va[v_dic[w]] = 1

                for w in top_20_list:
                    vb[v_dic[w]] = 1

                print(cos(va,vb), n[0])

                if cos(va,vb) > 0:
                    # print(n[0])
                    top_list.append(n)

            # print(top_list)

            top_list = sorted(top_list, key=lambda x:x[1], reverse=False)[-3:]

            print(top_list)

            print('추천된 제품 3가지 입니다.')
            print('\n')

            for i in top_list:

                print('추천된 제품명 : ',i[0])
                print('브랜드 : ', i[2])
                print('가격 : ', i[3])
                print('이 화장품은 : ', i[4], '피부타입에 맞는 화장품입니다.')
                print('이 제품은 ',i[9],'에 효과적입니다~!')
                print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
                print('\n')

            conn.close()

        else:

            print('다시입력해주세요')
            continue

        break
