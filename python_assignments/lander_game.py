# Program: hw09_lander.py
# Purpose: A text-based game that emulates the Moon landing on a myriad of different planets/levels
# Author:  Tobias Safie - tks57@drexel.edu
# Date:    March 12, 2025

# Dictionary of levels
LEVELS = {
    "Sun": (-274.13, 50000),
    "Mercury": (-3.59, 1000),
    "Venus": (-8.87, 1000),
    "Earth": (-9.81, 5000),
    "Moon": (-1.622, 150),
    "Mars": (-3.77, 1000),
    "Jupiter": (-25.95, 1000),
    "Saturn": (-11.08, 1000),
    "Uranus": (-10.67, 1000),
    "Neptune": (-14.07, 1000),
    "Pluto": (-0.42, 1000),
    "Nibiru": (-543.00, 100000)}

def askFuel(currentFuel):
        try:
            fuel = int(input("Enter units of fuel to use: "))
            if fuel < 0:
                print("Cannot use negative amounts of fuel.")
            elif fuel > currentFuel:
                print(f"Not enough fuel. Max fuel: {currentFuel}")
            else:
                return fuel
        except:
            print("Value must be an integer.")

def playLevel(name, G, fuel):
    # Begin text chain for the simulation
    print(f"\nLanding on the {name}")
    print(f"Gravity is {G} m/s^2")
    print("Initial Altitude: 50 meters")
    print("Initial Velocity: 0.00 m/s")
    print("Burning a unit of fuel causes 0.10 m/s slowdown.")
    print(f"Initial Fuel Level: {fuel} units\n")
    print("GO")
    
    # Initialize variables
    altitude = 50
    velocity = 0
    time = 0
    T = 0.1  # Thruster acceleration per unit of fuel
    
    # Create the actual game loop
    while altitude > 0:
        print(f"After {time+1} seconds Altitude is {max(0, altitude):.2f} meters, velocity is {velocity:.2f} m/s.")
        print(f"Remaining Fuel: {fuel} units.")
        
        # Burn fuel, adjust velocity, adjust altitude, move time forward
        if altitude > 0:
            burn = askFuel(fuel)
            fuel -= burn
            velocity += G + (T * burn)
            altitude += velocity
            time += 1
    
    # Winning/losing condition
    if -2 <= velocity <= 2:
        print("Landed Successfully.")
    else:
        print("Crashed!")

if __name__ == "__main__":
    # Prints the menu
        print("\nSelect option to play level (or quit game)")
        # Iterates thru the list of planets/levels
        i = 0
        for planet in LEVELS.keys():
            print(f"{i}. {planet}")
            i += 1
        print("12. Quit")
        
        # Take user input and select that option
        try:
            choice = int(input("Enter Option: "))
            if choice == 12:
                print("Bye")
            elif choice in range(12):
                planet = list(LEVELS.keys())[choice]
                playLevel(planet, *LEVELS[planet])
            else:
                print("Invalid input.")
        except:
            print("Invalid input.")
