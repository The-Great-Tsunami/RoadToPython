# Default arguments are created when the function is first defined and are not recreated when the function is called multiple times.
# Therefore, the result list keeps referencing the same object each time the function is called multiple times.
# 기본 인수는 처음 함수를 정의할 때 생성, 함수가 여러 번 호출되어도 재생성되지 않는다.
# 따라서 result 리스트는 함수가 여러 번 호출될 때마다 같은 객체를 계속해서 참조하게 된다.

# The following function has a generic parameter arg and result which takes an empty list as default parameter. The function adds arg to the result list.
# You can expect that a list with one item will be returned each time the function is called, but the result of the previous call is output as it is in the list.
# 다음 함수에는 일반 매개변수 arg와 기본 매개변수로 빈 리스트를 취하는 result가 있다. 함수는 arg를 result 리스트에 추가한다.
# 함수를 호출헐 때마다 한 항목이 있는 리스트가 반환될 것이라고 예상할 수 있지만, 이전에 호출했던 result가 그대로 리스트에 남아있는 상태로 출력된다.

def pokemon(arg, result=[]):
	result.append(arg)
	print(result)

pokemon('pikachu')
pokemon('Pairi')

def pokemons(arg):
	result = []  #In this case, the list result is recreated every time the function is called. # 이 경우에는 함수를 호출할 때마다 리스트 result가 다시 생성된다.
	result.append(arg)
	return result

print(pokemons('pikachu'))
print(pokemons('pairi'))
