# Python program for implementation of Insertion Sort

def insertionSort(arr):  
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >=0 and key < arr[j] : 
			arr[j+1] = arr[j] 
			j -= 1
		arr[j+1] = key 

arr = [12,14,25,1,2,8,3,9,15,20] 
insertionSort(arr) 
print ("Sorted array is:") 
for i in arr: 
    print (i)  
