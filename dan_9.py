import math



# class Student:
#     def __init__ (self, indeks, ime, prezime):
#         self.indeks = indeks
#         self.ime = ime
#         self.prezime = prezime
    
#     def __str__(self):
#         return f"[{self.indeks}] {self.ime} {self.prezime}"
    
#     def prikazi (self):
#         print(self)
    
#     def predstavi_se (self):
#         print(f"Dobar dan, ja sam {self.ime}, student.")

# student1 = Student(2008213514, "Milan", "Tair")
# student1.prikazi()
# student1.predstavi_se()

# print(f"Dobar dan, {student1.ime}.")



class Tacka3D:
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__ (self):
        return f"({self.x:0.4f}, {self.y:0.4f}, {self.z:0.4f})"
    
    def udaljenost (self, druga_tacka):
        d_x = self.x - druga_tacka.x
        d_y = self.y - druga_tacka.y
        d_z = self.z - druga_tacka.z