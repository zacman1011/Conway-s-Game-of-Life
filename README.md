# Conway's Game of Life
My take on Conway's Game of Life simulation allows you to choose from 3 "boards" and 4 sets of "rules". To control which of these are used, give the appropriate command-line arguments.

## Boards
A board represents the available plain for the cells to live and move through. I have provided 3 boards: infinite, padded, wrap-around.

### Infinite board
As the name suggests, this allows the cells to grow into any space without being restricted by a border.

### Padded
This board has a finite space and will use, by default, a "dead" padding around the border that cells interact with when they reach the edge of the board. You may choose to use an alive border but this is not available via the command line.

### Wrap-around
Rather than a constant border around the board, the cells will simply teleport to the opposite side. ie: if a cell moves over the x boundary to width + 1 then it will actually be found at x = 0. This also applies to finding neighbours, which allows, for example, a glider to repeatedly go round and round the board.

## Rules
There are currently 4 sets of rules which determine how cells survive/spawn.

### Conway's
The classic Conway's Game of Life rules. 
 - If an alive cell has less than 2 neighbours, it dies. 
 - If an alive cell has 2 or 3 neighbours, it survives
 - If an alive cell has more than 3 neighbours, it dies.
 - If a dead cell has exactly 3 neighbours, it spawns.
 - All other dead cells remain dead

### Herd
The same idea as the classic rules, but requires more neighbours for each condition.
 - If an alive cell has less than 3 neighbours, it dies.
 - If an alive cell has 4, 5, or 6 neighbours, it survives.
 - If an alive cell has more than 6 neighbours, it dies.
 - If a dead cell has between 3 and 6 neighbours (inclusive), it spawns.
 - All other cells remain dead.

### Lone Wolf
Similarly, this takes its idea from the classic rules but requires fewer neighbours.
 - If any cell has 2 neighbours then it either survives or spawns.
 - If an alive cell has more than 3 neighbours, it dies.
 - All other dead cells remain dead.

### Roulette
This is the only non-deterministic set of rules available, and relies on probability to spawn or survive.
 - An alive cell has an 80% chance of surviving.
 - A dead cell has a neighbours/10 chance of spawning. Meaning dead spaces stay dead, but random additional cells may spawn near existing cells.

## Command line arguments
You may run a Game of Life from the command line by using the arguments listed below.

### File name (Required)
`--file_name initial_states/glider.csv`

This argument must be provided and be the location of a csv containing the starting coordinates of alive cells.

### Rules
`--rules conways`

Defaults to `conways`

Must be the name of a rule set to use:
 - conways
 - herd
 - lone_wolf
 - roulette

### Board
`--board infinite`

Defaults to `infinite`

Must be the name of a board to use:
 - infinite
 - padded_quad
 - wrap_around

### Height/Width
`--height 50`

`--width 50`

Defaults to `50` for both

The height and width that the board should be. Ignored for the infinite board.

### Maximum iterations
`--max_iterations 100`

Defaults to `100`

The maximum amount of iterations the simulation will run for. It will stop earlier if the board "dies" (no more alive cells).

