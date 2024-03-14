# Strict typing components
from typing import Optional, Union
# Kernels

class Kernel:
    """
    Class for operating system kernels.
    Parameters:
    - name: the name of the kernel
    - monolithic: a boolean, True if the kernel is monolithic, False if it is not (a microkernel), None if it is hybrid.
    - size: size of kernel source in MB (-1 if unavailable)
    """
    def __init__(self, name: str, monolithic: Optional[bool], size: float=0):
        self.name = name
        self.monolithic = monolithic
        self.size = size

    def __repr__(self):
        return f'<{self.name} Kernel, {self.get_arch()}, {self.size} MB>'
    
    def __add__(self, other):
        if isinstance(self, Minix) and isinstance(other, Unix):
            return Linux()
        elif isinstance(self, Unix) and isinstance(other, Minix):
            return Linux()

        if self.monolithic == other.monolithic:
            monolith = self.monolithic
        else:
            monolith = None
        if self.name == other.name:
            name = self.name
        else:
            name = f'{self.name}/{other.name}'
        if self.size == -1 and other.size == -1:
            size = -1
        elif self.size == -1:
            size = other.size
        elif other.size == -1:
            size = self.size
        else:
            size = self.size + other.size
        return Kernel(
            name,
            monolith,
            size,
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
    Class for Unix-like kernels, which usualy loosely based on Bell Labs' Research Unix.
    Parameters:
    - name: the name of the kernel
    - size: the size of the kernel in MB
    """
    def __init__(self, name: str, size: float=0):
        Kernel.__init__(self, name, True, size)

class Minix(Unix):
    """
    Minix, by Andrew S. Taunenbaum
    """
    def __init__(self):
        self.monolithic = False
        Unix.__init__(self, 'Minix', 194.72)

class Linux(Unix):
    """
    Linux Kernel, originally published in 1991 by Linus Torvalds
    Inspired by Minix.
    """
    def __init__(self):
        Unix.__init__(self, 'Linux', size = 4942.469)

class BSD(Unix):
    """
    Berkely Software Distribution, created at Berkely
    """
    def __init__(self, deriv: str = '', size = 3066.468):
        Unix.__init__(self, f'{deriv}BSD', size)

class FreeBSD(BSD):
    """
    FreeBSD Project
    """
    def __init__(self):
        BSD.__init__(self, 'Free')

class XNU(BSD):
    """
    XNU Kernel, by Apple Inc. --- "X is Not Unix"
    """
    def __init__(self, name = 'XNU'):
        Unix.__init__(self, name, size = 111.14)

class NT(Kernel):
    """
    NT Kernel, by Microsoft
    """
    def __init__(self):
        Kernel.__init__(self, 'NT', None, -1)

