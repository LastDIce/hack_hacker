import string
import random

#https://goni9071.tistory.com/entry/java-한글-이름-랜덤-생성
first_list = ["김", "이", "박", "최", "정", "강", "조", "윤", 
"장", "임", "한", "오", "서", "신", "권", "황", "안",
        "송", "류", "전", "홍", "고", "문", "양", "손", 
        "배", "조", "백", "허", "유", "남", "심", "노", 
        "정", "하", "곽", "성", "차", "주",
        "우", "구", "신", "임", "나", "전", "민", "유", "진", 
        "지", "엄", "채", "원", "천", "방", "공", "강", "현", 
        "함", "변", "염", "양",
        "변", "여", "추", "노", "소", "신"]

second_list = ["가", "강", "건", "경", "고", "관", "광", 
"구", "규", "근", "기", "길", "나", "남", "노", "다",
        "단", "담", "대", "덕", "도", "동", "두", 
       "마", "만", "명", 
        "무", "문", "미", "민", "바", "박",
         "범",  "병", "보", "산", "상", 
        "새", "서", "석", "선", "설",  "성", "세", 
        "소", "솔", "수", "숙", "순",
        "숭", "승", "시", "아", "안", "애", 
        "여", "영", "예", "옥", "완", "용", "우", "원", "위",
        "유", "윤", "율", "은", "의", "이", "익", 
        "인", "일", "잔", "장", "재", "전", "정", "제", "조", "종", "준",
        "중", "지", "진", "찬", "창", "채", "천", "철", "초", 
        "충", "치", "탐", "태", "판", "하", "한", "해", "현", "형",
        "혜", "호", "홍", "화", "회", "효", "훈", "휘", 
        "희", "운", "배", "부", "혼", "황", "비",
         "탁", "온", "균", "송", "욱", "령", "성",
        "열",  "변", "양", "흥", "식", "란", "실",
         "복", "헌", "엽", "학", "평", "향"]

Third_list = ["곤","울", "학", "림","규", "건", "근", 
"길","영", "섭","슬", "재", "석", "민", "원", "연",
            "혁","홍", "현", "남", "슬", "철", "자","별",
            "은","윤","주","훈","린","우", "철", "빈", "솔","욱","환","을","아", "범","중","인",
            "영","정", "권","우","협", "용", "웅",]

def random_id_pw():
   id = ""
   for i in range(random.randint(4,8)):
      id += random.choice(string.ascii_lowercase)
   for i in range(random.randint(3,5)):
      id += random.choice(string.digits)
   return id

def random_name():
	return random.choice(first_list)+random.choice(second_list)+random.choice(Third_list)

def random_price():
	return str(random.randint(1, 60)) + "0000"

def random_small_price():
	return str(random.randint(1, 15)) + "0000"

def random_munsang():
	number = []
	for i in range(3):
		nm = ""
		for j in range(4):
			nm += random.choice(string.digits)
		number.append(nm)
	nm = ""
	for i in range(6):
		nm += random.choice(string.digits)
	number.append(nm)
	return number