w = 0
x = 0
y = 0
z = 0

def pad(s):
    return "0" * (4 - len(s)) + s

print("a b c d e f g h i j k l m")

for i in range(9 + 1):
    bits = pad(bin(i)[2:])
    w = 0 if bits[0] == "0" else 1
    x = 0 if bits[1] == "0" else 1
    y = 0 if bits[2] == "0" else 1
    z = 0 if bits[3] == "0" else 1

    aa = 1 ^ ((1 ^ w) & (1 ^ x) & (1 ^ y) & z)
    bb = 1 ^ ((1 ^ w) & (1 ^ y) & (x ^ z))
    cc = 1
    dd = 1 ^ ((1 ^ w) & (((1 ^ x) & (1 ^ y) & z) | ((1 ^ x) & y & (1 ^ z)) | ((1 ^ x) & y & z) | (x & y & z)))
    ee = 1 ^ ((1 ^ w) & x & (y ^ z))
    ff = 1 ^ (z & (1 ^ w) & (((1 ^ x) & (1 ^ y)) | (x & y)))
    gg = 1 ^ (((1 ^ w) & (1 ^ x) & (1 ^ y)) | ((1 ^ w) & x & y & z))
    hh = 1
    ii = (1 ^ z) & ((y & (1 ^ w)) | ((1 ^ y) & (1 ^ x)))
    jj = 1 ^ ((1 ^ w) & (1 ^ x) & y & (1 ^ z))
    kk = 1 ^ ((x & (i(1 ^ w) & ((y & z) | ((1 ^ y) & (1 ^ z))))) | ((1 ^ x) & ((1 ^ y) & z)))
    ll = kk
    mm = 1

    # res = [aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm]
    # print(" ".join([str(x) for x in res]))

    on  = "#"
    off = " "

    aa = on if aa == 1 else off
    bb = on if bb == 1 else off
    cc = on if cc == 1 else off
    dd = on if dd == 1 else off
    ee = on if ee == 1 else off
    ff = on if ff == 1 else off
    gg = on if gg == 1 else off
    hh = on if hh == 1 else off
    ii = on if ii == 1 else off
    jj = on if jj == 1 else off
    kk = on if kk == 1 else off
    ll = on if ll == 1 else off
    mm = on if mm == 1 else off

    print(f"i: {i}")
    print(f"{aa}{bb}{cc}")
    print(f"{dd} {ee}")
    print(f"{ff}{gg}{hh}")
    print(f"{ii} {jj}")
    print(f"{kk}{ll}{mm}")
    print("")
