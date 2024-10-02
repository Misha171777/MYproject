import time
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
myworld=["fortuna" , "windrise" , "aigis"]
myworld2=["windrise", "aigis"]
myworld4=["fortuna", "aigis"]
myworld3=["fortuna", "windrise"]
world=["fortuna"]
world2=["windrise"]
world3=["aigis"]
invent=[]
A=input("what is your name..?  ")
time.sleep(3)
x = input ("hello there , would you like to play a game " +str(A) +"?     ")

time.sleep(2)
if x == "no":
    print("ok, maybe some other time")
    exit
else :
    with open("plot.txt", "r") as file:
        print (file.read())
        y =  input ("do you want to head to the door? ")
        time.sleep(3)
        if y == "no":
            print("fine")
            exit
        else :
            with open("plot2.txt", "r") as file:
                print (file.read())
                print(myworld)
                time.sleep(3)
                a = input("what city do you want to go to now?  ")
                chest=["book"]
                if a == "fortuna" or a=="1" or a=="left" or a=="first":
                     with open ("fplot.txt" , "r") as file:
                          time.sleep(2)
                          print(file.read())
                          print(chest)
                          time.sleep(3)
                          w=input("would you like to take those items")
                          if w == "yes":
                              invent.append("book")
                              print("items added to inventory!!")
                          time.sleep(3)
                          with open ("moreplot.txt" , "r") as file:
                              print(file.read())
                              print(myworld2)
                              s=input("choose your next destination")
                              if s=="windrise":
                                  with open ("wplot.txt" , "r") as file:
                                      print(file.read())
                                      time.sleep(2)
                                      input("welcome to our land , you must be tired from the travel  ")
                                      print("hehe , then follow me to get some rest at the city")
                                      time.sleep(2)
                                      print ("you walk along with the bird through the grassy fields")
                                      time.sleep(1)
                                      print("you have multiple conversations regarding you and your life")
                                      input("the bird says: so how did you get here? ")
                                      input("interesting...and what is your goal for now?  ")
                                      print("well, i hope you achieve it no matter how many obstacles you encounter")
                                      with open ("ouioui.txt" , "r") as file:
                                          print(file.read())
                                          print(world3)
                                          time.sleep(2)
                                          print("now to our last destination")
                                          time.sleep(3)
                                          with open ("aigis.txt" , "r") as file:
                                              print(file.read())
                                              time.sleep(2)
                                              with open ("end.txt") as file:
                                                  print(file.read())
                                                  time.sleep(2)
                                                  print("the end")
                              if a=="aigis":
                                  with open ("aigis.txt" , "r") as file:
                                      print(file.read())
                                      time.sleep(2)
                                      print(world2)
                                      time.sleep(2)
                                      print("for our last destination")
                                      with open ("wplot.txt" , "r") as file:
                                          print(file.read())
                                          time.sleep(2)
                                          input("welcome to our land , you must be tired from the travel  ")
                                          print("hehe , then follow me to get some rest at the city")
                                          time.sleep(2)
                                          print ("you walk along with the bird through the grassy fields")
                                          time.sleep(1)
                                          print("you have multiple conversations regarding you and your life")
                                          input("the bird says: so how did you get here? ")
                                          input("interesting...and what is your goal for now?  ")
                                          print("well, i hope you achieve it no matter how many obstacles you encounter")
                                          with open ("ouioui2.txt" , "r") as file:
                                              print(file.read())
                                              time.sleep(2)
                                              with open ("end.txt") as file:
                                                  print(file.read())
                                                  time.sleep(2)
                                                  print("the end")


                if a=="windrise" or a=="2" or a=="middle" or a=="second":
                    with open ("wplot.txt" , "r") as file:
                        print(file.read())
                        time.sleep(2)
                        input("welcome to our land , you must be tired from the travel  ")
                        print("hehe , then follow me to get some rest at the city")
                        time.sleep(2)
                        print ("you walk along with the bird through the grassy fields")
                        time.sleep(1)
                        print("you have multiple conversations regarding you and your life")
                        input("the bird says: so how did you get here? ")
                        input("interesting...and what is your goal for now?  ")
                        print("well, i hope you achieve it no matter how many obstacles you encounter")
                        time.sleep(2)
                        with open ("ouioui.txt" , "r") as file:
                            print(file.read())
                            print(myworld4)
                            d=input("where to now?  ")
                            if d=="fortuna":
                                with open ("fplot.txt" , "r") as file:
                                    time.sleep(2)
                                    print(file.read())
                                    print(chest)
                                    time.sleep(3)
                                    w=input("would you like to take those items")
                                    if w == "yes":
                                        invent.append("book")
                                        print("items added to inventory!!")
                                        time.sleep(3)
                                        with open ("moreplot.txt" , "r") as file:
                                            print(file.read())
                                            print(world3)
                                            time.sleep(2)
                                            print("now to our last destination")
                                            with open ("aigis.txt" , "r") as file:
                                              print(file.read())
                                              time.sleep(2)
                                              with open ("end.txt") as file:
                                                  print(file.read())
                                                  time.sleep(2)
                                                  print("the end")
                            if d=="aigis":
                                with open ("aigis.txt" , "r") as file:
                                    print(file.read())
                                    time.sleep(2)
                                    print("you encounter 2 doors in front of you ")
                                    print(world)
                                    print("and now your last destination")
                                    time.sleep(2)
                                    with open ("fplot.txt" , "r") as file:
                                        time.sleep(2)
                                        print(file.read())
                                        print(chest)
                                        time.sleep(3)
                                        w=input("would you like to take those items")
                                        if w == "yes":
                                            invent.append("book")
                                            print("items added to inventory!!")
                                            time.sleep(3)
                                            with open ("moreplot.txt" , "r") as file:
                                                print(file.read())
                                                time.sleep(2)
                                                with open ("end.txt") as file:
                                                    print(file.read())
                                                    time.sleep(2)
                                                    print("the end")

                if a=="aigis":
                    with open ("aigis.txt" , "r") as file:
                        print(file.read())
                        time.sleep(2)
                        print("you encounter 2 doors in front of you ")
                        print(myworld3)
                        j=input("what will you choose next")
                        if j == "fortuna" or a=="1" or a=="left" or a=="first":
                            with open ("fplot.txt" , "r") as file:
                                time.sleep(2)
                                print(file.read())
                                print(chest)
                                time.sleep(3)
                                c=input("would you like to take those items")
                                if c == "yes":
                                    invent.append("book")
                                    print("items added to inventory!!")
                                    time.sleep(3)
                                with open ("moreplot.txt" , "r") as file:
                                        print(file.read())
                                        print(world2)
                                        print("for our last destination")
                                        with open ("wplot.txt" , "r") as file:
                                            print(file.read())
                                            time.sleep(2)
                                            input("welcome to our land , you must be tired from the travel  ")
                                            print("hehe , then follow me to get some rest at the city")
                                            time.sleep(2)
                                            print ("you walk along with the bird through the grassy fields")
                                            time.sleep(1)
                                            print("you have multiple conversations regarding you and your life")
                                            input("the bird says: so how did you get here? ")
                                            input("interesting...and what is your goal for now?  ")
                                            print("well, i hope you achieve it no matter how many obstacles you encounter")
                                            with open ("ouioui2.txt" , "r") as file:
                                                print(file.read())
                                                time.sleep(2)
                                                with open ("end.txt") as file:
                                                  print(file.read())
                                                  time.sleep(2)
                                                  print("the end")
                        if j=="windrise":
                                  with open ("wplot.txt" , "r") as file:
                                      print(file.read())
                                      time.sleep(2)
                                      input("welcome to our land , you must be tired from the travel  ")
                                      print("hehe , then follow me to get some rest at the city")
                                      time.sleep(2)
                                      print ("you walk along with the bird through the grassy fields")
                                      time.sleep(1)
                                      print("you have multiple conversations regarding you and your life")
                                      input("the bird says: so how did you get here? ")
                                      input("interesting...and what is your goal for now?  ")
                                      print("well, i hope you achieve it no matter how many obstacles you encounter")
                                      with open ("ouioui.txt" , "r") as file:
                                          print(file.read())
                                          print(world)
                                          time.sleep(2)
                                          print("now to our last destination")
                                          time.sleep(3)   
                                          with open ("fplot.txt" , "r") as file:
                                              time.sleep(2)
                                              print(file.read())
                                              print(chest)
                                              time.sleep(3)
                                              w=input("would you like to take those items")
                                              if w == "yes":
                                                  invent.append("book")
                                                  print("items added to inventory!!")
                                                  time.sleep(3)
                                                  with open ("moreplot.txt" , "r") as file:
                                                      print(file.read())
                                                      time.sleep(2)
                                                      with open ("end.txt") as file:
                                                          print(file.read())
                                                          time.sleep(2)
                                                          print("the end") 
    time.sleep(2)
    print("thank you for playing my game , it's barely anything but i tried")
    time.sleep(2)                                                              
    Q=input("how was your experience in the cities?  ")
    B=input("what was your favourite city so far  ")
    time.sleep(2)
    print("very well , have a lovely day!")


    data_to_append=[str(A),str(a) , "full", str(B), Q]
    with open("DATA.csv", "a"  , newline="") as csvfile:
        csvwriter =csv.writer(csvfile)
        csvwriter.writerow(data_to_append)
        csvfile.close
    dataframe=  pd.read_csv("DATA.csv")
    print("the data collected : "
           , dataframe)
    
    
    y = np.array([40, 40, 20,])
    mylabels = ["Aigis", "Fortuna", "Windrise",]

    plt.pie(y, labels = mylabels)
    plt.show() 


    x = np.array(["pleasant",  "unpleasant",  "neutral"])


    y = np.array([5,0,3])
    plt.xlabel("Average experience")
    plt.ylabel("approximate number of opinions")
    plt.plot(x, y)
    plt.show()


