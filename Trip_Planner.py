
import random  

def trip_planner_welcome(name):
    print("Welcome to tripplanner v1.0, " + name)

def estimated_time_rounded(estimated_time):
    rounded_time = round(float(estimated_time))
    return rounded_time

def destination_setup():
    origin = input("Enter your starting location: ")
    destination = input("Enter your destination: ")
    estimated_time = input("Enter the estimated time for the trip (in hours): ")
    mode_of_transport = input("Enter your mode of transport (default is Car): ")

    if not mode_of_transport:
        mode_of_transport = "Car"

    return origin, destination, estimated_time, mode_of_transport

def display_trip_details(origin, destination, estimated_time, mode_of_transport):
    print("\nYour trip starts off in " + origin)
    print("And you are traveling to " + destination + "\n")
    print("You will be traveling by " + mode_of_transport)
    print("It will take approximately " + str(estimated_time) + " hours")

def check_weather_forecast(destination):
    
    weather_conditions = ["sunny", "cloudy", "rainy", "snowy"]
    forecast = random.choice(weather_conditions)
    print("\nThe weather forecast for your destination (" + destination + ") is: " + forecast)

def calculate_distance(origin, destination):
    distance = abs(len(origin) - len(destination)) * 1.5  # Assuming each unit represents 1.5 kilometers
    if estimated_time>10:
        print("Looks like a long drive, you should consider flying!")
    else:
        print("Drive isn't too long, you should be fine in a car.")

name = input("Welcome! Please enter your name: ")
trip_planner_welcome(name)
origin, destination, estimated_time, mode_of_transport = destination_setup()
estimated_time = estimated_time_rounded(estimated_time)


display_trip_details(origin, destination, estimated_time, mode_of_transport)


check_weather_forecast(destination)
calculate_distance(origin, destination)
print("Enjoy your trip!")
