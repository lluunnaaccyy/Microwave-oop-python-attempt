# Brandon Salman-Tehrani
# 10.1 Your Own Class
# my class is based on a microwave and looks at cook time, food mode, power level
class Microwave:
    # class attribute: the microwave needs electricity
    has_electricity = True

    def __init__(self, food_mode, power_level = 0, cook_time = 0):
        # establishing my data variables
        self.__cook_time = cook_time
        self.__food_mode = food_mode
        self.__power_level = power_level

    # get-set methods for the cook time
    def set_time(self, time):
        self.__cook_time = time
        
    def get_time(self):
        return self.__cook_time

    # get-set methods for the power level
    def set_power_level(self, power):
        self.__power_level = power

    def get_power_level(self):
        return self.__power_level

    # magic method to return the end result of what was inputted into the microwave
    def __str__(self):
        return (f'Food mode: {self.__food_mode}\nPower Level: {self.__power_level}%\nCook Time: {self.__cook_time} seconds')

    
    # method to warn the person about how well cooked their food is
    def temperature_warning(self):
        # warning for too hot
        if self.__cook_time > 120:
            return 'Your food is too hot! Wait for it to cool down if you do not want to burn your tongue! Enjoy when cooled!'
        # warning for too cold
        elif self.__cook_time in range(1, 39):
            return 'Your food is still cold! Put it back in for longer.'
        # perfect temperature statement
        elif self.__cook_time in range(40, 50):
            return 'Your food is cooked to perfection! Enjoy!'
        # warning for potentially too hot
        elif self.__cook_time in range(51, 119):
            return 'Your food may be little hot. Proceed with caution...'

    # method to imitate a timer that would be on a microwave
    def timer(t):
        # importing the time module to make things easier
        import time
        # while the value is over 0 the timer still goes
        while t > 0:
            print(t)
            # the timer goes down by 1
            t -= 1
            time.sleep(1)

# main function with my demo program inside
def main():
    # while loop to ensure either 'timer' or 'cook' is entered
    while True:
        # input that determines which mode the microwave will run
        w = str(input('Hello! I am a SmartMicrowaveTM!\nWould you like to "cook" or set a "timer"? '))
        # if 'timer' is entered
        if w == 'timer':
            # I was not sure how to access this function in my main function.
            def timer(t):
                import time
                while t > 0:
                    print(t)
                    t -= 1
                    time.sleep(1)
                print("timer finished!")
            # taking the input for the timer(in seconds)
            print("Enter how long you want to set the timer for(in seconds): ")
            seconds = input()
            # error handling if input wasn't an integer
            while not seconds.isdigit():
                print("That wasn't a valid time. Please enter a valid time:")
                seconds = input()
            seconds = int(seconds)
            timer(seconds)
        # if 'cook' is entered
        elif w == 'cook':
            break
    # list of cooking modes that are possible
    modes = ['time cook', 'reheat', 'popcorn', 'frozen dinner', 'pizza', 'chicken']
    while True:
        # taking in the mode input
        m = input('Please enter your desired mode: ')
        # making sure the mode inputted is one of the ones in the list
        if m not in modes:
            print('We do no currently have this mode. Look out for future software updates, it may get added!')
        elif m in modes:
            break
    print('\n')
    while True:
        # taking the input for the power level
        p = float(input('Please select your power level: '))
        # error handling
        if p < 0:
            print('Enter a valid power level please')
        elif p > 100:
            print('Enter a valid power level please')
        else:
            break
    print('\n')

    while True:
        # taking the time input
        t = float(input('Please enter your desired cook time(in seconds): '))
        # eroor handling
        if t < 0:
            print('Please enter a time')
        else:
            break
    print('\n')
    # calling the class and inputting the required arguments
    uu = Microwave(m, p, t)
    # printing the results
    print(str(uu))
    # using my temperature_warning method to check the temperature of the food
    print(uu.temperature_warning())
    
# calling the main function
if __name__ == '__main__':
    main()