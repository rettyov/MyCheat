# LPVOID ScanSignature(HANDLE hProcess, ULONG_PTR startAddress, SIZE_T scanSize, PBYTE pattern, std::wstring& mask);
# bool CheckSignature(PBYTE source, PBYTE pattern, std::wstring& mask);
# void ShowErrorMessage(HWND hwnd, LPCWSTR errorMessage);

# readBytes
# readSmallInteger
# readInteger
# readQword
# readPointer
# readFloat
# readDouble
# readString
# writeBytes
# writeSmallInteger
# writeInteger
# writeQword
# writeFloat
# writeDouble
# writeString


from ctypes import windll, c_ulong, byref, c_ubyte


class MemoryTools:
    """
    This class provides all the functions with RAM
    """

    ReadProcessMemory = windll.kernel32.ReadProcessMemory
    WriteProcessMemory = windll.kernel32.WriteProcessMemory

    __bufferSize = 4
    __buffer = (c_ubyte * __bufferSize)()
    __bytesRead = c_ubyte()

    def __init__(self):
        pass

    def __read_bytes(self, process_handle: int, address: int):
        """
        Read bytes from RAM\n
        :param process_handle: int.
            A handle to the process with memory that is being read.
        :param address: int.
            A base address in the specified process from which to read. Before any data transfer occurs, the system
            verifies that all data in the base address and memory of the specified size is accessible for read access,
            and if it is not accessible the function return None.
        :return: Sequence[int] or None.
            List with bytes or None.
            If the function succeeds, the return value is not None.
            The function fails if the requested read operation crosses into an area of the process that is inaccessible.
        """
        self.__buffer = (c_ubyte * self.__bufferSize)()
        self.__bytesRead = (c_ubyte * (self.__bufferSize // 256 + 1))()
        is_read = self.ReadProcessMemory(process_handle, address, byref(self.__buffer),
                                         self.__bufferSize, byref(self.__bytesRead))
        if not is_read:
            return None
        return self.__buffer[::]

    def read_integer(self, process_handle: int, address: int):
        """
        Read Integer from RAM\n
        :param process_handle:
            A handle to the process with memory that is being read.
        :param address:
            A base address in the specified process from which to read.
        :return: int or None.
        """
        self.__bufferSize = 4
        value = self.__read_bytes(process_handle, address)
        return None if value is None else int.from_bytes(value, byteorder='little')

    def write_integer(self, proc_h, adr, value):
        """
        Write Integer to RAM
        :param proc_h: processHandle
        :param adr: address
        :param value: value must be integer
        :return: True or False
        """
        if type(value) is not int:
            return False
        value_size = 4
        value = c_ulong(value)
        bytes_written = c_ubyte()

        is_write = self.WriteProcessMemory(proc_h, adr, byref(value), value_size, byref(bytes_written))
        if not is_write:
            return False
        return True
