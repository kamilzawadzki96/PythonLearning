class Queue:
    def __init__(self):
        print("I am initiated!!!")
        self._login="JohnDoe"
        self.__password="P@ssw0rd!!!"


queue = Queue()
print(queue._login)
print(queue._Queue__password)