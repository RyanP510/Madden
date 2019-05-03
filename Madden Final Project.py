import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]


print ("You are the OB for USC. 2 minutes to go. Your team is down by 5 "
           "One touchdown will win you the game...its now first down on your own 25 yard line with no timeouts, Do you throw or run?")

print ("A. Throw the ball B. Run the ball with your RB")
choice = input()
if choice in answer_A:
    print ("You threw the ball to your receiver, you gained 7 yards. It is now 2nd & 3 on the 32 yard line "
           "\nThe coach has now called a running play, \nDo you want to agree with coach and say yes or say no to audible to a pass play?")
    choice = input()
    if choice in yes:
        print ("You agreed with coach to run the ball and now only gained 2 yards to make it 3rd & 1, \n Do you throw or run the ball"
                "A. Throw B. Run")
        choice = input()
        if choice in answer_A: #for line 20
            print ("You completed a pass for 9 yards, ball on the 43 yard line, \nwhats the next play you want to run?"
                    "A. Throw B. Run")
            choice = input()
            if choice in answer_A: # for line 24
                print ("You threw the ball, it was intercepted...You LOST the game")
            if choice in answer_B: # for line 24
                print ("You ran the ball all the way to the end zone, you WON the game")

        if choice in answer_B: # for line 20
            print ("You ran the ball and went for 30 yards, ball on the opposing 36 yard line"
                   "Now Select next play  A. Throw B. Run")
            if choice in answer_A:
                print ("You threw a quick slant to the WR, he runs it in all the way....Touchdown....You WON")
            if choice in answer_B:
                print ("Handed it off to RB, he runs 20 yards...gets stripped and fumbles. Other team recovers and You LOST")

    if choice in no:
        print ("You audibled the play to a pass play, you completed a 15 yard pass, \nyou are now on your on 47 yard line, \nits now 1st & 10, coach said its on you to throw or run the ball,"
               " A. Throw the ball B. Run the ball")
        choice = input()
        if choice in answer_A:
            print ("You threw the ball down the field, it was an incomplete pass, its now 2nd & 10"
                    "A. Throw B. Run")


elif choice in answer_B:
    print ("You decided to run the ball, you have gained 2 yards. It is now 2nd & 8 on the 27 yard line"
           "Coach says its on you to throw or run now on 2nd & 8   A. Throw  B. Run")
    choice = input ()
    if choice in answer_A:
        print ("You just completed a 38 yard pass to your Tight End on the 35 yard line of the opposing side"
               "Next Play....A. Throw B. Run")
        choice = input()
        if choice in answer_A:
            print ("You decided to throw the ball into the endzone....ball was tipped and intercepted taken back for a pick 6. You LOST")
        if choice in answer_B:
            print ("You decided to run the ball, The RB ran all the way to the 3 yard line...Your team didnt make it up to the line before time expired and You LOST")
    if choice in answer_B:
        print ("You decided to run the ball for 23 yards to the 50 yard line"
               "Time is running out....Do you A. Throw or B. Run the ball?")
        choice = input()
        if choice in answer_A:
            print ("You threw the ball all the way to end zone, ball was tipped twice in the air...your receiver caught it. You WON!")
        if choice in answer_B:
            print ("You ran the ball, the linebacker came from behind to strip and recover for the other team. You LOST!")



