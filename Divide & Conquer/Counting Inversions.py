#https://www.coursera.org/lecture/algorithms-divide-conquer/o-n-log-n-algorithm-for-counting-inversions-i-GFmmJ

#https://medium.com/@ssbothwell/counting-inversions-with-merge-sort-4d9910dc95f0

#Really amazing to understand how merge sort works! :) 



def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr)/2]
        b = arr[len(arr)/2:]
        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a)-i)
    c += a[i:]
    c += b[j:]
	return c, inversions