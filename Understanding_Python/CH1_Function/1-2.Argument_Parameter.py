#Let's define a shouting() function with a parameter called inPut.
#inPut 파라미터와 함께 shouting() 함수를 정의해보자.
#Return the inPut variable with the return statement.
#inPut 변수를 return문으로 값을 반환한다.


#Values passed to a function are called 'arguments'.
#함수로 전달한 값을 인수하고 부른다.
#When calling a 'argument' and a 'function', the value of the 'argument' is copied to the corresponding 'parameter' within the function.
#인수와 함수를 호출하면 인수의 값은 함수 내에서 해당하는 매개변수에 복사된다.


### They are called 'arguments' outside the function, but are called 'parameters' inside the function.
### 함수 외부에서는 인수라고 하지만 내부에서는 매개변수라고 부른다.
def shouting(inPut):
	return "This is a " + inPut

print(shouting('Pikachu'))

def catch_color(color):
	if color == 'red':
		return "It's a Tomato"
	elif color == 'green':
		return "It's a green Peper"
	elif color == 'yellow':
		return "It's a banana"
	else:
		return "I've never heard of the color " + color + "."

print(catch_color('red'))
print(catch_color('blue'))

