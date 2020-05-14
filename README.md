# predicting_uber_driving_centers
# Introduction
The dataset consists of uber pickups on each and every day of July month in 2014 for NewYork city. Aim is to predict the 
optimal location for Uber Pickup points on each day so that time and money can be minimized.
# Installation
~~~
Clone this repo.
Open it in Jupyter Notebook.
Open the ipython notebook and run it.
~~~
# Logic Behind Prediction
Agglomerative clustering is applied on a small subset of dataset and the data points are clustered based on date of pickup and latitude,longitude of the pickup point as agglomerative  clustering can't be applied on a large dataset. Then k-nearest neighbour is applied to get the labels for all the remaining points.Hence we have clustered the data points.Then we draw a scatter plot with day on the x-axis and the label on the y-axis. We also the lat-long on x and y axis for each data label and by the use of all of these plots we can see on which day we have to place the driver at what place.
# Demo
![](https://github.com/HarshitNITT/predicting_uber_driving_centers/blob/master/images/demo_1.png)
![](https://github.com/HarshitNITT/predicting_uber_driving_centers/blob/master/images/demo_2.png)
![](https://github.com/HarshitNITT/predicting_uber_driving_centers/blob/master/images/demo_3.png)
![](https://github.com/HarshitNITT/predicting_uber_driving_centers/blob/master/images/demo_4.png)
![](https://github.com/HarshitNITT/predicting_uber_driving_centers/blob/master/images/demo_5.png)
![](https://github.com/HarshitNITT/predicting_uber_driving_centers/blob/master/images/demo_6.png)
![](https://github.com/HarshitNITT/predicting_uber_driving_centers/blob/master/images/demo_7.png)
![](https://github.com/HarshitNITT/predicting_uber_driving_centers/blob/master/images/demo_8.png)
![](https://github.com/HarshitNITT/predicting_uber_driving_centers/blob/master/images/demo_9.png)
# Languages
Python
# License
Project is licensed under MIT License.

