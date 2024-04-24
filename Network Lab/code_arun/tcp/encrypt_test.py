import io

class test():
    
    def __init__(self):
        self.buffer = io.BytesIO()
        
    def writing(self):
        data = input("Enter the data to be written - ")
        self.buffer.write(bytes(data.encode("utf-8")))
        
    def reading(self):
        f = open(self.buffer, "rb")
        print(f)
        
c = test()
c.writing()
c.reading()