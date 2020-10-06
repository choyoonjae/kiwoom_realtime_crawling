순환신경망을 활용한 호가데이터 기반의 주식시장 예측에 대한 연구 프로젝트

키움증권의 api를 활용하여 2019년 3월 20일부터 2019년 5월 7일까지 코스닥(KOSDAQ) 시가총액 상위 50종목의 실시간 호가 잔량 정보를 수집함.




using PYTHON{

1. real_time_crawler.py

키움증권에서 제공하는 open api를 통해 수집대상인 종목코드와 컬럼을 정의

2. execute.py

real_time_crawler에서 정의한 데이터를 수집하여 로컬에 종목&일자 별로 파일을 생성하여 저장

}

using R{

3. data_preprocessing.R

수집된 데이터를 분석에 적합한 형태로 변환하기 위한 전처리 코드 1

4. dataset_generating.R

수집된 데이터를 분석에 적합한 형태로 변환하기 위한 전처리 코드 2

}

using tensorflow{

4. 
