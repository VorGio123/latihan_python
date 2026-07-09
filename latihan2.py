age = 15

if age < 18:
    print("Anda masih di bawah umur.")
elif age == 18:
    print("Anda baru saja menjadi dewasa!")
else:
    print("Anda sudah dewasa.")
 
fruits = ["apel", "pisang", "ceri"]

for fruit in fruits:
    print(fruit)

count = 1

while count < 6:
    print(count)
    count += 1

for i in range(10):
    if i == 6:
        break
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

for i in range(5):
    pass

print("Perulangan selesai.")

def greet(name):
    return f"Halo, {name}!"

message = greet("Nandika")
print(message)

def add(a, b=10):
    return a + b

result = add(12)
print(result)

square = lambda x: x ** 3

print(square(2))

my_list = ["apel", "pisang", "jeruk", "anggur"]

print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

my_tuple = (4, 5, 6)

print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

my_set = {7, 8, 9, 7}

print(my_set)

nama_buah= {"apel", "pisang", "anggur", "jeruk", "apel"}

print(nama_buah)

person = {
    "nama": "Candra",
    "umur": 17,
    "kota": "Tasikmalaya"
}

print(person["nama"])
print(person["umur"])
print(person["kota"])

person = {
    "nama": "Nandika",
    "umur": 17,
    "kota": "Tasikmalaya"
}

print(person["nama"])
print(person["umur"])
print(person["kota"])

squares = [x**2 for x in range(11)]

print(squares)