import time


def fizz_buzz_game():
    list_of_values = []
    current_number = 1
    while current_number <= 100:
        if current_number % 3 == 0 and current_number % 5 == 0:
            list_of_values.append('FizzBuzz')
            current_number += 1
            
        elif current_number % 3 == 0:
            list_of_values.append('Fizz')
            current_number += 1

        elif current_number % 5 == 0:
            list_of_values.append('Buzz')
            current_number += 1

        else:
            list_of_values.append(current_number)
            current_number += 1

    return list_of_values



if __name__ == '__main__':
    result = fizz_buzz_game()
    print(result)
    time.sleep(20)
    
