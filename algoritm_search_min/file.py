def find_Smallest(a r r): 
  smallest = arr[0]
  smallest_index = 0
  for i in range(l, len(arr)): 
    if arr[i] < smallest: 
      smallest = arr[i] 
      smallest_index = i 
  return smallest_index 


def selectionSort(arr): 
   newArr = [] 
   for i in range(len(arr)): 
    smallest = indSmallest(arr) · 
    newArr.append(arr.pop(smallest)) 
   return newArr 

print (selectionSort([S, З, 6, 2, 10])) 