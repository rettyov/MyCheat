'''
int GetProcessIdByWindowName(LPCWSTR className, LPCWSTR windowName);
int GetProcessIdByProcessName(LPCWSTR processName);
int WriteMem(HANDLE hProcess, LPVOID address, LPVOID source, SIZE_T writeAmount);
LPVOID ReadMem(HANDLE hProcess, LPVOID address, SIZE_T readAmount);
LPVOID AllocMem(HANDLE hProcess, LPVOID startAddress, SIZE_T allocationAmount);
int FreeMem(HANDLE hProcess, LPVOID address, SIZE_T amount);
LPVOID ScanSignature(HANDLE hProcess, ULONG_PTR startAddress, SIZE_T scanSize, PBYTE pattern, std::wstring& mask);
bool CheckSignature(PBYTE source, PBYTE pattern, std::wstring& mask);
void ShowErrorMessage(HWND hwnd, LPCWSTR errorMessage);
bool isTargetx64Process(HANDLE hProcess);
DWORD_PTR GetProcessBaseAddress(HANDLE hProcess);
DWORD_PTR GetModuleBaseAddress(HANDLE hProcess, LPCWSTR lpszModuleName);
'''
class MemoryTools:
    '''This class provides all the functions with RAM'''
    def __init__(self):
        pass