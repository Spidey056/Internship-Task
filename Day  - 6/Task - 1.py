from IPython.display import clear_output

def display_options():
    clear_output()
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    print('1.Rock')
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    print('2.Paper')
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    print("3.Scissors")


def opp_choice(choice):
    if (choice == 1):
        
        r = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        
     Rock   
        
        """

        return r
        
    elif (choice == 2):
        
        p = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
        
     Paper   
        """
        return p 
    
    elif (choice == 3):
        
        s = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
        
     Scissors   
        """
        return s
        
    else:
        print("\nPlease Choose Correct choice")    



def choose_winner(ch1,ch2):
    if ch1==1 and ch2==3:
        print("You Win")    
    elif ch1==3 and ch2==1:
        print("Computer Win")
    
    elif ch1==2 and ch2==1:
        print("You Win")
    elif ch1==1 and ch2==2:
        print("Computer Win")
    
    elif ch1==3 and ch2==2:
        print("You Win")
    elif ch1==2 and ch2==3:
        print("Computer Win")
        
    elif ch1==1 and ch2==1:
        print("Draw")
    elif ch1==2 and ch2==2:
        print("Draw")
    elif ch1==3 and ch2==3:
        print("Draw")


import random

game_on = True

while game_on :
    
    display_options()
    
    print("\nLet's Play Rock Paper Scissors")
    
    choice = True
    
    while choice:
        
        ch_1 = int(input("\nEnter Your Choice:"))
    
        chd_1 = opp_choice(ch_1)
        
        if (ch_1 > 4 or ch_1==0):
            
             pass
        
        else:
            
            choice = False
    
    print(chd_1)    
    
    ch_2 = random.randint(1,3)
    
    chd_2 = opp_choice(ch_2)
    
    print(chd_2)
    
    choose_winner(ch_1,ch_2)
    
    check = True
    
    while check:
    
        con = input("\nDo You Want to continue?\n\nIf Yes Type Y, If No Type N")
    
        con = con.upper()
    
        if(con=="Y"):
        
            game_on = True
            check = False
    
        elif(con=="N"):
        
            game_on = False
            check = False
            print("\nThank You!")
    
        else:
            print("\nEnter Correct Keyword.")
            pass
        