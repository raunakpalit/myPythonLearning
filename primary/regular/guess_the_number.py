a = [x for x in range(100)]
print(a)

def guess_number():
    unum = input("Think of a number from 1 to 100: ")
    ques1 = input("Is the number greater than 50 (y/n): ")
    if ques1 == 'y':
        ul = [x for x in range(50, 100)]
        ques2 = input("Is the number less than 75 (y/n): ")
        if ques2 == 'y':
            ul = [x for x in range(50, 75)]
            ques3 = input("Is the number even: (y/n): ")
            if ques3 == 'n':
                ul = [x for x in range(50, 75) if x%2 !=0] # 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73
                ques4 = input("Is the number divisible by 3: (y/n): ")
                if ques4 == 'n':
                    ul = [x for x in ul if x%3 !=0] # 53, 55, 59, 61, 65, 67, 71, 73
                    ques5 = input("Is the difference of ones and tens digit > 0: (y/n): ")
                    if ques5 == 'n':
                        ul = [i for i in ul if (i//10 - i%10)<0] # 59, 67
                        ques6 = input("Is the sum of ones and tens digit > 13: (y/n): ")
                        if ques6 == 'y':
                            print("The number is 59")
                        else:
                            print("The number is 67")
                    else:# 53, 55, 61, 65, 71, 73
                        ques6 = input("Is the sum of ones and tens digit > 8: (y/n): ")
                        if ques6 == 'y': # 55, 65, 73
                            ques7 = input("Is the tens digit 5: (y/n): ")
                            if ques7 == 'n':
                                print("The number is 73")
                            else: # 55, 65
                                ques8 = input("Is the ones digit 5: (y/n): ")
                                if ques8 == 'y':
                                    print("The number is 55")
                                else:
                                    print("The number is 65")
                        else: # 53, 61, 71
                            ques7 = input("Is the tens digit 1: (y/n): ")
                            if ques7 == 'n':
                                print("The number is 53")
                            else: # 61, 71
                                ques8 = input("Is the ones digit 6: (y/n): ")
                                if ques8 == 'y':
                                    print("The number is 61")
                                else:
                                    print("The number is 71")
                else: # 51, 57, 63, 69
                    ul = [x for x in ul if x % 3 == 0]
                    ques5 = input("Is the difference of ones and tens digit > 0: (y/n): ")
                    if ques5 == 'n': # 57, 69
                        ul = [i for i in ul if (i // 10 - i % 10) < 0]
                        ques6 ==
                    else: # 51, 63





guess_number()
