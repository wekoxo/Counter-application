# Uncomment, if want to count all actual dll and run in 32-bit Python on 64-bit Windows
#import ctypes
#class disable_file_system_redirection:
#    _disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
#    _revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
#    def __enter__(self):
#        self.old_value = ctypes.c_long()
#        self.success = self._disable(ctypes.byref(self.old_value))
#    def __exit__(self, type, value, traceback):
#        if self.success:
#            self._revert(self.old_value)
#
#
#disable_file_system_redirection().__enter__()


import os, ctypes, sys


def count_dll(path):
    res = []
    for entry in os.scandir(path):
        if entry.is_file() and entry.name.lower().endswith('.dll'):
            res.append(entry.name)
    return res

#Check privileges
if not ctypes.windll.shell32.IsUserAnAdmin():
    sys.stderr.write('Script must be run as Administrator')
    sys.exit(1)

path = 'C:\\Windows\\System32'

res = count_dll(path)
#Count in every 'a*' directory
for entry in os.scandir(path):
    if entry.is_dir() and entry.name.startswith('a'):
        res.extend(count_dll(entry.path))
print('Number of files: {}'.format(len(res)))
print('Files:')
#print('\n'.join(res)))
for i in res:
    print(i)
