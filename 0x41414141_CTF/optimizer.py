from pwn import *
import sys, os

cnx = remote('207.180.200.166',9660)

# ignore first two lines
cnx.recvline()
cnx.recvline()

# LEVEL 1 : Tower of Hanoi

while 1:

	l1 = cnx.recvline()
	arr = l1.decode("utf-8").rstrip().replace('> ', '').strip('][').split(', ')
	if 'level 2' in arr[0]:
		break
	cnx.send(str.encode('{}'.format(2**(len(arr)) - 1)))


# LEVEL 2 : merge sort

def get_count_invs(arr, n): 
  
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count 

while  1:

	l2 = cnx.recvline()
	arr = l2.decode("utf-8").rstrip().replace('> ', '').strip('][').split(', ')
	if 'flag' in arr[0]:
		print(l2)
		break
	arr = [int(i) for i in arr]
	cnx.send(str.encode('{}'.format(get_count_invs(arr,len(arr)))))

cnx.close()

# flag{g077a_0pt1m1ze_3m_@ll}