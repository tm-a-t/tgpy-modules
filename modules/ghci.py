import os
import subprocess
import functools

hs_in = None
hs_out = None
hs_proc = None


def ghci_init():
    global hs_proc, hs_in, hs_out
    with open('.ghci', 'w') as cfg:
        cfg.write(':set prompt "' + chr(23) + '"
                                              ')
        # cfg.write(':set +m
                                              ')
        hs_proc = subprocess.Popen(['ghci'], encoding='utf-8', stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT, env={**os.environ,
                                                                  'PATH': '/run/wrappers/bin:/home/tgpy/.nix-profile/bin:/etc/profiles/per-user/tgpy/bin:/nix/var/nix/profiles/default/bin:/run/current-system/sw/bin'})
        hs_in = hs_proc.stdin
        hs_out = hs_proc.stdout
        hs_out.readline()
        hs_out.readline()
        hs_out.read(1)


def ghci_cmd(cmd):
    global hs_proc, hs_in, hs_out
    hs_in.write(cmd + '
                      ')
    hs_in.flush()
    return ''.join(iter(functools.partial(hs_out.read, 1), chr(23)))


def ghci_restart():
    global hs_proc, hs_in, hs_out
    hs_proc.terminate()
    ghci_init()


def hs_trans(cmd):
    if cmd.lower().startswith('.hs ') or cmd.lower().startswith('.hs
                                                                '):
        return f"ghci_cmd({repr(cmd[4:])})"
    return cmd


tgpy.add_code_transformer('ghci_cmd', hs_trans)
ghci_init()
