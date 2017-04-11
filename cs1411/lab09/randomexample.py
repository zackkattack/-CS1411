import random
#random.randint(n,m) generates n <= random integer <= m
#random.random() generates 0 <= random float < 1.0
#random.randrange(n,m,s) generates n <= random integer < m with step value s
#random.uniform(n,m) generates n <= random float <= m
#random.choice(sequence) selects a random element from the sequence and returns it
#random.shuffle(sequence) shuffles the order of the sequence in place
#random.sample(sequence,num) generates a new sequence by sampling k elements from the original sequence

#demo randint
#print 5 random numbers seeded with 5
print('seed 5 randint():',end=' ')
random.seed(5)
for i in range(0,5):
    print (random.randint(1,10),end=' ')
print()
#print 5 random numbers seeded with the current time
print('seed current time randint():',end=' ')
random.seed()
for i in range(0,5):
    print (random.randint(1,10),end=' ')
print()
#print another 5 random numbers seeded with the current time
print('seed current time randint():',end=' ')
random.seed()
for i in range(0,5):
    print (random.randint(1,10),end=' ')
print()
#print 5 random numbers seeded with 5 to show the same sequence occurs
print('seed 5: randint()',end=' ')
random.seed(5)
for i in range(0,5):
    print (random.randint(1,10),end=' ')
print()

#demo random
#print 5 random numbers 
random.seed(5)
print('seed 5 random():',end=' ')
for i in range(0,5):
    print (random.random(),end=' ')
print()

#demo randrange
print('randrange(0,10,2) =',random.randrange(0,10,2))
#demo uniform
print('uniform(2.0,10.0) =',random.uniform(2.0,10.0))
#demo choice
print('choice(\'abcdefg\') =',random.choice('abcdefg'))
#demo shuffle
a = [1,2,3,4,5]
random.shuffle(a)
print('shuffle([1,2,3,4,5]) =',a)
#demo sample
print('sample([1,2,3,4,5],3) =',random.sample([1,2,3,4,5],3))

#seeding the random number generator each time a random number is generated
for i in range(0,5):
    random.seed(5)
    print(random.randint(1,10),end=' ')
print()

