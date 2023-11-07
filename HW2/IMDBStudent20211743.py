#!/usr/bin/python3

import sys

# 커맨드라인 인자 체크
if len(sys.argv) != 3:
    print("주의!! IMDBStudent20151047.py <첫번째 인자:inputF> <두번째 인자:outputF>")
    sys.exit()

# 커맨드라인 인자에서 파일 이름 가져오기
input_file = sys.argv[1] 
output_file = sys.argv[2] 

# 장르별 영화 수를 저장할 사전 생성
genre_dict = dict()

# 입력 파일 movie.dat 파일 열기
with open(input_file, 'r', encoding='utf-8') as f:
    for line in f: # 파일 한 줄씩 정독
        line = line.strip() # 양끝의 공백 제거
        fields = line.split('::') # '::' 기준으로 쪼개기 → 3개 나오는 걸 확인
        genres = fields[-1].split('|') # 마지막 필드(장르 정보)를 '|'로 쪼개기
        for genre in genres: # 각 장르에 대하여
            if genre in genre_dict: # 사전 안에 있다면
                genre_dict[genre] += 1 # +1 해주기
            else:
                genre_dict[genre] = 1 # 없다면 넣기

# 결과를 출력 movieoutput.txt로 저장
with open(output_file, 'w', encoding='utf-8') as f:
    for genre, count in genre_dict.items():
        f.write("%s %d" % (genre, count))

# 도대체 뭐가 문제일까요..???? 알 수가 없네요???? 단어찾기를해도 개수는 맞는데 어디에서 18개나 틀렸을까요??? 와아아아아아아
# 결과는 정상동작 하는데 뭐꼬..? 개수를 다시 
