def sorting(list, n):
    i, j, tmp, swap = 0, 0, 0, 0
    for i in range (n):
        i+=1
        for j in range (n-i-1):
            j+=1
            if(list[j]>list[j+1]):
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp
                print("["+str(list[j])+","+str(list[j+1])+"] -> "),
                swap+=1
                for k in range(len(list)):
                    print(str(list[k])),
                    if k == len(list)-1:
                        print("\n")
    return swap
list = [4, 9, 7, 5, 8, 9, 3]
swap = sorting(list, len(list))
print("Jumlah Swap : "+str(swap))