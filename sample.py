def enter_evaluation():
    while True:
        print('Please enter a rating from 1 to 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 5:
                print('Please enter a comment')
                comment = input()
                post = f'Point: {point} Comment: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
            else:
                print('Please enter a rating from 1 to 5')
        else:
            print('Please enter the evaluation points as numbers')

def check_results():
    print('Previous results')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

def main():
    while True:
        print('Choose the action you want to perform')
        print('1: Enter evaluation points and comments')
        print('2: Check previous results')
        print('3: Exit')
        num = input()

        if num.isdecimal():
            num = int(num)

            if num == 1:
                enter_evaluation()
            elif num == 2:
                check_results()
            elif num == 3:
                print('Exiting')
                break
            else:
                print('Please enter a number from 1 to 3')
        else:
            print('Please enter a number from 1 to 3')

if __name__ == "__main__":
    main()
