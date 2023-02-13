print(3+3)

my_list = ["chicken wing", "chicken wing", "hot dog", "bologna", "chicken", "macaroni"]
my_string = ""
for index in range(len(my_list)):
    if index == 6:
        my_string += "chillin' with my homie"
    my_string[index] = "chicken wing"
print(my_string)

