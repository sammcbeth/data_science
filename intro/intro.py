d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

print(d['k1'][3])

def domainGet(email):
    return email.split('@')[1]

print(domainGet("user@domain.com"))

def findDog(s):
    return 'dog' in s.lower().split()

print(findDog('is there a dog in here'))


def countDog(s):
    count = 0
    for word in s.lower().split():
        if word == 'dog':
            count += 1
    return count

print(countDog('this is a dog this is another dog one other dog'))



seq = ['soup','dog','salad','cat','great']

print(list(filter(lambda word: word[0] == 's', seq)))

def is_it_a_ticket(speed, birthday):
    big_speed = 81
    mid_speed = 61

    if birthday:
        big_speed += 5
        mid_speed += 5

    if speed < mid_speed:
        print('No Ticket')
    elif speed > big_speed:
        print('Big ticket')
    else:
        print('Medium ticket')


is_it_a_ticket(55,False)
is_it_a_ticket(102,False)
is_it_a_ticket(69,True)
is_it_a_ticket(81,True)