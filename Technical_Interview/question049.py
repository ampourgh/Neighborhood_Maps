# ENCRYPTION

# haveanicelife -> haee anl vii ecf
# Read top down from column to column

s = 'haveanicelife'

rint, rfloat = int(len(s) ** 0.5), len(s) ** 0.5

cols = rint < rfloat and rint + 1 or rint

for i in range(cols):
    print(s[i::cols], end=' ')
   
# Alternative Method

s = list('haveanicelife'.strip())
L =  len(s)
row = math.floor(L**(1/2))
col = math.ceil(L**(1/2))

for i in range(col):
    x = 0     
    while True:
        try:
            print(s[i+x],end='')
            x+= col
        except:
            break        
    print(' ',end='')
