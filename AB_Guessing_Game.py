def str2ilist(guess_str_in):
    guess_ilist_in=[]
    for digit in guess_str_in:
        guess_ilist_in.append(int(digit))
    return guess_ilist_in

def numbers_generate():
    import random
    digit_int = int(input ("Please enter the digit number you like to guess:"))
    answer_ilist_in=random.sample([0,1,2,3,4,5,6,7,8,9], digit_int)
    type (answer_ilist_in)
    return answer_ilist_in

def compare(digit_count_in, answer_ilist_in, guess_ilist_in):
#    print answer_ilist_in
#    print guess_ilist_in
    A_count_int=0
    B_count_int=0
    for i_int in answer_ilist_in:
        for j_int in guess_ilist_in:
            if i_int==j_int:
                if answer_ilist_in.index(i_int)==guess_ilist_in.index(j_int):
                    A_count_int=A_count_int+1
                    if A_count_int == digit_count_in: print ("You Got It, Good Job!!")
                else: B_count_int=B_count_int+1
            else: pass


    print ("%dA %dB" %(A_count_int, B_count_int))
    return A_count_int


def play(play_count_in):
    answer_ilist = numbers_generate()
    digit_count = len(answer_ilist)
    guess_count_int = 1
    A_int = 0
    while A_int != digit_count:
        guess_str = str(input("Please enter your guessing No.%d: " % guess_count_int))
        guess_ilist = str2ilist(guess_str)
        A_int = compare(digit_count, answer_ilist, guess_ilist)
        guess_count_int = guess_count_int+1
        play_count_in = play_count_in+1
    return play_count_in

""" Start Here """
play_count = 0
while True:
    if play_count == 0:
        play_count = play(play_count)
        continue
    else:
        go = raw_input ("Would you like to play again(y or n)?")
        if go == 'y':
            play_count = play(play_count)
            continue
        else:
            print "Goodbye"
            break


