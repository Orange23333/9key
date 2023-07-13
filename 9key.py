# -*- coding: utf-8 -*-

####
# Program: 9key
# Author: Orange233
# Date: 2023 Jul 13rd
####

import os
import sys

nine_key_map = {
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

def check_key(k):
	return '2' <= k[0] and k[0] <= '9'

def check_number(n):
	return '1' <= n[0] and n[0] <= '4'

def contains(arr, v):
	i = 0
	while i < len(arr):
		if v == arr[i]:
			return True
	return False

def query_value(k, n):
	if k in nine_key_map.keys():
		temp = nine_key_map[k]
		if n in temp.keys():
			return temp[n]
	return None

if __name__ == '__main__':
	# Input Examples:
	# python 9key.py "23 33 42"
	# python 9key.py "233342"

	i = 0
	in_str = sys.argv[1]
	out_str = ''
	while(i < len(in_str)):

		# Skip whitespaces. 
		while(i < len(in_str)):
			if in_str[i] != ' ' and in_str[i] != '\t':

				# Decode
				k = in_str[i]
				if not check_key(k):
					print('Error: Unexcept key "' + k + '" at ' + str(i + 1) + '. It must be a number in 2~9.')
					os._exit(-1)
				
				i += 1
				if i >= len(in_str):
					print('Error: Unexcept number "' + k + '" at ' + str(i + 1) + ' is alone. Input numbers are not paired.')
					os._exit(-1)
				
				n = in_str[i]
				if not check_number(n):
					print('Error: Unexcept number "' + n + '" of key "' + k + '" at ' + str(i + 1) + '. If key is 7 or 9, it must be a number in 1~4. In other cases, it must be a number in 1~3. (*1)')
					os._exit(-1)
				
				v = query_value(k, n)
				if v is None:
					print('Error: Unexcept number "' + n + '" of key "' + k + '" at ' + str(i + 1) + '. If key is 7 or 9, it must be a number in 1~4. In other cases, it must be a number in 1~3.(*2)')
					os._exit(-1)
				
				i += 1

				out_str += v

				break

			i += 1
	
	print(out_str)

	os._exit(0)