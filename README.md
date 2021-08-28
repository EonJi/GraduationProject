# GraduationProject
graduation project 2019 (Cosmetic recommendation system based on ingredient information)

## 개요
화장품 이름으로부터 추출한 화장품 성분을 이용한 화장품 추천 시스템을 제안한다. 사용자가 추천받고자 하는 화장품의 카테고리를 입력받은 후 사용자에게 좋았던 화장품 이름과 트러블이 생겼던 화장품 이름을 입력받는다. 코사인 유사도를 이용해 사용자가 입력한 화장품 정보를 찾고 성분정보들을 각 각 리스트에 넣는다. 좋았던 화장품의 성분에서 트러블이 생겼던 화장품 성분을 빼준 후 따로 리스트에 넣어준다. 사용자가 입력한 카테고리에서 평점 순으로 정렬하고 이모티콘을 이용해 부여한 점수가 높은 순서대로 정렬해준 후 최종적으로 순위가 높은 상위 20개 항목을 뽑아온 후 그것의 성분과 가장 유사한 상위 3개 제품을 추천해준다.

## Skill
- Language : python
- DB : MySQL
- 수행 환경 : python 3.7 idle
- os : windows

## Simulation
https://user-images.githubusercontent.com/35449029/130458447-88ad76c8-67ca-4ed9-aafd-1bdb56e31d33.mp4
