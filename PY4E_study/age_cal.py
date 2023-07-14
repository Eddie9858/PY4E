from datetime import datetime


def cal(birth_year, birth_month, birth_day):

	# 현재 날짜와 입력받은 날짜 불러오기
	rn = datetime.now()
	birth = datetime(birth_year, birth_month, birth_day)


	# 출력할 한국나이와 현재나이 변수할당
	age = rn.year - birth.year
	korean_age = f"한국 나이는 {age + 1}세 입니다."
	current_age = f"\n현재 나이는 {age}세 입니다."


	# 1. 생일 판별하기
	if birth.month == rn.month and birth.day == rn.day:

		# 탄생일 판별하여 탄생 축하메세지 출력(탄생일이라서 나이생략)
		if birth.year == rn.year:
			print("\n탄생을 축하합니다!")

		# 탄생일외에는 생일 축하메세지와 나이 출력
		else:
			print("\n생일을 축하힙니다!")
			print(korean_age, current_age)

	#2. 입력받은 년도가 현재보다 크다면 아직 태어나지 않음 메세지 출력
	elif birth.year > rn.year:
		print("아직 태어나지 않았습니다!")
		birth_input()

	#3. 년도가 같을경우
	elif birth.year == rn.year:

		#년도는 같으나 미래의 날짜일경우
		#예외1. month가 미래의 month 일경우
		if birth.month > rn.month:
			print("아직 태어나지 않았습니다!")
			birth_input()

		#예외2. month도 같으나 day만 미래의 day일 경우
		elif birth.month == rn.month and birth.day > rn.day:
			print("아직 태어나지 않았습니다!")
			birth_input()

		# 그외 정상 출력
		# 년도가 같기때문에 현재년도 - 출생년도 = 현재나이
		else:
			print(korean_age, current_age)

	#4. 현재 월이 출생월보다 크거나
	#5. or 달이 같을 경우 day가 현재보다 작다면 생일이 지났으므로 현재나이 출력
	elif birth.month < rn.month or (birth.month == rn.month and birth.day < rn.day):
		print(korean_age, current_age)

	#6. 나머지 경우 생일이 안지났으므로 현재나이-1 출력
	else:
		current_age = f"\n현재 나이는 {age-1}세 입니다."
		print(korean_age, current_age)


def birth_input():
	#무한루프
	while True:
		try:
			# 사용자 입력 받아서 각 변수에 숫자로 변환하여 할당
			birth_year, birth_month, birth_day = input('\n생년월일을 입력하세요(예시: 2000.01.01): ').split('.')
			birth_year = int(birth_year)
			birth_month = int(birth_month)
			birth_day = int(birth_day)

			#변환한 변수 cal함수에 할당
			cal(birth_year, birth_month, birth_day)
			#무한루프 탈출
			break

		# 문자입력, 12월을 초과하는 숫자입력, 해당월의 초과하는 날짜 입력 예외처리
		except (NameError, ValueError):
			print("생년월일을 제대로 입력해주세요!")
		# 무한루프이므로 다시 while문으로 돌아감


birth_input()
