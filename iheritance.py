class Metal:

    def __init__(self,vocal,year):
        self.vocal=vocal
        self.year=year

    def display(self):
        print("vocalist is ::::::",self.vocal)
        print("Band was formed in:",self.year)

class Metaltypes(Metal):
    def __init__(self,guitar,Metal):
        self.guitar=guitar
        self.vocal=Metal.vocal
        self.year=Metal.year

    def details(self):
        print(self.guitar)
        print("vocalist ::",self.vocal)
        print("Band was formed in::",self.year)

class Metalband(Metaltypes):
    def __init__(self,types,Metaltypes):
        self.types=types
        self.guitar=Metaltypes.guitar
        self.year=Metaltypes.year
        self.vocal=Metaltypes.vocal
        


    def details(self):
        print("presents different genre of Metal",self.types)
        print("vocalist ::",self.vocal)
        print("Band was formed din ::",self.year)
s1=Metal('bruce dikinson',1990)
s2=Metaltypes('electric',s1)
s3=Metalband('black',s2)
s3.display()
s3.details()


