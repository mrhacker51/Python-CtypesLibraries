from ctypes import *
import sys


def main():
	my_test_c_lib = CDLL("/root/my_library.so")
	result = my_test_c_lib.topla(5,5)
	print(result)
	# sys.exit()
	result = my_test_c_lib.cikar(15,5)
	print(result)
	# sys.exit()
	result = my_test_c_lib.carp(5,5)
	print(result)
	# sys.exit()

if __name__ == '__main__':
	main()



