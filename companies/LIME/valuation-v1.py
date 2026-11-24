# LIME valuace – horizont konec 2027 (~1,1 roku), ocenění na forward 2028E
price=19.69
basic=65.32; opts=5.866; strike=9.28; rsu=3.505; war=0.04
dil_now=basic+opts*(1-strike/price)+rsu+war
cash=417.7
mcap=dil_now*price; ev=mcap-cash
print(f"Diluted now {dil_now:.1f} M, mcap {mcap:.0f}, EV {ev:.0f}")
rev26=1070; ebitda26=254; sbc=55; da26=0.125*rev26
print(f"EV/adjEBITDA26 {ev/ebitda26:.1f}x, EV/(EBITDA-SBC)26 {ev/(ebitda26-sbc):.1f}x")
# reverse: what multiple of FY26 adj EBITDA-SBC
sc={
 'bear':dict(g27=0.07,g28=0.06,m27=0.215,m28=0.21,mult=4.0,pe=10,ebitm28=0.055,capex27=0.15,p=0.30),
 'base':dict(g27=0.13,g28=0.12,m27=0.24,m28=0.25,mult=6.0,pe=16,ebitm28=0.105,capex27=0.14,p=0.50),
 'bull':dict(g27=0.19,g28=0.17,m27=0.265,m28=0.28,mult=8.0,pe=22,ebitm28=0.14,capex27=0.14,p=0.20),
}
H=1.1
shares27=dil_now*1.03  # ředění ~3 % (plán +5 %/rok, část kryta RSU už ve výpočtu)
ws=0
for k,s in sc.items():
    r27=rev26*(1+s['g27']); r28=r27*(1+s['g28'])
    e27=r27*s['m27']; e28=r28*s['m28']
    fcf27=e27-r27*s['capex27']-10+15   # daně ~10 (NOL), úroky +15
    fcf26q4=15
    cash27=cash+fcf26q4+fcf27
    ev_t=s['mult']*(e28-sbc*(1.1 if k=='bull' else 1))
    t1=(ev_t+cash27)/shares27
    ni28=(r28*s['ebitm28']+15)*0.75
    t2=ni28/shares27*s['pe']
    t=(t1+t2)/2
    ws+=s['p']*t
    print(f"{k}: rev27 {r27:.0f} rev28 {r28:.0f} ebitda27 {e27:.0f} ebitda28 {e28:.0f} fcf27 {fcf27:.0f} cash27 {cash27:.0f} | EV-metoda {t1:.1f} P/E-metoda {t2:.1f} (EPS28 {ni28/shares27:.2f}) -> cíl {t:.1f} ({t/price-1:+.0%})")
ret=ws/price-1
print(f"Vážený cíl {ws:.2f} USD, výnos {ret:+.1%}, p.a. {(1+ret)**(1/H)-1:+.1%} (H={H} r.)")
for H2 in (1.5,2.0):
    print(f"  p.a. při H={H2}: {(1+ret)**(1/H2)-1:+.1%}")
# Buy threshold: +50% => price
print(f"Cena pro +50 % k váženému cíli: {ws/1.5:.2f}")
