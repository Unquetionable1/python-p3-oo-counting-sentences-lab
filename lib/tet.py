def ss(sns):
    s=[]
    for sn in sns.split('.'):
        for subsn in sn.split('!'):
            print([subsn])
            for subsubsn in subsn.split('?'): 
                s.append(subsubsn)
    return s
sns='uydyudyid?sdyszuyduudsuds! sidduududdud.'
print(ss(sns))

