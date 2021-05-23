Email = input("이메일을 입력하세요.\n")

if Email[Email.index('@'):] == "@co.kr":
    print("domain is co.kr.")
else : print("domain is not co.kr")