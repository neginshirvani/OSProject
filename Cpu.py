
from Process import Process

import random
import time
import numpy

mainmemory = [0 for i in range(8000)]
# TLB = [[0 for x in range(4)] for y in range(3)]
TLB = [[11, 12, 5],
       [15, 6 ,10],
       [10, 8, 12],
       [12 ,15 ,8]]

class Cpu:


    # RoundRobin algorithm
    def cpuScheduling(self, n, burstTime, quantom):
        while (1):

            ispending = True

            for i in range(n):

                if (burstTime[i] > 0) :
                    ispending =False

                    if (burstTime[i] > quantom):
                        burstTime[i] -= quantom
                        print(burstTime[i])

                    else:
                        burstTime[i] = 0

            if (ispending == True):
                break

    # random address is created by the cpu every 1 second
    def create_address(self):

        time.sleep(1)
        address = random.randint(0, 2047)

        print(address)
        return address

    ''' addresi k tolid mishe az 0 ta 2047 hast hala farze man in hast k
        msln addrese tolid shode 1023 bashe ma injoori dar nazaresh begirim k
        0001 0000 0010 0011 hala 11taro vase offset mizarim kenare mimoone
        00010 hala mirim moadele ino dakhele TLB nega mikonim va b onvane 
        frame number qararesh midim farz mikonim k pagenumber[2] = 3 msln 
        pas hala bayad berim b addres 0001 1000 0010 0011 k tebqe qarardadi k kardam 
        ba khodam mimshe 1823 addressi k byd morajee konim besh '''

    def translate_address(self):

        res = 0
        address = self.create_address()
        digits = [int(d) for d in str(address)]
        # print("hi")
        print(digits)

        #We have only 4 rows in the TLB so
        if digits[0] > 4:
            print("need too access disk")
            return address
        else:
            digits[0] = TLB[digits[0]][1]

        for i in range(len(digits)):
            res += digits[i] * (10 ** ((len(digits) - 1) - i))

        address = res

        print(address)
        return address

    def access_memory(self):

        pf = 0
        address = self.translate_address()

        # 10ms delay to access memory
        time.sleep(0.01)
        if mainmemory[address] == 1:
            print("page hit")

        else:
            pf += 1
            print("pf occurred, wait...")

            # we should now access disk and bring the address

            time.sleep(1)
            mainmemory[int(address)] = 1
            self.access_memory()

    def process_being_run(self):
        # p = Process()
        # self.cpuScheduling(5, p.burstTime, 4)
        p1 = Process(3, 5, 1, 8)
        p2 = Process(3, 4, 1, 13)
        p3 = Process(3, 6, 1, 15)
        p4 = Process(3, 5, 1, 12)
        p5 = Process(1, 4, 1, 4)

        burstTime = [p1.burstTime, p2.burstTime, p3.burstTime, p4.burstTime, p5.burstTime]
        self.cpuScheduling(5, burstTime, 4)


if __name__ == "__main__":
    c = Cpu()

    c.process_being_run()

    # q = 2


    # c.cpuScheduling(n, burstTime, q)
    # print(c.create_address())
    # c.access_memory()
    # n = 1023
    # lst = [int(d) for d in str(n)]
    # lst[0] = burstTime[1]
    # print(len(lst))
    # print(lst)
    # res = 0
    # for i in range(len(lst)):
    #     res += lst[i] * (10 ** ((len(lst) - 1) - i))
    # print(res)
    # c.access_memory()
    # c.create_address()
