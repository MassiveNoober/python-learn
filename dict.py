# sample_dict = {1: 'coffee', 2: 'Tea', 3: 'juice'}
# print(sample_dict[1])
# sample_dict[2] = 'Mint Tea'
# print(sample_dict[2])
# del sample_dict[3]

my_d = {1: 'Test', 'Name': 'Jim'}
print(type(my_d))
print(my_d['Name'])

for key, value in my_d.items():
    print(str(key) + " : " + value)