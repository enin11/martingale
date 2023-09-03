""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  		 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  		 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  		 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  		 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 		  		  		    	 		 		   		 		  
or edited.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		  		 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  		 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Student Name: Marc Cabote  		  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: mcabote3  		  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 903859736	  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np
import matplotlib.pyplot as plt		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def author():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return "mcabote3"  # replace tb34 with your Georgia Tech username.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def gtid():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return  903859736  # replace with your GT ID number  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  

def get_spin_result(win_prob):  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		  		 		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    result = False  		  	   		  		 		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		  		 		  		  		    	 		 		   		 		  
        result = True  		  	   		  		 		  		  		    	 		 		   		 		  
    return result

def test_code():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    win_prob = 9/19   # probability of winning red or black
                      # number of black or red pockets/total number of pockets
                      # 18/38 or 9/19 about 47.37%
    np.random.seed(gtid())  # do this only once  		  	   	

    # for i in range(10):	  		 		  		  		    	 		 		   		 		  
    #     print(get_spin_result(win_prob))  # test the roulette spin  

    # add your code here to implement the experiments
    experiment_1(win_prob)  		  
    experiment_2(win_prob)	 
"""
--------Professor Balch's Martingale Pseudocode-----------------
episode_winnings = $0
while episode_winnings < $80:
	won = False
	bet_amount = $1
	while not won
		wager bet_amount on black
		won = result of roulette wheel spin
		if won == True:
			episode_winnings = episode_winnings + bet_amount
		else:
			episode_winnings = episode_winnings - bet_amount
			bet_amount = bet_amount * 2
----------------------------------------------------------------
"""  		  	   		  		 		  		  		    	 		 		   		 		  
def simple_simulator(win_prob):

    outcome_arr = np.full((1000),80) #fill data forward with value of 80
    episode_winnings = 0
    episode_counter = 0

    while episode_winnings < 80:
        won = False
        bet_amount = 1

        while not won and episode_counter < 1000:

            outcome_arr[episode_counter] = episode_winnings
            episode_counter += 1

            won = get_spin_result(win_prob)
            
            if won:
                episode_winnings += bet_amount
            
            else:
                episode_winnings -= bet_amount
                bet_amount *= 2

                                                                                                
    return outcome_arr

def realistic_simulator(win_prob):

    outcome_arr = np.full((1000),80) #fill data forward with value of 80
    episode_winnings = 0
    episode_counter = 0

    while episode_winnings < 80:
        won = False
        bet_amount = 1

        while not won: 

            if episode_counter > 1000:
                return outcome_arr

            outcome_arr[episode_counter-1] = episode_winnings
            episode_counter += 1

            won = get_spin_result(win_prob)   
            if won:
                episode_winnings += bet_amount
            
            else:
                episode_winnings -= bet_amount
                bet_amount *= 2

                if episode_winnings == -256:
                    outcome_arr[episode_counter:] = episode_winnings
                    return outcome_arr
                
                if episode_winnings - bet_amount < -256:
                    bet_amount = episode_winnings + 256
                                                                                                
    return outcome_arr

	 		  		  		    	 		 		   		 		  
