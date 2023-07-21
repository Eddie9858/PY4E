from datetime import datetime


def calculate_age(birth_year, birth_month, birth_day):
    # 현재 날짜와 입력받은 날짜 불러오기
    now = datetime.now()
    birth = datetime(birth_year, birth_month, birth_day)

    # 출력할 나이 변수 할당
    age = now.year - birth.year

    # 생일 판별
    if birth.month > now.month or (birth.month == now.month and birth.day > now.day):
        age -= 1

    return age


def get_birthday_input():
    while True:
        try:
            # 사용자 입력 받아서 각 변수에 숫자로 변환하여 할당
            birth_year, birth_month, birth_day = map(int, input('생년월일을 입력하세요(예시: 2000.01.01): ').split('.'))
            return birth_year, birth_month, birth_day
        except ValueError:
            print("생년월일을 제대로 입력해주세요!")


def print_age_information(age):
    print(f"한국 나이는 {age + 1}세입니다.")
    print(f"현재 나이는 {age}세입니다.")


def main():
    birth_year, birth_month, birth_day = get_birthday_input()
    age = calculate_age(birth_year, birth_month, birth_day)
    print_age_information(age)


if __name__ == '__main__':
    main()