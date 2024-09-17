import os 


restaurants = [{'name':'Luigis', 'category':'Pizza', 'active': False},
                {'name': 'Nihon', 'category':'Japanese','active':True},
                {'name': 'LeChef', 'category':'French','active': False}]




def show_program_name():
    print("""
█▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀   █▀▀ █░░ ▄▀█ █░█ █▀█ █▀█ █▀
██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█   █▀░ █▄▄ █▀█ ▀▄▀ █▄█ █▀▄ ▄█
      """)

def show_options():
    print('1. Register Restaurant')
    print('2. List Restaurant')
    print('3. Changing the state of the restaurant')
    print('4. Leave\n')

def finish_app():
    display_subtitle('Leaving the app\n')

def return_to_menu():
    input('\nPress a key to go back to the main menu')
    main()


def invalid_option():
    print('Invalid option\n')
    return_to_menu()

def display_subtitle(text):
    os.system('cls')
    line = '*' * (len(text))
    print(line)
    print(text)
    print(line)

def register_new_restaurant():
    display_subtitle('Register new restaurants\n')
    restaurant_name = input('Type the name of the restaurant you want to register: ')
    category = input(f'Type the category of the restaurant {restaurant_name}: ')
    restaurant_data = {'name': restaurant_name, 'category':category, 'active': False}
    restaurants.append(restaurant_data)
    print(f'The restaurant {restaurant_name} was successfully registered\n')
    return_to_menu()



def list_restaurant():
    display_subtitle('Listing all restaurants\n')
    print(f'{'restaurant name'.ljust(23)} | {'category'.ljust(20)} | status')
    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        category = restaurant['category']
        active = 'active' if restaurant['active'] else 'disable'
        print(f' - {restaurant_name.ljust(20)} | {category.ljust(20)} | {active}')

    return_to_menu()



def change_restaurant_state():
    display_subtitle('changing restaurant state')
    restaurant_name = input('Type the name of the restaurant you want to change the state: ')
    restaurant_found = False

    for restaurant in restaurants:
        if restaurant_name == restaurant['name']:
            restaurant_found = True
            restaurant['active'] = not restaurant['active']
            message = f'The restaurant {restaurant_name} was successfully activated' if restaurant['active'] else f'The restaurant {restaurant_name} was successfully disabled'
            print(message)

    if not restaurant_found:
        print('The restaurant was not found')

    return_to_menu()

def choose_option():
    try:
        chosen_option = int(input('Choose an option: '))


        if chosen_option == 1 :
           register_new_restaurant()
        elif chosen_option == 2:
            list_restaurant()
        elif chosen_option == 3:
           change_restaurant_state()
        elif chosen_option == 4:
            finish_app()
        else:
            invalid_option()
    except:
        invalid_option()




def main():
    os.system('cls')
    show_program_name()
    show_options()
    choose_option()

if __name__ == '__main__':
    main()
