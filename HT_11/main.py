import requests
import random

def check_id(ID,param):
    url = f'https://jsonplaceholder.typicode.com/{param}'
    res = requests.get(url)
    data = res.json()
    for i in data:
        if i.get('id') == ID:
            return True
       
def get_info():
    url = 'https://jsonplaceholder.typicode.com/users'
    res = requests.get(url)
    data = res.json()
    for i in data:
        print(f'ID: {i.get("id")}')
        print(f'Name: {i.get("name")}')
        print(f'Username: {i.get("username")}')
        
def main():
    get_info()
    try:
        user_id = int(input('Enter user ID: '))
    except:
        print('You input incorrect ID')
    else:
        if check_id(user_id,'users') == True:
            while True:    
                print('\n 1 - Full information about user\n 2 - Posts\n 3 - TODOs\n 4 - Get random picture\n 5 - Exit')
                user_choice = input('Enter your choice (1,2,3,4,5): ')
                if user_choice == '1':
                    users_json(user_id)
                elif user_choice == '2':
                    print(' 1 - list of posts this user\n 2 - information about specific post')
                    user_choice_2 = input('Enter your choice (1 or 2): ')
                    if user_choice_2 == '1':
                        posts_json(user_id)
                    elif user_choice_2 == '2':
                        post_id = input('Enter post id: ')
                        if check_id(int(post_id),'posts') == True:
                            posts_full_json(int(post_id))
                        else:
                            print('Not found')
                    else:
                        print('Incorrect number')
                elif user_choice == '3':
                    print(' 1 - list of uncompleted tasks\n 2 - list of completed tasks')
                    user_choice_3 = input('Enter your choice (1 or 2): ')
                    if user_choice_3 == '1':
                        todo_json(user_id,False)
                    elif user_choice_3 == '2':
                        todo_json(user_id,True)
                    else:
                        print('Incorrect number')
                elif user_choice == '4':
                    random_picture_json()
                elif user_choice == '5':
                    print('Exit')
                    break
                else:
                    print('Incorrect number')
        else:
            print('Not found')

                
def users_json(user_id):    
    url = 'https://jsonplaceholder.typicode.com/users'
    res = requests.get(url)
    data = res.json()
    for i in data:
        if i.get('id') == user_id:
            for key in i:
                print(f'{key}: {i.get(key)}')

def posts_json(user_id):
    url = 'https://jsonplaceholder.typicode.com/posts'
    res = requests.get(url)
    data = res.json()
    for i in data:
        if i.get('userId') == user_id:
            print(f'id: {i.get("id")}')
            print(f'title: {i.get("title")}')

def posts_full_json(post_id):
    url = 'https://jsonplaceholder.typicode.com/posts'
    res = requests.get(url)
    data = res.json()
    for i in data:
        if i.get('id') == post_id:
            for key in i:
                print(f'{key}: {i.get(key)}')
            
    url = 'https://jsonplaceholder.typicode.com/comments'
    res = requests.get(url)
    data = res.json()
    count_comments = 0
    id_comm_list = []
    for i in data:
        if i.get('postId') == post_id:
            count_comments += 1
            id_comm_list.append(i.get('id'))
    print(f'Count of comments = {count_comments}, id list this comments = {id_comm_list}')

def todo_json(user_id,status):
    url = 'https://jsonplaceholder.typicode.com/todos'
    res = requests.get(url)
    data = res.json()
    for i in data:
        if i.get('userId') == user_id and i.get('completed') == status:
            print(i.get('title'))

def random_picture_json():
    url = 'https://jsonplaceholder.typicode.com/photos'
    res = requests.get(url)
    data = res.json()
    list_url = []
    for i in data:
        list_url.append(i.get('url'))
    print(random.choice(list_url))

main()
