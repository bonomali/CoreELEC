from fcntl import ioctl
 
fd = open('/dev/tty0', 'wb'); \
ioctl(fd, 0x4B3A, 0); \
fd.close

fd = open('/dev/tty1', 'wb'); \
ioctl(fd, 0x4B3A, 0); \
fd.close

fd = open('/dev/ttyS0', 'wb'); \
ioctl(fd, 0x4B3A, 0); \
fd.close
