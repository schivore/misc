import pandas as pd,numpy.random as nr


words=['WELL','PULL','FULL','WALL','BUZZ','FIZZ','BACK','STICK','FLICK','PAL']

df=pd.DataFrame(words)

def conceal(s,n):

    l=list(s)

    for i in range(n):
        l[nr.randint(len(l))]='_'
    return "".join(l)

df[1]=df[[0]].apply(lambda x:conceal(x[0],1),axis=1)
df[2]=df[[0]].apply(lambda x:conceal(x[0],1),axis=1)
df[3]=df[[0]].apply(lambda x:conceal(x[0],2),axis=1)
df[4]=df[[0]].apply(lambda x:conceal(x[0],2),axis=1)
df[5]=df[[0]].apply(lambda x:conceal(x[0],3),axis=1)
df[6]=df[[0]].apply(lambda x:conceal(x[0],3),axis=1)

df.to_csv(r"/Users/seb/Documents/spelling.csv",index=False,header=None)

print(df)