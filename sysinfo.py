#!/usr/bin/env python3
import platform


def humanbytes(B):
   'Return the given bytes as a human friendly KB, MB, GB, or TB string'
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776

   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.2f} TB'.format(B/TB)


################################################################################################################


print("Architecture: " + platform.architecture()[0])
print("Machine: " + platform.machine())
print("Node: " + platform.node())
print("System: " + platform.system())

dist = platform.dist()
dist = " ".join(x for x in dist)
print("Distribution: " + dist)

# CPU info
print("Processors: ")
with open("/proc/cpuinfo", "r") as f:
    info = f.readlines()

cpuinfo = [x.strip().split(":")[1] for x in info if "model name" in x]
for index, item in enumerate(cpuinfo):
    print("     " + str(index) + ": " + item)

# Memory info
print("Memory Info: ")
with open("/proc/meminfo", "r") as f:
    lines = f.readlines()

print("     " + lines[0].strip().format(humanbytes))
print("     " + lines[1].strip().format(humanbytes))

# Uptime
uptime = None
with open("/proc/uptime", "r") as f:
    uptime = f.read().split(" ")[0].strip()
uptime = int(float(uptime))
uptime_hours = uptime // 3600
uptime_minutes = (uptime % 3600) // 60
print("Uptime: " + str(uptime_hours) + " hours, " + str(uptime_minutes) + " minutes")

# Load
with open("/proc/loadavg", "r") as f:
    print("Average load: " + f.read().strip())