# int GetProcessIdByWindowName(LPCWSTR className, LPCWSTR windowName);
# int GetProcessIdByProcessName(LPCWSTR processName);
# int WriteMem(HANDLE hProcess, LPVOID address, LPVOID source, SIZE_T writeAmount);
# LPVOID ReadMem(HANDLE hProcess, LPVOID address, SIZE_T readAmount);
# LPVOID AllocMem(HANDLE hProcess, LPVOID startAddress, SIZE_T allocationAmount);
# int FreeMem(HANDLE hProcess, LPVOID address, SIZE_T amount);
# LPVOID ScanSignature(HANDLE hProcess, ULONG_PTR startAddress, SIZE_T scanSize, PBYTE pattern, std::wstring& mask);
# bool CheckSignature(PBYTE source, PBYTE pattern, std::wstring& mask);
# void ShowErrorMessage(HWND hwnd, LPCWSTR errorMessage);
# bool isTargetx64Process(HANDLE hProcess);
# DWORD_PTR GetProcessBaseAddress(HANDLE hProcess);
# DWORD_PTR GetModuleBaseAddress(HANDLE hProcess, LPCWSTR lpszModuleName);


from sys import byteorder
import win32ui
import win32process
from ctypes import windll, c_char_p, c_ulong, byref, c_ubyte, create_string_buffer, c_size_t, c_ubyte


class MemoryTools:
    """
    This class provides all the functions with RAM
    """
    # Initializing functions and permissions
    OpenProcess = windll.kernel32.OpenProcess
    ReadProcessMemory = windll.kernel32.ReadProcessMemory
    WriteProcessMemory = windll.kernel32.WriteProcessMemory
    CloseHandle = windll.kernel32.CloseHandle

    PROCESS_ALL_ACCESS = 0x1F0FFF
    PROCESS_QUERY_INFORMATION = 0x0400
    PROCESS_VM_OPERATION = 0x0008
    PROCESS_VM_READ = 0x0010
    PROCESS_VM_WRITE = 0x0020

    # End of Initializing session

    def __init__(self):
        pass

    def read_integer(self, proc_h, adr):
        """
        Read Integer from RAM
        :param proc_h: processHandle
        :param adr: address
        :return: int or None
        """
        buffer_size = 4
        buffer = (c_ubyte * buffer_size)()
        bytes_read = c_ubyte()

        is_read = self.ReadProcessMemory(proc_h, adr, byref(buffer), buffer_size, byref(bytes_read))
        if not is_read:
            return None
        return int.from_bytes(buffer[::], byteorder='little')

    # def write_integer(self, proc_h, adr, value):
    #     """
    #     Read Integer from RAM
    #     :param proc_h: processHandle
    #     :param adr: address
    #     :return: int or None
    #     """
    #     buffer_size = 4
    #     buffer = (c_ubyte * buffer_size)()
    #     bytes_read = c_ubyte()
    #
    #     is_read = self.ReadProcessMemory(proc_h, adr, byref(buffer), buffer_size, byref(bytes_read))
    #     if not is_read:
    #         return None
    #     return int.from_bytes(buffer[::], byteorder='little')
