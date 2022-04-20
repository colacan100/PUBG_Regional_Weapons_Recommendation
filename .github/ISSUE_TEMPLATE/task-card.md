---
name: Task Card
about: Task 카드 생성시 사용되는 template입니다.
title: ''
labels: ''
assignees: ''

---

## Task Card

""Assignee** : 박성우

#### Job Description

**데이터 가져오기**
1) Selenium
> 셀레니움을 통해서 전적통계사이트인 op.gg 의 서버별 경쟁전 상위 500명의 닉네임을 동적크롤링
2) PUBG developer API
> 배틀그라운드 개발자 API를 통해서 유저닉네임별 ID 추출
> 유저닉네임별로 최근 매치정보 ID 추출
3) Chicken dinner API
>매치정보 ID를 통해서 세부매치정보 조회

>세부매치정보 중 킬로그 데이터 추출

**데이터 저장**

1. NoSQL - MongoDB
>NoSQL 데이터베이스 중 하나인 MongoDB에 추출한 데이터 저장

>Directory명 : PUBG_MONGODB

>Database명: pubgdata

>Collection명 : steam_data

>쿼리 :
```
{
    "_id": {
        "$oid": "625febde77348e530d8cdf2b"
    },
    "map": "Tiger_Main",
    "rank": {
        "$numberInt": "36"
    },
    "zone": "palace",
    "additional_info": [],
    "damage_causer_name": "WeapMini14_C",
    "damage_reason": "HeadShot",
    "distance": {
        "$numberDouble": "416.1879577636719"
    }
}
```

2. SQL - SQLite

>Database명: pubg_result.db

>스키마 :
```
_id VARCHAR NOT NULL PRIMARY KEY,
map VARCHAR,
rank INTEGER,
zone VARCHAR,
damage_causer_name VARCHAR,
damage_reason VARCHAR,
distance REAL,
additional_info VARCHAR
```

**분석용 대시보드 개발**

1. Metabase
> 대시보드 중 하나인 Metabase를 이용하여 MongoDB에 저장된 데이터 시각화

![image](https://user-images.githubusercontent.com/85010611/164219950-e07eb972-4e8e-4b5f-9673-ebaf5f2b1fcc.png)
> 배틀그라운드 경쟁전 맵 종류

> 많이 나오는 경쟁전 맵 TOP 5

> 미라마의 주요 교전장소

> 에란겔의 주요 교전장소

> 태이고의 교전장소

![image](https://user-images.githubusercontent.com/85010611/164220099-eb0c7113-249d-4133-a056-f7a0d2565876.png)

> PUBG 무기 종류

> 킬을 많이한 총기 TOP5

> 에란겔의 선호무기

> 미라마의 선호무기

> 태이고의 선호무기

**머신러닝 모델 적용**

1. SVD(Singular value Decomposition)
> 특이값 분해 모델을 통해서 추천시스템 개발

> 각 맵,지역과 무기를 사용하여서 Rank 타겟을 예측한다.

> 가장 낮은 Rank, 즉 가장 높은 순위의 무기를 결과로 내보낸다.

> 학습한 model은 pickle을 통해서 부호화

**웹페이지 구현**

![image](https://user-images.githubusercontent.com/85010611/164220901-97574bea-824c-4b44-ad40-2651582dad70.png)

> 메인이미지 클릭시 홈화면으로 돌아옴

> 맵 선택시 지역리스트 자동 업데이트

> 맵과 지역을 선택한 후 Click버튼 클릭시 추천무기, 서브이미지 출력

> 서브이미지 클릭시 상세정보창으로 넘어감

**웹 페이지 배포**

1. AWS ec2
> 클라우드 플랫폼 중 하나인 AWS ec2를 이용하여 배포

> 로컬의 경우 : http://127.0.0.1:5000/

> AWS ec2를 이용한 경우 : http://15.164.89.222:5000/

> 다른 ip를 이용하여 확인했을 때 정상동작
