def s_f (number):
    return number%10

list=[]

list.sort( key= s_f )

print("Ваш отсортированный список:", list, sep="\n")
