from typing import Optional
# Kernels

class Kernel:
    """
    Class for operating system kernels.
    Parameters:
    - name: the name of the kernel
    - monolithic: a boolean, True if the kernel is monolithic, False if it is not (a microkernel), None if it is hybrid.
    - size: size of kernel in MB
    - loc: lines of code in the kernel's source
    """
    def __init__(self, name: str, monolithic: Optional[bool], size: float=0, loc: int=0):
        self.name = name
        self.monolithic = monolithic
        self.size = size
        self.loc = loc

    def __repr__(self):
        return f'<{self.name} Kernel, {self.get_arch()}, {self.size} MB, {self.loc} LOC>'
    
    def __add__(self, other):
        if self.monolithic == other.monolithic:
            monolith = self.monolithic
        else:
            monolith = None
        if self.name == other.name:
            name = self.name
        else:
            name = f'{self.name}/{other.name}'
        if self.loc == -1:
            loc = other.loc
        elif other.loc == -1:
            loc = self.loc
        else:
            loc = self.loc + other.loc
        return Kernel(
            self.name + other.name,
            monolith,
            self.size + other.size,
            loc
        )
    
    def get_arch(self):
        if self.monolithic == None:
            return 'Hybrid'
        elif self.monolithic:
            return 'Monolithic'
        else:
            return 'Microkernel'

class Unix(Kernel):
    """
    Class for Unix-like kernels, loosely based on Bell Labs' Research Unix.
    Parameters:
    - name: the name of the kernel
    - size: the size of the kernel in MB
    - loc: lines of code in the source
    """
    def __init__(self, name: str, size: float=0, loc: int=0):
        Kernel.__init__(self, name, True, size, loc)

class Minix(Unix):
    """
    Minix, by Andrew S. Taunenbaum
    """
    def __init__(self):
        self.monolithic = False
        Unix.__init__(self, 'minix', 194.72, 6000)

class Linux(Unix):
    """
    Linux Kernel, originally published in 1991 by Linus Torvalds
    Inspired by Minix.
    """
    def __init__(self):
        Unix.__init__(self, 'linux', size = 1.5, loc = 27800000)

class BSD(Unix):
    """
    Berkely Software Distribution, created at Berkely
    """
    def __init__(self, deriv: str = '', size = 25, loc = -1):
        Unix.__init__(self, f'{deriv}bsd', size, loc)

class FreeBSD(BSD):
    """
    FreeBSD Project
    """
    def __init__(self):
        BSD.__init__(self, 'free')

class XNU(BSD):
    """
    XNU Kernel, by Apple Inc. --- "X is Not Unix"
    """
    def __init__(self, name = 'xnu'):
        Unix.__init__(self, name, size = 111.14, loc = 2235726)

class NT(Kernel):
    """
    NT Kernel, by Microsoft
    """
    def __init__(self):
        Kernel.__init__(self, 'nt', None, 25, loc = -1)

