#!/usr/bin/env python

import struct

pkt = "\xd4\x06\x00\x00\x03\x10\x3c\x00\x07\x00\x00\x00\x9c\xff\x66\xfd\x00\x04\xe7\xfb\xa0\x41\xe7\xfb\xa0\x41\xe7\xfb\xa0\x41\x00\x00\x70\x42\x00\x00\x70\x42\x07\x00\x00\x00\x2e\xf8\x73\xec\x00\x10\x7d\x1f\x48\x43\x52\x58\x48\x43\x91\xad\x48\x43\x00\x00\xfa\x43\x00\x00\x16\x44\x7d\x4d"

# Packet from the virtual FCU: 
pkt = "\xb1\x00\x00\x00\x03\x10\x3c\x00\x04\x00\x00\x00\x41\x01\xb0\x01\x1f\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x41\x01\xb0\x01\x1f\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf5\x46"


su_fields = [('Sequence', 10), ('Packet Type', 6), ('Length', 6)]
su_header = struct.unpack("<LHH", pkt[0:8])

for i, h in enumerate(su_header): 
    print "{}: {:#08x}".format(su_fields[i][0], h)
