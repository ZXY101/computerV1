# Compuer

def mixs(num):
	try: 
		ele = float(num)
		return (0, ele, '')
	except ValueError:
		return (1, num, '')

def sqrt(x):
	n = 1
	for _ in range(10):
		print(n)
		n = (n + x/n) * 0.5


def find_degree(equation):
	degree = 0
	i = 0

	for char in equation:
		if char == '^':
			deg = float(equation[i + 1])
			if deg > degree:
				degree = deg
		i += 1
	return degree

def simplify_side(side):
	#5 * X^0 + 4 * X^1 = 4 * X^0
	#5 + 4x - 4
	i = 0
	simplified_side = []
	while i < len(side):
		if side[i] == "-":
			simplified_side.append("-" + side[i + 1]) 
			i += 2
		elif side[i] == "+":
			simplified_side.append(side[i + 1]) 
			i += 2
		else:
			simplified_side.append(side[i]) 
			i += 1
	return simplified_side

def carry_right_over(left_side, right_side):
	i = 0
	for num in right_side:
		if num[0] != '-':
			right_side[i] = '-' + num
		else:
			right_side[i] = num.replace("-", '')
		i += 1

	left_side.extend(right_side)
	return left_side

def simplify_equation(left_side, right_side):
	simplified_left = simplify_side(left_side)
	simplified_right = simplify_side(right_side)

	carried_over = carry_right_over(simplified_left, simplified_right)
	for index,x in enumerate(carried_over):
		i = 0
		while i < len(x):
			if x[i] == "^" and x[i + 1] == "0":
				carried_over[index] = x[0:i - 1]
			elif x[i] == "^" and x[i + 1] == "1":
				carried_over[index] = x[0:i]
			i += 1
	return carried_over

def solve_degree_1(equation):
	i = 0
	for x in equation:
		if (x.find('X') == -1):
			equation[i] = float(x)
		i+=1
	equation.sort(key = mixs)
	
	final = []
	final.append(equation[0])
	i = 1

	while i < len(equation):
		if isinstance(final[0], float) and isinstance(equation[i], float):
			final[0] += equation[i]
			i += 1
		else:
			break

	temp = []
	while i < len(equation):
		if (equation[i] == 'X'):
			temp.append(1)
		elif (equation[i] == '-X'):
			temp.append(-1)
		else:
			temp.append(float(equation[i].replace('X','')))
		i+=1

	x = temp[0]
	i = 1
	while i < len(temp):
		x += temp[i]
		i +=1
	if x == 1 or x == -1:
		x = 'X'
	else:
		x = str(x) + "X"
	
	final.append(x)
	print("---------------------")
	print("The degree is: 1")
	if (final[0] < 0):
		print("Simple form is: ",final[1] +' - '+ str(final[0]*-1) + " = 0")
	else:
		print("Simple form is: ",final[1] +' + '+ str(final[0]) + " = 0")

	div = str(final[1]).replace('X','')
	if div =='':
		div = 1
	print("The solution is: ",final[0]/float(div) *-1)

def solve_quad(equation):
	#ax^2 + bx + c = 0
	print(equation)
	a = float(equation[0].replace("X^2", ""))
	b = float(equation[1].replace("X", ""))
	c = equation[2]

	root_part = (b * b - 4 * a * c) ** 0.5
	den = 2 * a

	root1 = (b * -1 + root_part) / den
	root2 = (b * -1 - root_part) / den
	print("root1", root1)
	print("root2",root2)




def solve_degree_2(equation):
	i = 0
	for x in equation:
		if (x.find('X') == -1):
			equation[i] = float(x)
		i+=1
	equation.sort(key = mixs)
	print(equation)
	
	digit_total = equation[0]
	i = 1

	while i < len(equation):
		if isinstance(digit_total, float) and isinstance(equation[i], float):
			digit_total += equation[i]
			i += 1
		else:
			break

	first_degree_total = []
	while i < len(equation):
		if (equation[i] == 'X'):
			first_degree_total.append(1)
		elif (equation[i] == '-X'):
			first_degree_total.append(-1)
		elif equation[i].find("^") == -1:
			first_degree_total.append(float(equation[i].replace('X','')))
		i+=1

	x = first_degree_total[0]
	i = 1
	while i < len(first_degree_total):
		x += first_degree_total[i]
		i +=1
	if x == 1 or x == -1:
		x = 'X'
	else:
		x = str(x) + "X"

	second_degree_total = []
	while i < len(equation):
		if (equation[i] == 'X^2'):
			second_degree_total.append(1)
		elif (equation[i] == '-X^2'):
			second_degree_total.append(-1)
		elif equation[i].find("^") > 0:
			second_degree_total.append(float(equation[i].replace('X^2','')))
		i+=1
	

	x2 = second_degree_total[0]
	i = 1
	while i < len(second_degree_total):
		x2 += second_degree_total[i]
		i +=1
	if x2 == 1 or x2 == -1:
		x2 = 'X^2'
	else:
		x2 = str(x2) + "X^2"

	equation_final = []
	
	equation_final.append(digit_total)
	equation_final.append(x)
	equation_final.append(x2)
	equation_final.reverse()
	print("The simple form is: ", equation_final)
	solve_quad(equation_final)
	
def main():

	print("Welcome to CompuerV1!")
	print("--------------------------", 4**0.5)

	# equation = input("Please enter a valid equation:")
	# equation = "5 * X^0 + 4 * X^1 = 4 * X^0"
	equation = "5 * X^0 + 3 * X^1 + 3 * X^3 = 1 * X^0 + 0 * X^1"
	highest_degree = find_degree(equation)

	if highest_degree > 2:
		print("The degree is greater than 2, baka mitai!")
		exit()

	if highest_degree == 0:
		print("The solution is ALL real numbers, baka mitai!")
		exit()

	split_sides = equation.replace(' * ','').split("=")

	simplfied_equation = simplify_equation(split_sides[0].split(), split_sides[1].split())

	if (highest_degree == 1):
		solve_degree_1(simplfied_equation)
	if (highest_degree == 2):
		solve_degree_2(simplfied_equation)


if __name__ == "__main__":
	main()
