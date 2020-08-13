# LPVOID ScanSignature(HANDLE hProcess, ULONG_PTR startAddress, SIZE_T scanSize, PBYTE pattern, std::wstring& mask);
# bool CheckSignature(PBYTE source, PBYTE pattern, std::wstring& mask);

from struct import unpack
from ctypes import windll, c_ulong, byref, c_ubyte, c_long, c_float


class MemoryTools:
    """
    This class provides all the functions with RAM
    """
    ReadProcessMemory = windll.kernel32.ReadProcessMemory
    WriteProcessMemory = windll.kernel32.WriteProcessMemory

    __bufferSize = 4
    __buffer = (c_ubyte * __bufferSize)()
    __bytesRead = c_ubyte()
    __bytes_written = c_ubyte()

    def __init__(self):
        pass

    def __read_bytes(self, process_handle: int, address: int):
        """
        Read bytes from RAM\n
        :return: Sequence[int] or None.
            List with bytes or None.
            If the function succeeds, the return value is not None.
            The function fails if the requested read operation crosses into an area of the process that is inaccessible.
        """
        self.__buffer = (c_ubyte * self.__bufferSize)()
        self.__bytesRead = (c_ubyte * (self.__bufferSize // 256 + 1))()
        is_read = self.ReadProcessMemory(process_handle, address, byref(self.__buffer),
                                         self.__bufferSize, byref(self.__bytesRead))
        return None if not is_read else self.__buffer[::]

    def __write_bytes(self, process_handle: int, address: int, value: [int, float]):
        """
        Write bytes from RAM\n
        :return: True or False.
            If the function succeeds, the return value is True in another case return value is False.
        """
        if type(value) is int:
            value = c_long(value)
        elif type(value) is float:
            value = c_float(value)
        self.__bytes_written = (c_ubyte * (self.__bufferSize // 256 + 1))()
        is_write = self.WriteProcessMemory(process_handle, address, byref(value),
                                           self.__bufferSize, byref(self.__bytes_written))
        return True if is_write else False

    def read_integer(self, process_handle: int, address: int):
        """
        Read Integer(4 bytes) from RAM\n
        :param process_handle:
            A handle to the process with memory that is being read.
        :param address:
            A base address in the specified process from which to read.
        :return: int or None.
        """
        self.__bufferSize = 4
        value = self.__read_bytes(process_handle, address)
        return None if value is None else int.from_bytes(value, byteorder='little')

    def read_long_integer(self, process_handle: int, address: int):
        """
        Read Long Integer(8 bytes) from RAM\n
        :param process_handle:
            A handle to the process with memory that is being read.
        :param address:
            A base address in the specified process from which to read.
        :return: int or None.
        """
        self.__bufferSize = 8
        value = self.__read_bytes(process_handle, address)
        return None if value is None else int.from_bytes(value, byteorder='little')

    def read_float(self, process_handle: int, address: int):
        """
        Read Float(4 bytes) from RAM\n
        :param process_handle:
            A handle to the process with memory that is being read.
        :param address:
            A base address in the specified process from which to read.
        :return: float or None.
        """
        self.__bufferSize = 4
        value = self.__read_bytes(process_handle, address)
        return None if value is None else unpack('<f', bytearray(value))

    def read_double(self, process_handle: int, address: int):
        """
        Read Double(8 bytes) from RAM\n
        :param process_handle:
            A handle to the process with memory that is being read.
        :param address:
            A base address in the specified process from which to read.
        :return: float or None.
        """
        self.__bufferSize = 8
        value = self.__read_bytes(process_handle, address)
        return None if value is None else unpack('<d', bytearray(value))

    def write_integer(self, process_handle: int, address: int, value):
        """
        Write Integer(4 bytes) to RAM
        :param process_handle:
            A handle to the process with memory that is being read.
        :param address:
            A base address in the specified process from which to read.
        :param value: value must be integer
        :return: True or False
        """
        self.__bufferSize = 4
        is_write = self.__write_bytes(process_handle, address, value)
        return True if is_write else False

    def write_long_integer(self, process_handle: int, address: int, value):
        """
        Write Long Integer to RAM
        :param process_handle:
            A handle to the process with memory that is being read.
        :param address:
            A base address in the specified process from which to read.
        :param value: value must be integer
        :return: True or False
        """
        self.__bufferSize = 8
        is_write = self.__write_bytes(process_handle, address, value)
        return True if is_write else False

    def write_float(self, process_handle: int, address: int, value):
        """
        Write Float to RAM
        :param process_handle:
            A handle to the process with memory that is being read.
        :param address:
            A base address in the specified process from which to read.
        :param value: value must be float
        :return: True or False
        """
        self.__bufferSize = 4
        is_write = self.__write_bytes(process_handle, address, value)
        return True if is_write else False

    def write_double(self, process_handle: int, address: int, value):
        """
        Write Double to RAM
        :param process_handle:
            A handle to the process with memory that is being read.
        :param address:
            A base address in the specified process from which to read.
        :param value: value must be double
        :return: True or False
        """
        self.__bufferSize = 8
        is_write = self.__write_bytes(process_handle, address, value)
        return True if is_write else False
