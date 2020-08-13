import game
# from struct import pack, unpack
import memory_tools as mp
import win32process
import win32ui
from ctypes import windll


if __name__ == '__main__':
    # shell_shock_live = game.Game('ShellShock Live')
    # shell_shock_live.enable()
    hwnd = win32ui.FindWindow(None, 'The Trail: Frontier Challenge').GetSafeHwnd()
    tid, pid = win32process.GetWindowThreadProcessId(hwnd)
    a = mp.MemoryTools()
    print(tid, pid)

    PROCESS_ALL_ACCESS = 0x1F0FFF
    address = 0x1EAB0AD0
    OpenProcess = windll.kernel32.OpenProcess
    processHandle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    print(processHandle)
    value = a.read_float(processHandle, address)
    print(value)
    print(a.write_float(processHandle, address, 4.5))
    windll.kernel32.CloseHandle(processHandle)

