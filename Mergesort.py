# To do
# 1.create a func for insert_data from a List
# 2.get length func
# 3.remove the element at index
# 4. insert( 0,"")

class Mergesort:

    def merge(self, arr1, arr2):

        #edge cases
            #1.arr1[n] < arr2[1]
            #2.arr2[n] < arr1[1]

        next_array=0
        merged_array=[]
        for i in range(len(arr1)):
            if arr1[i] < arr2[next_array]:
                merged_array.append(arr1[i])
            else:
                for j in range(next_array,len(arr2)):
                    if arr2[j] < arr1[i]:
                        merged_array.append(arr2[j])
                        if i == ( len(arr1)-1 ):
                            merged_array.append(arr1[i])
                    else:
                        merged_array.append(arr1[i])
                        next_array = j
                        break

        print(merged_array)

if __name__ == '__main__':

    a1 = [17,21,29,38,45]
    a2 = [4,9,25,32,56,78]

    mm = Mergesort()
    mm.merge(a1,a2)

