# PUBG_Effective_Range_Project

---

## 배틀그라운드 지역별 유효사정거리 측정

**데이터 가져오기**
1) Selenium
> 셀레니움을 통해서 전적통계사이트인 op.gg 의 서버별 경쟁전 상위 500명의 닉네임을 동적크롤링
2) PUBG developer API
> 배틀그라운드 개발자 API를 통해서 유저닉네임별 ID 추출
> 유저닉네임별로 최근 매치정보 ID 추출
3) Chicken dinner API
>매치정보 ID를 통해서 세부매치정보 조회

>세부매치정보 중 킬로그 데이터 추출

>맵 별로 분류 (에란겔, 미라마, 테이고) - 추후 다른맵 데이터도 추가예정
4) Data Column
>데이터는 dictionary 의 형태로 저장됩니다.

>zone : Kill이 이루어진 지역정보

>additional_info : Killer의 파츠정보

>damage_causer_name : Killer의 무기정보

>damage_reason : Victim의 피격정보

>damage_type_category : Killer의 공격수단

>distance : Killer의 공격

>is_through_penetrable_wall : 벽너머로의 피격여부

**데이터 저장**

1. MongoDB
>NoSQL 데이터베이스 중 하나인 MongoDB에 추출한 데이터 저장

>Directory명 : PUBG_MONGODB

>Database명: pubgdata

>Collection명 : steam_erangel, steam_miramar, steam_taego, kakao_erangel, kakao_miramar, kakao_taego

**분석용 대시보드 개발**

1. Metabase
> 대시보드 중 하나인 Metabase를 이용하여 MongoDB에 저장된 데이터 시각화

> 장소별 킬량 그래프 : 교전이 자주 일어나는 장소 탐색

> 무기별 킬량 그래프 : 많이 사용하는 무기 탐색

> 파츠별 킬량 그래프 : 많이 사용되는 파츠 탐색
