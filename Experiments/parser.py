import wikipediaapi
import time

wiki_wiki = wikipediaapi.Wikipedia('en')


def users():
    query = input(" Article name : ")
    user_list = list()
    page = wiki_wiki.page(f"Talk:{query}/Archive_1")
    num = 1
    while(page.exists()):
        user_in_page = list()
        for key in page.links.keys():
            if('user' in key.lower() and 'user talk' not in key.lower()):
                temp = key
                user_in_page.append(temp[5:])
        user_list.append(user_in_page)

        print(f"appended users for archive {num}")

        num += 1
        page = wiki_wiki.page(f"Talk:{query}/Archive_{num}")
    page = wiki_wiki.page(f"Talk:{query}")
    if(page.exists()):
        user_main_page = list()
        for key in page.links.keys():

            if('user' in key.lower() and 'user talk' not in key.lower()):
                temp = key
                user_main_page.append(temp[5:])
        user_list.append(user_main_page)
        print(f"appended users for current talk")

    print(user_list)


def save_data():
    query = input()
    page = wiki_wiki.page(f"Talk:{query}/Archive_1")
    num = 1
    # Get total no. of archives in the given article's talk page ###
    archives = len(page.backlinks)-1

    while(page.exists()):
        # Writing archives in the txt file
        for i in page.sections:
            with open(f"{query}_archive.txt", 'a', encoding='utf-8') as f:
                f.write(str(i))

                f.write('\n'*2)
                f.write('#'*40)
                f.write('\n'*2)
                f.close()
        print(f"saved archived : {num} of {archives}")
        num += 1
        page = wiki_wiki.page(f"Talk:{query}/Archive_{num}")

    # For writing the current talk page
    page = wiki_wiki.page(f"Talk:{query}")
    if(page.exists()):
        for k in page.sections:

            with open(f"{query}_archive.txt", 'a', encoding='utf-8') as f:
                f.write(str(k))

                f.close()
        print("written current talk")


def get_date_index():
    query = input(" Article Name: ")
    page = wiki_wiki.page(f"Talk:{query}/Archive_1")
    arr = list()
    for i in page.sections:
        temp = list()
        string = str(i)
        for t in range(len(string)-4):
            if(string[t:t+5] == "(UTC)"):
                temp.append(t)
        arr.append(temp)

    return arr, page


def get_date_time():
    arr, page = get_date_index()
    date_in_sections = list()
    for i in range(len(page.sections)):
        temp = list()
        string = str(page.sections[i])
        for j in arr[i]:
            if ':' in string[j-26:j]:
                mini_str = string[j-26:j+5]
                ind = mini_str[::-1].index(':')
                ind = len(mini_str) - ind - 1

                temp.append(mini_str[ind-3:j+5])
        date_in_sections.append(temp)

    return arr, date_in_sections


def get_section_name():
    comments = list()
    query = input("Article Name: ")
    page = wiki_wiki.page(f"Talk:{query}/Archive_1")
    arr, date_in_sections = get_date_time()
    # users = users()
    section_names = list()
    for x, i in enumerate(page.sections):
        section = str(i)
        last_indexes = arr[x]
        ind = section.index('\n')
        section_names.append(section[9:ind-4])
        dates = date_in_sections[x]
        start_index = ind+1
        for y, k in enumerate(dates):

            comment = section[start_index:last_indexes[y]]
            start_index = last_indexes[y]+1



# users()
save_data()
