import game
# from struct import pack, unpack
import memory_tools as mp
import win32process
import win32ui
import win32api
import win32security
from ctypes import windll
import test
import time

# def se_debug():
#     try:
#         """SEDebug"""
#         flags = win32security.TOKEN_ALL_ACCESS
#         h_token = win32security.OpenProcessToken(win32api.GetCurrentProcess(), flags)
#
#         id = win32security.LookupPrivilegeValue(None, "seDebugPrivilege")
#
#         newPrivileges = [(id, win32security.SE_PRIVILEGE_ENABLED)]
#         # is_enable = win32security.CreateRestrictedToken(h_token, (), 0, 0, 0)
#
#         token_r = win32security.CreateRestrictedToken(h_token, 0, None, None, None)
#         is_enable = win32security.AdjustTokenPrivileges(token_r, 0, newPrivileges)
#         print(h_token, id, newPrivileges)
#         print('is enabled', token_r)
#     except Exception as e:
#         print(e)


if __name__ == '__main__':
    # shell_shock_live = game.Game('ShellShock Live')
    # shell_shock_live.enable()
    hwnd = win32ui.FindWindow(None, 'ShellShock Live').GetSafeHwnd()
    tid, pid = win32process.GetWindowThreadProcessId(hwnd)
    a = mp.MemoryTools()
    # print(tid, pid)

    PROCESS_ALL_ACCESS = 0x1F0FFF
    PROCESS_QUERY_INFORMATION = 0x0400
    PROCESS_VM_OPERATION = 0x0008
    PROCESS_VM_READ = 0x0010
    PROCESS_VM_WRITE = 0x0020
    # address = 0x305D9B4D
    """SEDebug"""
    # test.disable_privilege('SeDebugPrivilege')

    OpenProcess = windll.kernel32.OpenProcess
    processHandle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    print(processHandle)
    old_number = 0x0
    with open('3.txt', 'w') as f:
        hex_old_number = hex(old_number)[:2]+'0'*(8-len(hex(old_number))+2)+hex(old_number)[2:]
        print(hex_old_number, end=':')
        f.write(hex_old_number + ':')
        for i in range(1, 0x3fffffff):
            if a.read_byte(processHandle, i) is None:
                if not (old_number == i - 1):
                    number = hex(i)[:2]+'0'*(8-len(hex(i))+2)+hex(i)[2:]
                    print(number, end=':')
                    f.write(number+':')
                old_number = i
            else:
                if old_number == i - 1:
                    print(hex(i)[:2]+'0'*(8-len(hex(i))+2)+hex(i)[2:])
                    f.write(hex(i)[:2]+'0'*(8-len(hex(i))+2)+hex(i)[2:] + '\n')
    # signature = '89 47 1C 8B 47 20 89 45 F8'
    # # value = a.read_integer(processHandle, address)
    # t1 = time.process_time()
    # address = a.scan_signature(processHandle, 0x0, 0x7fffffffffff, signature)
    # t2 = time.process_time()
    # print('time = ', t2-t1)
    # print('Address is', None if address is None else hex(address))

    windll.kernel32.CloseHandle(processHandle)


