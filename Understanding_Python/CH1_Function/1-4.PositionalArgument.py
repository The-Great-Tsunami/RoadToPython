#The most familiar type of argument is the positional argument, which copies the value to the corresponding parameter in order.
#인수의 가장 익숙한 유형은 값을 순서대로 상응하는 매개변수에 복사하는 위치 인수이다.

#The following function creates and stores a dictionary with positional arguments.

def meal_day(Breakfast, Lunch, Dinner):
	return {'Breakfast menu':Breakfast, 'Lunch menu':Lunch, 'Dinner menu':Dinner}

Day1 = meal_day('French Fries', 'Sushi', 'Steak')

#Although very common, the downside of positional arguments is that you need to know the meaning of each position.
