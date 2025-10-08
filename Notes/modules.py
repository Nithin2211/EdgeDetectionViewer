# MODULE - A file containing code you want to include in your program 
#          use 'import' to include a module (built-in or your own) 
#          useful to break up a large program reusable separate files

# print(help("module"))
# print(help("math"))

# from math import pi
# print(pi)                                                    # output - 3.1415...

# IMPORT MATH as m
# print(m.pi)                                               # output - 3.1415...
# print(m.e)                                                # output - 2.718...
# print(m.sqrt(4))                                          # output - 2
# print(m.ceil(9.1))                                        # output - 10(highest round off)
# print(m.floor(9.1))                                       # output - 9(lowest round off)

# IMPORT RANDOM
#   print(help(random))                                        # output - it prints all the function of random with definitions
#   low = 1
#   high = 100
#   num = random.randint(low, high)
#   print(num)                                                 # output - it prints random numbers between 1 to 100 (only whole numbers)

#   num = random.random()
#   print(num)                                                 # output - it prints random numbers between 0 to 1 (only float numbers)

#   options = ("rock", "paper", "scissors")
#   cards = ["2", "3", "4", "5"]
#   print(random.choice(options))                              # output - choose a random element from a non-empty sequenc
#   print(random.shuffle(cards))                               # output - Shuffle list cards in place, and return None

# IMPORT TIME
# Syntax
#   time.sleep()                                               # Pauses execution for 2 seconds

# MY OWN MODULE
# import example
# result = example.pi
# result = example.square(3)
# print(result)

# IMPORT DATETIME
#   date  = datetime.date(2025, 1, 2)
#   today = datetime.date.today()
#   time  = datetime.time(12, 30, 0)
#   now   = datetime.datetime.now()
#   now1   = now.strftime("%H:%M:%S %m-%d-%Y")                 # These are the format specifier used for this module please check more format specifiers in the documentation.
#   target_datetime = datetime.datetime(2030, 1, 2 ,12 ,30 ,1)
#   current_datetime = datetime.datetime.now()

#   if target_datetime < current_datetime:
#       print("target date has passed")
#   else:
#       print("Target date has NOT passed")                    # output - target date has not passed

#   print(date)                                                # output - 2025-01-02
#   print(today)                                               # output - it prints today's date
#   print(time)                                                # output - 12:30:00
#   print(now)                                                 # output - 2024-07-14 09:41:55.409676
#   print(now1)                                                # output - 09:43:14 08-22-2025

#   MULTITHREADING - Used to perform multiple tasks concurrently (multitasking)
#                    Good for I/O bound tasks like reading files or fetching data from APIs
#                    threading. Thread(target = my_function)

# Syntax
#   import threading
#   import time
#   def walk_dog():
#       time.sleep(8)
#       print("You finish walking the dog")

#   def take_out_the_tarsh():
#       time.sleep(2)
#       print("You take out the trash")

#   def get_mail():
#       time.sleep(4)
#       print("You get the mail")

#   chore1 = threading.Thread(target = walk_dog)               # In this thread(target = my_func) is a constructor.
#   chore1.start()

#   chore2 = threading.Thread(target = take_out_the_trash)               
#   chore2.start()

#   chore3 = threading.Thread(target = get_mail)               
#   chore3.start()

#   chore1.join()
#   chore2.join()
#   chore3.join()

#   print("All chores are completed")

#   IMPORTANT
#   IN THIS IF WE DIRECTLY CALL THE FUNCTION LIKE WALK_DOG() THEN THEWE GET OUTPUT ONLY ONE AT A TIME.
#   IF WE USE THREADING LINE NO 82-89 THEN THE OUTPUT WILL BE GENERATED SIMULTANEOUSLY FOR ALL THE CALL FUNCTION.
#   THE JOIN FUNCTION IS USED TO WAIT FOR THE TREADS TO COMPLETE THEIR WORK AND THEN MOVE TO NEXT LINE.

#   OUTPUT;;
#   You take out the trash
#   You get the mail
#   You finish walking the dog
#   All chores are completed

#   PIP INSTALL PACKAGE_ITEM - YOU HAVE TO RUN THIS COMMAND IN TERMINAL TO INSTALL THE PARTICULER MODULE IF IT IS NOT INSTALLED