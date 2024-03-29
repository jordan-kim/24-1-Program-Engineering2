# 주민등록번호에서 생년월일, 성별 추출하는 함수
def ext(a):

    # 123456-789000을 [123456, 789000]로 나누기
    b = a.split('-')

    # 성별로 출생년 1900과 2000 나누기. 그 다음 성별 결정
    sec = int(b[1][0])
    cen = "19" if sec <= 2 else "20"
    sex = "남자" if sec % 2 == 1 else "여자"

    # 12년 34월 56일 추출
    y = b[0][:2] #년
    m = b[0][2:4] #월
    d = b[0][4:6] #일

    return f"나는 {cen}{y}년 {m}월 {d}일에 태어난 {sex}입니다."

a = input("주민등록번호를 입력하세요: ")

print(ext(a))