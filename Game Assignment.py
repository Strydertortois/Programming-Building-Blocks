
user_name = input('Please input your username: ')
print()
print(f'Welcome {user_name}. You are lost in a cave and you are trying to find a way out. You have a flashlight. You must make the correct choices to find your way out.')

Level_1 = input('As you are walking down the cave you see a lever. Do you pull the lever (a) or do you keep walking? (b): ')
if Level_1.lower() == 'a':
    print()
    print('You pull the lever and you hear a faint rumbling noise. All of the sudden the cave collapses...')
    print('You died! Please restart game...')

elif Level_1.lower() == 'b':
    print()
    Level_2 = input('You continue walking and come to a fork in the cave. You can see a faint light coming from the tunnel on the right while the tunnel on the left is pitch black. Do you choose the tunnel on the right (a) or the tunnel on the left (b)?: ')
    
    if Level_2.lower() == 'a':
        print()
        Level_3 = input('You take the cave to the right and as you walk the light gets lighter and lighter. You continue walking and notice a rope hanging down from an opening in the ceiling and you can see the outside world above! do you climb the rope (a) or do you continue walking (b)?: ')
       
        if Level_3.lower() == 'a':
            print()
            print('You begin climbing the rope. You are almost to the top when suddenly, the rope snaps and you fall to your demise...')
            print('You died! Please restart game...')
       
        elif Level_3.lower() == 'b':
            print()
            print('You continue walking down the cave and it begins to incline upwards! You keep walking and eventually you reach the world above!')
            Reward = input('Congrats! You beat the level! Choose either 1,000xp (a) or 1,000 coins (b): ')

            if Reward.lower() == 'a':
                print()
                print('You have received 1,000xp! Thanks for playing!')
                
            elif Reward.lower() == 'b':
                print()
                print('You have received 1,000 coins! Thanks for playing')

            else:
                print('That is not an option')
                
        else:
            print('That is not an option')
   
    elif Level_2.lower() == 'b':
        print()
        print('You decide to take the cave to the left, you walk for hours and all of the sudden your flashlight runs out of battery. try to find your way back to where the tunnels parted but you become dissorientated...')
        print('You eventually die of dehydration! Please restart game...')
   
    else:
        print('That is not an option')

else:
    print()
    print('That is not an option')
