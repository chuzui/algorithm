import threading

class Park():
    def __init__(self, unoccupiedNum):
        self.unoccupiedNum = unoccupiedNum
        self.entryAndExitList = []

class ParkBaseThread(threading.Thread):
    def __init__(self, index, park):
        self.index = index
        self.park = park
        self.timeStamp = 0
        self.isOnAction = False
        self.num = 0
        self.mutex = threading.Lock()

    def receive(self, time):
        isAcquire = False
        if self.isOnAction and self.timeStamp < time:
            self.mutex.acquire()
            isAcquire = True
        if isAcquire:
            self.mutex.release()
        self.timeStamp = max(self.timeStamp, time) + 1
        return self.num


class EntryThread(ParkBaseThread):
    def entry(self):
        self.isOnAction = True
        self.mutex.acquire()
        self.timeStamp += 1
        sum = self.num
        for i, t in enumerate(self.park.entryAndExitList):
            if i != self.index:
                sum += t.receive(self.timeStamp)
        print sum
        if sum >= self.park.unoccupiedNum:
            print 'the park is full'
        else:
            print 'enter in ' + str(self.index)
            self.num += 1

        self.mutex.release()
        self.isOnAction = False

class ExitThread(ParkBaseThread):
    def exit(self):
        self.isOnAction = True
        self.mutex.acquire()
        self.timeStamp += 1
        sum = self.num
        for i, t in enumerate(self.park.entryAndExitList):
            if i != self.index:
                sum += t.receive(self.timeStamp)
        if sum <= 0:
            print 'the park is empty'
        else:
            print 'exit in ' + str(self.index)
            self.num -= 1
        self.mutex.release()
        self.isOnAction = False


Entry = 5
Exit = 4
UNOCCUPIED_NUM = 3
park = Park(UNOCCUPIED_NUM)
for i in range(Entry):
    index = len(park.entryAndExitList)
    t = EntryThread(index, park)
    park.entryAndExitList.append(t)

for i in range(Exit):
    index = len(park.entryAndExitList)
    t = ExitThread(index, park)
    park.entryAndExitList.append(t)

l = [1,2,4,2]
for i in l:
    park.entryAndExitList[i].entry()

e = [5,6,7,5]
for i in e:
    park.entryAndExitList[i].exit()