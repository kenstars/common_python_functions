#! /usr/bin/env python2.7

def array_merger(array_list):
    """
    This function can be used to sort and merge k sorted arrays , where k is the number of arrays
    """
    new_array = []
    length_array = len(array_list)
    range_array = range(length_array)
    array_tmp = [array_list[array_index].pop(0) for array_index in range_array]
    while array_tmp:
         combined_value = zip(range_array,array_tmp)
         min_value = min(combined_value, key = lambda x:x[1])
         new_array.append(min_value[1])
         try:
             new_replace_element = array_list[min_value[0]].pop(0)
         except Exception :
             array_tmp.pop(min_value[0])
         else:
             array_tmp[min_value[0]] = new_replace_element 
    return new_array 





if __name__ == "__main__":
   print array_merger([[3,6,10],[2,4,5]])
