  File Structure Overview：
1. main.py
The game controller that handles:

Player input & menu navigation

Day progression & energy management

Displaying daily status (temperature/radiation levels)

Calling appropriate functions from other files

2. planet.py
The alien world simulator that manages:

8 unique terrains (e.g. Crystal Plains, Lava Lakes)

24 base alien plants (3 per terrain)

Weather system (dynamic temperature/radiation)

Plant discovery during exploration

3. lab.py
The research lab handling:

Storing collected/hybrid plants

Breeding new hybrids from any two plants

Analyzing plant properties

Cataloging discoveries (with BASE/HYBRID labels)

  How They Work Together：
main.py orchestrates the game flow

planet.py provides the environment and plants

lab.py processes all scientific operations

All data persists within a single play session (no external files required)
