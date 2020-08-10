import memoryTools as memTs
from sys import byteorder
from struct import pack, unpack
import win32ui
import win32process
from ctypes import wintypes, windll, c_char_p, c_ulong, byref,c_ubyte,create_string_buffer,c_size_t, c_byte


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

    address = 0x39C9694C
    buffer_size = 4
    buffer = (c_byte * buffer_size)()
    bytes_read = (c_byte * (buffer_size // 256 + 1))()

    isRead = ReadProcessMemory(processHandle, address, byref(buffer), buffer_size, byref(bytes_read))
    # value = int.from_bytes(buffer.value, byteorder=byteorder)
    value = b''.join(pack('b', buffer[i]) for i in range(buffer_size))

    value2 = a.read_integer(processHandle, address)
    windll.kernel32.CloseHandle(processHandle)
    print('Memory Value =', bytes_read[::], buffer[::], unpack('b', value[0:1]))
    print(value2)