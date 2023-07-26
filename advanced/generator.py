
# Generator's aim is to generate iterator and save the computer's memory. 
# Besides, generator is equal to iterator


def my_range(n):
    i = 0
    while i < n:
        print(f'The program will run {i}')
        yield i # generator ues yield to generate what value you want to
         i += 1

for num in my_range(5):
    print(num)


x = [0, 1, 2, 3, 4, 5]
it = (n*n for n in x)

print([n*n for n in x]) # List comprehension use []
print((n*n for n in x)) # Generator expression use ()

