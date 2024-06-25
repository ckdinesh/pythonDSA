# Type Code	C Type	Python Type	Minimum size in Bytes
# ‘b’	signed 			char			int	1
# ‘B’	unsigned 		char			int	1
# ‘u’	Py_UNICODE	Unicode 		character	2
# ‘h’	signed 			short			int	2
# ‘H’	unsigned 		short			int	2
# ‘i’	signed 			int				int	2
# ‘I’	unsigned 		int				int	2
# ‘l’	signed 			long			int	4
# ‘L’	unsigned 		long			int	4
# ‘q’	signed long long				int	8
# ‘Q’	unsigned long long				int	8
# ‘f’	float							float	4
# ‘d’	double							float	8

#
# Below are some operations that can be performed in an array:
#
# append()
# insert()
# pop()
# remove()
# index()
# reverse()

# importing "array" for array operations
import array

# initializing array with array values and signed integers
arr = array.array('i', [1, 2, 3])

# printing original array
print ("The new created array is : ",end=" ")
for i in range (0, 3):
	print (arr[i], end=" ")
print("\r")

# using append() to insert new value at end
arr.append(4);

# printing appended array
print("The appended array is : ", end="")
for i in range (len(arr)):
	print (arr[i], end=" ")
