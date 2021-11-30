from Falcom.Common import *
import struct

def int_to_bytes(i, size) -> bytes:
    return int.to_bytes(i, size, GlobalConfig.DefaultEndian)

def str_to_bytes(s: str) -> bytes:
    return s.encode(GlobalConfig.DefaultEncoding) + b'\x00'

def float_to_bytes(i) -> bytes:
    return struct.pack(GlobalConfig.StructEndian + 'f', i)

def double_to_bytes(i) -> bytes:
    return struct.pack(GlobalConfig.StructEndian + 'd', i)

def pad_string(s: str, padding: int) -> bytes:
    return s.encode(GlobalConfig.DefaultEncoding).ljust(padding, b'\x00')

def read_fixed_string(fs: fileio.FileStream, size: int) -> str:
    return fs.Read(size).split(b'\x00', maxsplit = 1)[0].decode(GlobalConfig.DefaultEncoding)
