#To avoid positional argument confusion, arguments can be given names that correspond to parameters. You can even specify the instances in a different order than the function definition.
#위치 인수의 혼란을 피하기 위해 매개변수에 사응하는 이름을 인수에 지정할 수 있다. 심지어 인스를 함수 정의와 다른 순서로 지정할 수 있다.

def meal_day(Breakfast, Lunch, Dinner):
	return {'Breakfast menu':Breakfast, 'Lunch menu':Lunch, 'Dinner menu':Dinner}

Day2 = meal_day(Lunch='French Fries', Breakfast= 'Sushi', Dinner= 'Steak')

print(Day2)