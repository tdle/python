# Python

My Python learning journey. 

I am currently working on a task which will help me apply what I've learnt in Python so far to a real world application.

# The Task

The task is to take the data.csv file and transform it into a new format. Details shown below...

### Data.csv file

Hierarchy | Dept | Emp | Alpha | Bravo | Charlie | 01/01/2018 | 08/01/2018 |
----------|------|-----|-------|-------|---------|------------|------------|
Hierahcy 1| Dept 1 | JC | h | o | l | 0 | 2

# Desired Output
### new_data.csv

Hierarchy | Dept | Emp | Alpha | Bravo | Charlie | Date | Value |
----------|------|-----|-------|-------|---------|------|-------|
Hierahcy 1| Dept 1 | JC | h | o | l | 01/01/2018 | 0 
Hierahcy 1| Dept 1 | JC | h | o | l | 08/01/2018 | 2 

I'd like to capture the two dates, '01/01/2018' and 08/01/2018 into a new column called 'Date'.

I then want to place the values '0' and '2' next to the date they were originally assigned to in a new column called 'Value'.

Currently, I have explored, Pandas, and the `.melt()` method. 
