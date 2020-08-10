import memoryTools as memTs
from sys import byteorder

import win32ui
import win32process
from ctypes import wintypes, windll, c_char_p, c_ulong, byref,c_ubyte,create_string_buffer,c_size_t


if __name__ == '__main__':
    a = memTs.MemoryTools()
    print(a.__doc__)

    ### Initializing functions and permissions ###
    OpenProcess = windll.kernel32.OpenProcess
    ReadProcessMemory = windll.kernel32.ReadProcessMemory  # Method 1

    PROCESS_ALL_ACCESS = 0x1F0FFF
    PROCESS_QUERY_INFORMATION = 0x0400
    PROCESS_VM_OPERATION = 0x0008
    PROCESS_VM_READ = 0x0010
    PROCESS_VM_WRITE = 0x0020
    ### End of Initializing session

    ### Getting process handle ###
    HWND = win32ui.FindWindow(None, 'ShellShock Live').GetSafeHwnd()
    PID = win32process.GetWindowThreadProcessId(HWND)[1]
    processHandle = OpenProcess(PROCESS_ALL_ACCESS, False, PID)  # Why is it zero
    ### End of Getting process handle ###
    print('HWND is', HWND, '\nPID is', PID, '\nprocessHandle is', processHandle, '\n')
    ### Reading value of a Memory Address ###

    ADDRESS = 0x39C9694C
    buffer = c_char_p(b"data")
    buffer_size = len(buffer.value)
    bytes_read = c_ulong(0)
    bytes_written = c_ulong(0)

    isRead = ReadProcessMemory(processHandle, ADDRESS, buffer, buffer_size, byref(bytes_read))
    value = int.from_bytes(buffer.value, byteorder=byteorder)
    windll.kernel32.CloseHandle(processHandle)
    print('Memory Value =', value, buffer.value)