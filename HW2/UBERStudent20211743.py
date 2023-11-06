#!/usr/bin/python3

import sys
from datetime import datetime

# 커맨드라인 인자 체크
if len(sys.argv) != 3:
    print("주의!! IMDBStudent20151047.py <첫번째 인자:inputF> <두번째 인자:outputF>")
    sys.exit()

# 커맨드라인 인자에서 파일 이름 가져오기
input_file = sys.argv[1]
output_file = sys.argv[2]

# 데이터를 저장할 사전 생성
uber_dict = dict()

# 입력 파일 열기
with open(input_file, 'r', encoding='utf-8') as f:
    for line in f: # 파일 한 줄씩 정독
        line = line.strip() # 양끝의 공백 제거
        fields = line.split(',') # ',' 기준으로 쪼개기
        region = fields[0] # 0: 지역
        date_str = fields[1] # 1: 날짜
        vehicles = int(fields[2]) # 2: 차량
        trips = int(fields[3]) # 3: 운행된 수
        
        # 날짜 문자열을 datetime 객체로 변환(검색후 발견)
        date = datetime.strptime(date_str, "%m/%d/%Y")
        
        # 요일 코드 생성
        weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        day = weekday[date.weekday()]
        
        # 지역과 요일을 키로 사용하여 데이터 저장
        key = "%s,%s" % (region, day)
        if key in uber_dict: # 이미 존재한다면 +1
            uber_dict[key][0] += vehicles
            uber_dict[key][1] += trips
        else: # 없으면 삽입
            uber_dict[key] = [vehicles, trips]

# 결과를 출력 파일에 쓰기
with open(output_file, 'w', encoding='utf-8') as f:
    for key, value in uber_dict.items():
       f.write("%s %d,%d\n" % (key, value[0], value[1]))
        
# 너랑 쟤랑 똑같이 했는데 너는 왜 잘될까?????
