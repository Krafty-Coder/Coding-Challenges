def count_positives_sum_negatives(arr):
    i = [i for i in arr if i>0]
    j = [i for i in arr if i<0]
    return [] if len(arr)==0 else [len(i), sum(j)] 