def experiment_1(win_prob):
    """
    Figure 1: Run your simple simulator 10 episodes and track the winnings, 
    starting from 0 each time. Plot all 10 episodes on one chart using Matplotlib functions. 
    The horizontal (X) axis must range from 0 to 300, the vertical (Y) axis must range from –256 to +100. 
    We will not be surprised if some of the plot lines are not visible 
    because they exceed the vertical or horizontal scales.  
    """
    plt.title("Figure 1: 10 Episode Simulation")
    plt.xlabel("Trial #")
    plt.ylabel("Winnings")
    plt.axis([0,300,-256,100])
    

    """
    Run 10 episodes and plot
    """
    for i in range(10):
        episode = simple_simulator(win_prob)
        plt.plot(episode, label=f"episode {i + 1}")
        
    plt.legend()   

    plt.savefig("images/figure1.png")
    plt.clf()

    """
    Figure 2: Run your simple simulator 1000 episodes. (Remember that 1000 successive bets are one episode.) 
    Plot the mean value of winnings for each spin round using the same axis bounds as Figure 1. 
    For example, you should take the mean of the first spin of all 1000 episodes. Add an additional line 
    above and below the mean, at mean plus standard deviation, and mean minus standard deviation of the winnings at each point.
    """  		  		 		  		  		    	 		 		   		 		  
   
    """
    Figure 3: Use the same data you used for Figure 2 but plot the median instead of the mean. 
    Add an additional line above and below the median to represent the median plus standard deviation 
    and median minus standard deviation of the winnings at each point.  
    """

    outcome_arr = np.empty((1000,1000))
    """
    Run 1000 episodes
    """
    for i in range (1000):
        episode = simple_simulator(win_prob)
        outcome_arr [i] = episode

    """
    Calculate std, mean and median
    """
    std = np.std(outcome_arr, axis = 0)

    mean_arr = np.mean(outcome_arr, axis = 0)
    mean_plus = mean_arr + std
    mean_minus = mean_arr - std

    med_arr = np.median(outcome_arr, axis = 0)
    med_plus = med_arr + std
    med_minus = med_arr - std

    """
    Plot mean
    """
    plt.title("Figure 2: Mean")
    plt.xlabel("Trial #")
    plt.ylabel("Winnings")
    plt.axis([0,300,-256,100])

    plt.plot(mean_arr, label = "mean")
    plt.plot(mean_plus, label = "+std")
    plt.plot(mean_minus, label = "-std")
    plt.legend()

    plt.savefig("images/figure2.png")
    plt.clf()


    """
    Plot median
    """
    plt.title("Figure 3: Median")
    plt.xlabel("Trial #")
    plt.ylabel("Winnings")
    plt.axis ([0,300,-256,100])

    plt.plot(med_arr, label = "median")
    plt.plot(med_plus, label = "+std")
    plt.plot(med_minus, label = "-std")
    plt.legend()
      
    plt.savefig("images/figure3.png")
    plt.clf()

def experiment_2(win_prob):
    """
    Figure 4: Run your realistic simulator 1000 episodes and track the winnings, starting from 0 each time. 
    Plot the mean value of winnings for each spin using the same axis bounds as Figure 1. Add an additional 
    line above and below the mean at mean plus standard deviation and mean minus standard deviation of the winnings at each point.  
    """

    """
    Figure 5: Use the same data you used for Figure 4 but plot the median instead of the mean. Add an additional 
    line above and below the median to represent the median plus standard deviation and median minus standard deviation of the winnings at each point.
    """
    
    outcome_arr = np.empty((1000,1000))
    """
    Run 1000 episodes
    """
    for i in range (1000):
        episode = realistic_simulator(win_prob)
        outcome_arr [i] = episode

    """
    Calculate std, mean and median
    """
    std = np.std(outcome_arr, axis = 0)

    mean_arr = np.mean(outcome_arr, axis = 0)
    mean_plus = mean_arr + std
    mean_minus = mean_arr - std

    med_arr = np.median(outcome_arr, axis = 0)
    med_plus = med_arr + std
    med_minus = med_arr - std

    """
    Plot mean
    """
    plt.title("Figure 4: Realistic Mean")
    plt.xlabel("Trial #")
    plt.ylabel("Winnings")
    plt.axis([0,300,-256,100])

    plt.plot(mean_arr, label = "mean")
    plt.plot(mean_plus, label = "+std")
    plt.plot(mean_minus, label = "-std")
    plt.legend()
    
    plt.savefig("images/figure4.png")
    plt.clf()

    """
    Plot median
    """
    plt.title("Figure 5: Realistic Median")
    plt.xlabel("Trial #")
    plt.ylabel("Winnings")
    plt.axis ([0,300,-256,100])

    plt.plot(med_arr, label = "median")
    plt.plot(med_plus, label = "+std")
    plt.plot(med_minus, label = "-std")
    plt.legend()
    
    plt.savefig("images/figure5.png")
    plt.clf()


if __name__ == "__main__":  		  	   		  		 		  		  		    	 		 		   		 		  
    test_code()  		  	   		  		 		  		  		    	 		 		   		 		  
