import re, json
from collections import defaultdict

lines = open('../data/academic-disciplines.md').read().split('\n')

def alpha(n):                      # 1->a, 26->z, 27->aa
    s=''
    while n>0:
        n,r = divmod(n-1,26)
        s = chr(97+r)+s
    return s

# ---------- parse ----------
raw=[]
for i,l in enumerate(lines):
    if re.match(r'^#{2,5} ', l):
        raw.append({'k':'h','lvl':len(l)-len(l.lstrip('#')),'t':l.lstrip('# ').strip(),'ln':i+1,'note':None})
    elif re.match(r'^ *- ', l):
        m=re.match(r'^( *)- (.*)$', l)
        raw.append({'k':'b','lvl':len(m.group(1))//2,'t':m.group(2).strip(),'ln':i+1,'note':None})
    elif l.strip().startswith('_') and l.strip().endswith('_') and len(l.strip())>2 and raw:
        raw[-1]['note']=l.strip().strip('_')

# ---------- assign division numbers to headings ----------
out=[]
branch=0; disc=0; sub=0
cur_div=None
bullet_ctr=[0,0,0,0]      # counters per bullet level
bullet_addr=['','','','']

def reset_bullets(from_lvl=0):
    for i in range(from_lvl,4):
        bullet_ctr[i]=0; bullet_addr[i]=''

for n in raw:
    if n['k']=='h':
        if n['lvl']==2:
            branch+=1; disc=0; sub=0
            cur_div=f"{branch}000"
        elif n['lvl']==3:
            disc+=1; sub=0
            cur_div=f"{branch}{disc:02d}0"
        else:                          # #### and ##### share the units tier
            sub+=1
            cur_div=f"{branch}{disc:02d}{sub}"
        reset_bullets(0)
        out.append({**n,'num':cur_div,'depth':n['lvl']-2})
    else:
        lv=n['lvl']
        reset_bullets(lv+1)
        bullet_ctr[lv]+=1
        c=bullet_ctr[lv]
        seg = str(c) if lv%2==0 else alpha(c)
        parent = bullet_addr[lv-1] if lv>0 else ''
        bullet_addr[lv] = parent+seg
        num = f"{cur_div}/{bullet_addr[lv]}"
        out.append({**n,'num':num,'depth':4+lv})

json.dump(out, open('../data/numbered.json','w'))

# ---------- verification ----------
nums=[o['num'] for o in out]
assert len(nums)==len(set(nums)), "COLLISION"
print(f"entries numbered : {len(out)}")
print(f"unique addresses : {len(set(nums))}  (no collisions)")
print(f"longest address  : {max(nums,key=len)}  ({len(max(nums,key=len))} chars)")
divs=[o for o in out if o['k']=='h']
print(f"4-digit divisions: {len(divs)}")
print()
for o in out[:3]+[x for x in out if x['num'] in ('1010/1d1','3011/1b3c2','5040','5047','2100/3g1a','4033/8b2')]:
    print(f"  {o['num']:<14} {'  '*o['depth']}{o['t']}")
