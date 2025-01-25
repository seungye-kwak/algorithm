def is_valid_password(password):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # 조건 1: 모음을 반드시 하나 포함해야 함
    if not any(char in vowels for char in password):
        return False

    # 조건 2: 모음 3개 혹은 자음 3개가 연속으로 나오면 안 됨
    for i in range(len(password) - 2):
        if (password[i] in vowels and password[i+1] in vowels and password[i+2] in vowels) or \
           (password[i] not in vowels and password[i+1] not in vowels and password[i+2] not in vowels):
            return False

    # 조건 3: 같은 글자가 연속으로 두 번 오면 안 되나, 'ee'와 'oo'는 예외
    for i in range(len(password) - 1):
        if password[i] == password[i+1] and password[i] not in {'e', 'o'}:
            return False

    return True

def main():
    while True:
        password = input().strip()
        if password == "end":
            break

        if is_valid_password(password):
            print(f"<{password}> is acceptable.")
        else:
            print(f"<{password}> is not acceptable.")

if __name__ == "__main__":
    main()