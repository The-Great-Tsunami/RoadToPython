#'None' is a value that means there is nothing. It looks like 'False' of a boolean value, but means a different value.
#'None'은 아무것도 없다는 것을 뜻하는 값이다. Boolean 값의 False처럼 보이지만 다른 값을 의미한다.

thing = None

if thing:
	print("It's some thing")

else:
	print("It's no thing")

#If you want to distinguish between 'False' and 'None', use the operator 'is'.
#Boolean값 False와 None을 구분하기 위해 is연산자를 사용한다.

thing = None

if thing is None:
	print("It's nothing")

else:
	print("It's something")