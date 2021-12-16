import typing as t
import sys
from benchmark import benchmark
import math

class RawPacket:
    def __init__(self, data: str):
        self.pt = 0        
        self.data = str(bin(int(data, 16)))[2:].zfill(len(data) * 4)  
        print(self.data)      

    def read(self, n: int) -> int:        
        ret = self.data[self.pt: self.pt+n]        
        self.pt += n
        return int(ret, 2)

    def parse(self) -> 'Packet':                
        header = self.read(3), self.read(3)               
        if header[1] == 4:                     
            return Packet(*header, self)
        else:            
            return OpPacket(*header, self)


class Packet(object):
    version: int
    type: int
    len_type: int
    _value: int = 0

    def __init__(self, version:int, type_:int, packet: RawPacket):                    
        self.version = version
        self.type = type_
        self.len_type = -1
        self._read_packet(packet)
        
    def _read_packet(self, packet):                    
        flag = 1
        while flag:                                
            flag = packet.read(1)
            self.value = self.value << 4 | packet.read(4)        
        
    def sum_it(self) -> int:
        return self.version
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
    
    def __repr__(self):
        return f"{self.__class__} {self.version=}, {self.len_type}, {self.type=}, {self.value=}"
    

class OpPacket(Packet):
    sub_packets: t.List[Packet] = None
   
    @property
    def value(self):                
        return [
            # py3.8 so no match yet but i think match would be over kill anyway
            # so i didn't pick the best one but the one that looks most interesting atm
            lambda v: sum(v),
            lambda v: math.prod(v),
            lambda v: min(v),
            lambda v: max(v),
            lambda v: 0,
            lambda v: int(v[0] > v[1]),
            lambda v: int(v[0] < v[1]),
            lambda v: int(v[0] == v[1])
        ][self.type]([it.value for it in self.sub_packets])     

    def sum_it(self):
        return self.version + sum([it.sum_it() for it in self.sub_packets])

    def _read_packet(self, packet):                
        self.sub_packets = self.sub_packets or []        
        if len_type := packet.read(1): # len type              
            self.sub_packets.extend(packet.parse() for _ in range(packet.read(11)))
        else:                                        
            length = packet.read(15)          
            pt_now = packet.pt            
            while packet.pt - pt_now < length:                           
                self.sub_packets.append(packet.parse())                   
        self.len_type = len_type

    def __repr__(self):
        return (
          super().__repr__() + "\n" + "\n".join([s.__repr__() for s in self.sub_packets])  
        ) 


def main(data: str) -> int:  
    packet = RawPacket(data).parse()
    from devtools import debug
    debug(vars(packet))
   
    return packet.value

if __name__ == "__main__":
    if '--test' in sys.argv:
        data = "620080001611562C8802118E34"
    else:
        with open('data16a.txt') as f:
            data = f.read()
    
    with benchmark():
        print(main(data))
