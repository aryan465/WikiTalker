import wikipediaapi
import time
import json
wiki_wiki = wikipediaapi.Wikipedia('en')


def main():
    query = input("Article Name : ")
    page = wiki_wiki.page(f"Talk:{query}/Archive_1")
    num = 1
    comments = dict()
    comments['data'] = list()
    while(page.exists()):
        user_in_page = list()
        for key in page.links.keys():
            if('user' in key.lower()):
                if('user talk' not in key.lower()):
                    temp = key
                    user_in_page.append(temp[5:])
                else:
                    temp = key
                    user_in_page.append(temp[10:])

        for x in page.sections:
            section = str(x)

            ind = section.index('\n')
            section_name = section[9:ind-4]
            start_index = ind+1
            for t in range(len(section)-4):
                if(section[t:t+5] == "(UTC)"):
                    if ':' in section[t-26:t]:
                        mini_str = section[t-26:t+5]
                        date = mini_str[::-1].index(':')
                        date = len(mini_str) - date - 1
                        final_date = mini_str[date-3:t+5]
                        comment = section[start_index:t+5]
                        user = str()
                        for k in user_in_page:
                            if k in comment:
                                user = k
                                break
                        split_arr = comment.split('\n')
                        comment = " ".join(split_arr)
                        comment = comment[:comment.index(user)]
                        # if user != "":

                        dic = {
                            'user': user,
                            'comment': comment,
                            'parent_section': section_name,
                            'date_time': final_date,

                        }
                        comments['data'].append(dic)
                        start_index = t+5
        print(f"Saved data for archive {num}")
        num += 1
        page = wiki_wiki.page(f"Talk:{query}/Archive_{num}")

    page = wiki_wiki.page(f"Talk:{query}")
    if page.exists():
        user_in_page = list()
        for key in page.links.keys():
            if('user' in key.lower()):
                if('user talk' not in key.lower()):
                    temp = key
                    user_in_page.append(temp[5:])
                else:
                    temp = key
                    user_in_page.append(temp[10:])

        for x in page.sections:
            section = str(x)

            ind = section.index('\n')
            section_name = section[9:ind-4]
            start_index = ind+1
            for t in range(len(section)-4):
                if(section[t:t+5] == "(UTC)"):
                    if ':' in section[t-26:t]:
                        mini_str = section[t-26:t+5]
                        date = mini_str[::-1].index(':')
                        date = len(mini_str) - date - 1
                        final_date = mini_str[date-3:t+5]
                        comment = section[start_index:t+5]
                        user = str()
                        for k in user_in_page:
                            if k in comment:

                                user = k
                                break
                        split_arr = comment.split('\n')
                        comment = " ".join(split_arr)
                        comment = comment[:comment.index(user)]
                        # if user != "":

                        dic = {
                            'user': user,
                            'comment': comment,
                            'parent_section': section_name,
                            'date_time': final_date,
                        }

                        comments['data'].append(dic)

                        start_index = t+5
    print(f"saved data for the current talk page")
    json_data = json.dumps(comments, indent=4)
    with open(f'{query}.json', 'w') as f:
        f.write(json_data)
        f.close()


start = time.time()
main()

stop = time.time()

print("Exexcution Time:", stop-start)

