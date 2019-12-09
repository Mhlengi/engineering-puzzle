# Engineering Puzzle
## Instructions
We will give priority consideration to candidates supplying a pragmatic solution to the following puzzle:

A Census puts populations of 26 largest US metro areas at:

18897109, 12828837, 9661105, 6371773, 5965343, 5926800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279933, 3095213, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, and 2134411.

Can you find a subset of these areas where a total of exactly 101000000 people live, assuming the census estimates are exactly right?

- Given a sum total value and list of integers, we need to find a subset of combinations if we sum them, they sum up to the given total sum value.
- The function in python module `engineering_puzzle.py` does compute the expected results. 

## Requirements
- Python 3+

## Demonstration
- To demonstrate or see the final result, you need to follow these instructions
- Clone/Download a project `git clone https://github.com/Mhlengi/engineering-puzzle.git`
- Install python3 `brew install python3`
- Install pip3 `pip3 install virtualenv`
- Create virtual environment: `virtualenv -p python3 venv`
- Activate a virtual environment: `. venv/bin/activate`
- Navigate to source in such a way that you can see `engineering_puzzle.py` file
- Then run the following command.
- `python engineering_puzzle.py`
- If everything work as expected,
- Given input list and total exactly value  
``
list = [18897109, 12828837, 9661105, 6371773, 5965343, 5926800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279933, 3095213, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, 2134411]
total_exactly_value = 101000000
``
- The following data subset should be printed in your terminal as follows.
```
(18897109, 12828837, 9661105, 6371773, 5926800, 5582170, 5564635, 4552402, 4296250, 4224851, 3279933, 3095213, 2812896, 2710489, 2543482, 2226009, 2149127, 2142508, 2134411)
```
## Running unittest cases
- `python test_engineering_puzzle.py `
