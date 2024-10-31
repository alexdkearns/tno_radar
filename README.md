General approach:
In terms of the system i am simulating there are three sub systems, the radar, IFF and firing unit.
Radar:
This comes as a csv of comma delimitted binaries (1 and 0s), this format is not ideal for working with the data
in terms of designing an efficient scanning algorithm. Therefore the data is formatted (i do this in the iff).
But essentially the radar part is just the csv and loading the csv.
The problem statement said however that there 20s in the simulation and there are 20 rows in the csv so i assume each row is one pulse/scan of the radar.

IFF:
The IFF should identify using the scan if there are hostile entities in the radar data. This is signified by there being more odd values (1s) than even values (0s).
First i format the radar scan data for the algorthim, i do this by first flattening the scan data and i create
a 1D Array of integers from the flattened string which was made from the row in the csv.

The algorthim i designed is O(n), you cannot improve on this i don't think as you must innevitably check all the entries in the radar data set before determining the number of evens and odds.
However i did some optimisations;
1) using a two pointer approach instead of simply looping through each sequential element in the array technically means the algorithm is O(n / 2) which simplifies to O(n) this doesn't change much with these small datasets but in reality the data would be quite large so this could impact efficiency.
2) Another small optimisation was only calculating the odds, since if you have the number of odds you can obtain the number of evens by simply subtracting the length of the array by the number of odds.

Firing unit:
The job of this is to simulate the missile once an hostile has been detected.
This is done by using a random number generator with a uniform distribution.
I use the Mersenne Twister algorthim, Coded by Takuji Nishimura and Makoto Matsumoto in c.
I customised the code slightly, what I did was add the initialiser to use the time package called on NULL which just uses the current time so it uses the current time as the seed (so it should be different everytime). It then initialises once and is not called again because any other number generated uses the previous random number as the seed for the next one.
To call this c code / functions in python you have to use ctypes to wrap the c functions and make them callable. To do this you also need to make a Cross-Platform
shared library. (needs to compile etc) however these are not cross system compatable therefore I added both the windows (i saw people at TNO with windows laptops) as well as the mac version. (I haven't tested if the windows one works because i don't have a windows machine). But basically it should check the system and use the correct library.
It then sets the return types (required since python is not a typed language and c is).
Then i call the initialise random function and then i simulate the engagement by comparing the pk to the random value generated. of course the number since it has a seed isn't truly random as are any random number generators.


Full Sim:
Then we bring this all together in the main simulator.
We first in the main call the function that opens the csv containing the radar data and
encode it.
Using the object from that we loop through each radar pulse/scan, use the IFF on the data.
This returns True or False booleans if there is a hostile or not.
If there is a hostile it prints tehre is a hostile detected and the missile has been launched.
It then simulates the engagement also returning True or False;
which prints to the console either that the target was neutralised or not depending on if the random number was equal or lower than the pk which is 0.8.

It simply returns no hostile detected if the IFF doesn't see a hostile then moves to the next radar pulse.
(Side note if there is a miss it also continues to the next radar pulse i.e. it doesn't keep firing until the enemy is destroyed but that was not in the problem statement so i assume it should just check the next radar pulse).

It then sleeps for a second which is the time between each radar pulse.

Testing:
To run the tests call:
PYTHONPATH=. pytest tests/

I unit tested the firing unit and iff with some edge cases etc. I wasn't extremely thorough but i think covered the main cases.
The simulator is a bit more of an integration test, i use pytest but i use unittest to mock the functions outputs i.e. if iff = True and simulator = True what would the simulator output, this is neccessary since there is random number generators you must mock these outputs otherwise the tests would randomly fail/pass depending on the random number.


I don't test the random number generator itself becuase this code seems reliably and is used on many papers / is heavily cited etc.