#cython: language_level=3
#distutils: language = c

from typing import Any

cdef class TestClass:
    def __cinit__(self, data: Any) -> None:
        pass
