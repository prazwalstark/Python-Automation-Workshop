#! python

import sys, pyperclip


passwords ={
'email' : '077bct055.prajjwal@pcampus.edu.np',
}


account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])

                                        
