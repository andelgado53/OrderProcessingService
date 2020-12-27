#####
OrderProcessingService
#####

#####
How to run:
1. cd into folder ```cd ~/OrderProcessingService```
2. From that folder run ```python3 setup.py install --user```. This will install the packages so you can run the program. 
3. cd into ```cd ~/OrderProcessingService/app/src```
4. From src folder run ```python3 OrderService.py --tps 2 --orders ../data/orders.json > ../data/sample_out_put.txt```
this will run the program and will create a file with the output in the data folder.
5. To run all unittests cd into folder ```cd ~/OrderProcessingService/app/tst``` and run ```python3 -m unittest discover -p 'Test*'```
#####


#### Design Comments ####
1. How did I handle order flow between shelves when shelves were full:
    a. if there is space in the overflow shelf, orders goes into oveeflow.
    b. If overflow is full, I tried to find the first item in the overflow shelf that could be moved to its appropiate temp shelf.
    c. If above is not possible, I looked for the order in the oveflow shelf that was closest to expire and discarded it and then put the new order there.

2. I added enough unittests to show that all code should have coverage, but due to time considerations I did not include all possible tests. I created the ones I needed the most to prove that my code was correct.
3. Since drivers are concurrencly picking up orders as others get processed, the printing in the output might not necessarily followed a chronological order. 
4. I tried to add some TODOs in parts where I think code could be improved. 
5. I treated this project as a prototype for the system. Therefore I decided to use Python. For a production service, I would use a type safe language or would uses types in Python.
6. Please excuse any typos. 
