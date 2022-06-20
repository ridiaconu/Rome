# Rome

Rome is a Python application that calculates the shortest optimal route between two cities on a map.

# Prerequisites

We will consider two friends, living in two separate cities from Romania.

The map below will serve as a reference for the distances and routes.

![image](https://user-images.githubusercontent.com/77971744/174643007-83caed6a-1d83-4b82-b334-8cb77b6a41e6.png)

The two friends will try to reach one another using the shortest optimal route between their hometowns, meeting halfway through.

# Functionality and Output

The application will read from the samples.json file an interpretation of the map presented above. Then it will randomly choose two cities from the map and will compute the shortest optimal path between those cities using a modified version of Yen's Algorithm.
At the end of its execution it will print in the terminal the distance between the two cities, the time cost of that particular route and the point the two friends will meet halfway through, along with an explicitation of the route.
