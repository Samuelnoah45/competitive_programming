def countingSort(arr):
    freqArr = []
    for i in range(100):
        freqArr.append(0)
        
        
    for i in range(len(arr)):
        freqArr[arr[i]] += 1
        
    return freqArr    