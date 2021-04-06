# WareHouse-Locator

Mission Statement:
  We locate most efficient location for Warehouses of any company which have numerous Stores to reduce the cost of logistics and transport.
  We ask the User to input which city his store is available in and the number of warehouses he would like to set up and we do all the heavy lifting by calculating the distance between all the stores and using our Algorithm to produce the output.

Problem Statement of our Project:
  For given “N” number of cities, along with the distance between each pair of cities, we have to select “K” cities to place warehouses,
  such that the maximum distance of a city to a warehouse is minimized.
  Note: (K<N always)

Why Approximation Algorithum:
  We use the K-Centre Algorithm which works on the principle of Greedy Approach using an Approximation Algorithm.
  This is a NP-hard problem and to solve it would take lot of time/resources so we deploy this approach to find numerous warehouse locations.
  So we use this Approximation Algorithm to provide an accuracy of two times the optimal solution.
  
Algorithum:
    Lets start of K=3:
    a) Let the first arbitrarily picked vertex be store[0]. 
    b) The next vertex be the one which had a store farthest vertex from 0. 
    c) Calculate the distances from remaining cities from already selected warehouses . The greedy algorithm basically calculates following values. 
            Minimum of all distanced from remaining city[0] to already considered warehouses 
            Min[dist(remaining city[0], warehouse[0]), remaining (city[0], warehouse[1])]
            Repeat for remaining cities.
            After computing the above values, the city with the maximum value is picked. 
    Note that the greedy algorithm doesn’t give best solution for k = 2 as this is just an approximate algorithm with bound as twice of optimal. 

About our project:
  This is a django project and has one app named "user",
  Check our our user/views.py for the logic of our Algorithm.

Furthur Scope:
  Integrate it with Google Maps for more choices of ciies and better essimation of coordinates.
  Using  Euclidean distance to calculate distance between cities(Considering Earth as a sphere rather than a plane surface)
  
ScreenShots:
Django Admin App:
![alt text](https://github.com/J3rryPie/WareHouse-Locator/blob/master/MiniProject_SS/Admin_App.jpeg)

SignUp Page:
![alt text](https://github.com/J3rryPie/WareHouse-Locator/blob/master/MiniProject_SS/SignUp.jpeg)

All City Options:
![alt_text](https://github.com/J3rryPie/WareHouse-Locator/blob/master/MiniProject_SS/All_Cities.jpeg)

Input From User:
[!alt_text](https://github.com/J3rryPie/WareHouse-Locator/blob/master/MiniProject_SS/Input.jpeg)

Output:
[!alt_text](https://github.com/J3rryPie/WareHouse-Locator/blob/master/MiniProject_SS/Output.jpeg)

 
