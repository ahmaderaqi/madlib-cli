import re
# the newest solution
def terminal():
    # opening the file and show its content
    print("Insert what you should insert below")
    file_1=open("assest/make_me_a_video_game_template.txt")
    txt=file_1.read()

    content_tuple=() 
    user_input=() 

    # print(x)

    if "{" in txt and "}" in txt:
        content = re.findall(r'{(.*?)}', txt)
        txt = re.sub(r'{.*?}', "{}", txt)


    for i in content:
        inputt=input(f"please insert a {i}: ")
        y=list(user_input)
        y.append(inputt)
        user_input=tuple(y)
    # print(txt)
    # print(user_input)
    counter=0
    txt = txt.split(" ")      

    for i in range(len(txt)):
        if "{" in txt[i] and "}" in txt[i]:
            txt[i] = user_input[counter]
            counter+=1

    # print(txt)
    string = ' '.join(txt)
    file = open('filename.txt', 'w')
    file.write(string)
    file.close()

    return string
result=terminal()
print(result)


def open_file():
    file_1 = open("assest/small_file.txt")
    txt = file_1.read()
    return txt










# def command():
#     # these two tuples to store data
#     content_tuple=()
#     user_input=()

#     # welcoming message
#     print("Insert what you should insert below")

#     # opening the file and show its content
#     file_1=open("assest/small_file.txt")
#     content=file_1.read()
#     # converting the string in the file into an array
#     x = content.split(" ")
#     # print(x)

#     # store the words inside the curly brackets inside the tuple content_tuple
#     for i in x:
#         if "{" in i and "}" in i:
#             content = re.findall(r'{(.*?)}', i)
#             y=list(content_tuple)
#             y.append(content)
#             content_tuple=tuple(y)

#     # store the values that the user inserted inside a tuple user_input
#     # print(content_tuple)
#     for i in content_tuple:
#         inputt=input(f"please insert a {i}: ")
#         y=list(user_input)
#         y.append(inputt)
#         user_input=tuple(y)
#     # print("user_input",user_input)

#     # convert the new array to a string
#     counter=0
#     for i in range(len(x)):
#         if "{" in x[i] and "}" in x[i]:
#             x[i] = user_input[counter]
#             counter+=1

#     string = ' '.join(x)
#     return string

# result=command()
# print(result)

# # a function to store elements inside culry brackets in a list, and replace them with an empty
# def extract_element(txt):
#     if "{" in txt and "}" in txt:
#         content = re.findall(r'{(.*?)}', txt)
#         txt = re.sub(r'{.*?}', "{}", txt)


# the new solution
# import re
# def open_file():
#     file_1 = open("assest/file_read.txt")
#     txt = file_1.read()
#     return txt

# def store_curly_brackets(txt):
#     if "{" in txt and "}" in txt:
#         content = re.findall(r'{(.*?)}', txt)
#         txt = re.sub(r'{.*?}', "{}", txt)
#         for i in content:
#             inputt = input(f"please insert a {i}: ")
#             y = list(user_input)
#             y.append(inputt)
#             user_input = tuple(y)
#     return txt,user_input


# def terminal():
    
#     # opening the file and show its content

#     # file_1 = open("assest/file_read.txt")
#     # txt = file_1.read()
#     txt=open_file()

#     content_tuple = ()
#     user_input = ()

#     # print(x)


#     # if "{" in txt and "}" in txt:
#     #     content = re.findall(r'{(.*?)}', txt)
#     #     txt = re.sub(r'{.*?}', "{}", txt)
    


#     # for i in content:
#     #     inputt = input(f"please insert a {i}: ")
#     #     y = list(user_input)
#     #     y.append(inputt)
#     #     user_input = tuple(y)

#     # print(txt)
#     # print(user_input)

#     txt,user_input=store_curly_brackets(txt)
#     counter = 0
#     txt = txt.split(" ")

#     for i in range(len(txt)):
#         if "{" in txt[i] and "}" in txt[i]:
#             txt[i] = user_input[counter]
#             counter += 1

#     # print(txt)
#     string = ' '.join(txt)
#     return string
# result=terminal()
# print(result)


