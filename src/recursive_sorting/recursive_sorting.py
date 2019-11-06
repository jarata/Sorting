# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TODO
    merged_arr = []
    while len(arrA) > 0 or len(arrB) > 0:
      if len(arrA) > 0 and len(arrB) == 0:
        for num in arrA:
          merged_arr.append(arrA.pop(0))
      elif len(arrB) > 0 and len(arrA) == 0:
        merged_arr += arrB
        arrB = []
      else:
        if arrA[0] < arrB[0]:
          merged_arr.append(arrA.pop(0))
        else:
          merged_arr.append(arrB.pop(0))
        
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TODO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TODO
    
    
    return arr

def merge_sort_in_place(arr, l, r): 
    # TODO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
