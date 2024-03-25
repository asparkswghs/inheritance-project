# Import classes from kernels.py
from kernels import Kernel, Unix, Minix, Linux, BSD, FreeBSD, XNU, NT

# Show breif history of some of the operating systems being represented
tree = f'''
Inheritance Project - a hirearchy of Operating System Kernels

━ Unix
   ┃
   ┣━ Minix
   ┃    ┆
   ┣━━ Linux
   ┗━ BSD
       ┣━━ FreeBSD
       ┗━━ XNU

━━ (DOS)
     ┆
  ━━ NT

'''
print(tree)


unix = Unix('AT&T Research Unix', 124.78)
minix = Minix()
linux = Linux()
bsd = BSD()
freebsd = FreeBSD()
xnu = XNU()

dos = Kernel('DOS', None, 0.875)
nt = NT()

tests = [
    unix,
    minix,
    linux,
    bsd,
    freebsd,
    xnu,
    dos,
    nt,
    'GNU'
]

pad = lambda x: ' ' * (51 - len(str(x))) # Create padding for legibility, so everything is nice and aligned
                                         # Uses '51' as the base, as that's the length of the longest name.

for item in tests:
    if isinstance(item, Kernel):
        print(str(item) + pad(item) + ' is a Kernel.')
    else:
        print(str(item) + pad(item) + ' is NOT a Kernel.')

print(f'Unix + Minix = {unix + minix}')

