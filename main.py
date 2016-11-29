import time
import platform

#Algoritmo para parmutação dos índices de um vetor
#code source: https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/nextperm.py
def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return True

#Converte um array em um inteiro
def parse_array_to_integer(arr): 
	string = ''.join(arr)
	return int(string)


#Identifica se a série é um pandigital de acordo com as regras: 
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2 d3 d4  =406 is divisible by 2
# d3 d4 d5  =063 is divisible by 3
# d4 d5 d6  =635 is divisible by 5
# d5 d6 d7  =357 is divisible by 7
# d6 d7 d8  =572 is divisible by 11
# d7 d8 d9  =728 is divisible by 13
# d8 d9 d10 =289 is divisible by 17
def is_pandigital(number):
	test_index  = 0
	arr_index   = 1

	arr_test_div = [2, 3, 5, 7, 11, 13, 17]

	while(test_index < 7): 
		value = parse_array_to_integer(number[arr_index:arr_index+3])

		if not value % arr_test_div[test_index] == 0:
			return False

		test_index += 1
		arr_index  += 1
	return True


def get_microtime(): 
	return int(round(time.time() * 1000))

#Rodando teste
start_value = list('0123456789')
pandigital_sum = 0

started_at = get_microtime()

while(next_permutation(start_value)): 
	if is_pandigital(start_value): 
		pandigital_sum += parse_array_to_integer(start_value);

print("Pandigital sum result: %s" % pandigital_sum)

stoped_at = get_microtime()

print('Elapsed time: %f milliseconds' % round(stoped_at - started_at))
print('Processor %s' % platform.processor())
