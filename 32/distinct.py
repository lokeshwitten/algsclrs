def distinct_matcher(T,S):
    n=len(T)
    m=len(S)
    s=0
    while(s<=n-m):
        for i in range(0,m):
            if(T[s+i]==S[i]):
                if(i==m-1):
                    print('Pattern found at {0},{1}'.format(s,s+m-1))
                    print(T[s:s+m])
                    s=s+m-1
                    break
            else:
                if(i==0):
                    s+=1
                    break
                s+=i
                break
t='lokeshisagreathutylokeshuihuihuilokeshgcfcdcgxccghchhfyftyfyftyftxcrffffffffffffffffffffftyfyguihhuiufydrtdhuihctyfuyjguyhfghjolkioguygjhfyfcytdrtfgdyfvyjhgyhvtyfyhvuyjhvghcgvyfycfvycuyhvihikhikhnopkkljjvgfxc cgvrfresxqwrdrtugoihojhojnftsvghihig'
s='lokesh'
distinct_matcher(t,s)
