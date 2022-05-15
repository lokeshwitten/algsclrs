def naive_matcher(T,S):
    index=0
    count=0
    while(index<=len(T)-len(S)):
        for i in range(0,len(S)):
            if(T[index+i]==S[i]):
                if(i==len(S)-1):
                    print('PATTERN FOUND at {0},{1}'.format(index,index+len(S)-1))
                    index+=1
                    break
                continue
            else:
                index+=1
                break
l='lokeshisgreatlokesh'
s='lokesh'
naive_matcher(l,s)
