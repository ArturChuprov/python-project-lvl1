import random
import prompt


print('Welcome to the Brain Games!')
player_name = prompt.string('May I have your name? ')
print('Hello, {}!'.format(player_name))


def is_even(number):
    return number % 2 == 0


def run_game():
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    count_correct_answer = 0
    text = 'is wrong answer ;(. Correct answer was'
    while count_correct_answer < 3:
        number = random.randint(1, 100)
        if is_even(number) is True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print('Question: {}'.format(number))
        player_answer = prompt.string('Your answer: ')
        if player_answer == correct_answer:
            print('Correct!')
            count_correct_answer += 1
        else:
            print("'%s'" % player_answer, text, "'%s'" % correct_answer)
            print('Let\'s try again, %s!' % player_name)
            return
    print('Congratulations, %s!' % player_name)
