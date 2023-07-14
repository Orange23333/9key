# -*- coding: utf-8 -*-

####
# Program: 9key
# Author: Orange233
# Date: 2023 Jul 13rd
####

import os
import sys

__nine_key_map = {
	'2': {
		'1': 'a',
		'2': 'b',
		'3': 'c',
	},
	'3': {
		'1': 'd',
		'2': 'e',
		'3': 'f',
	},
	'4': {
		'1': 'g',
		'2': 'h',
		'3': 'i',
	},
	'5': {
		'1': 'j',
		'2': 'k',
		'3': 'l',
	},
	'6': {
		'1': 'm',
		'2': 'n',
		'3': 'o',
	},
	'7': {
		'1': 'p',
		'2': 'q',
		'3': 'r',
		'4': 's',
	},
	'8': {
		'1': 't',
		'2': 'u',
		'3': 'v',
	},
	'9': {
		'1': 'w',
		'2': 'x',
		'3': 'y',
		'4': 'z',
	},
}

def __check_key(k):
	return '2' <= k[0] and k[0] <= '9'

#def __check_number(n):
#	return '1' <= n[0] and n[0] <= '4'

def __query_value(k, n):
	if k in __nine_key_map.keys():
		temp = __nine_key_map[k]
		if n in temp.keys():
			return temp[n]
	return None

def main(cipher_text):
	i = 0
	result = ''
	while(i < len(cipher_text)):

		# Skip whitespaces. 
		while(i < len(cipher_text)):
			if cipher_text[i] != ' ' and cipher_text[i] != '\t':

				# Decode
				k = cipher_text[i]
				if not __check_key(k):
					return None, 'Error: Unexcept key "' + k + '" at ' + str(i + 1) + '. It must be a number in 2~9.'
				
				i += 1
				if i >= len(cipher_text):
					return None, 'Error: Unexcept number "' + k + '" at ' + str(i + 1) + ' is alone. Input numbers are not paired.'
				
				n = cipher_text[i]
				#if not __check_number(n):
				#	return None, 'Error: Unexcept number "' + n + '" of key "' + k + '" at ' + str(i + 1) + '. If key is 7 or 9, it must be a number in 1~4. In other cases, it must be a number in 1~3. (*1)'
				
				v = __query_value(k, n)
				if v is None:
					return None, 'Error: Unexcept number "' + n + '" of key "' + k + '" at ' + str(i + 1) + '. If key is 7 or 9, it must be a number in 1~4. In other cases, it must be a number in 1~3. (*2)'
				
				i += 1

				result += v

				break

			i += 1
	
	return result, None

if __name__ == '__main__':
	# Input Examples:
	# python 9key.py "23 33 42"
	# python 9key.py "233342"

	__result, __err = main(sys.argv[1])

	if __err is not None:
		print("Error: " + __err)
		os._exit(-1)

	print(__result)
	os._exit(0)
