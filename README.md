<h3>Car price prediction App</h3>

<h6>Deployment</h6>
<p>https://car-price-predict-flask.herokuapp.com/</p>




<h6>App</h6>
<p>A simple flask web app that predict the prices
Of fairly used cars in Nigeria using machine learning.</p>

<h6>Data</h6>
5700+ datapoints were used to train the model.The data was scraped from 3 sites 
   <ul>
     <li> https://carmart.ng/ </li>
     <li>https://deals.jumia.com.ng/cars   </li>
     <li>https://buy.cars45.com/cars</li>
   </ul>
The categorical values were label encoded and their numerical values were the "value" in their "option" tag.

<h6>Model</h6>
 <p>Sklearn's Gradient boosting regressor with a:</p><br>
 <p>Max depth:6</p><p>Max Features:5</p><p>Learning rate:0.025<p><p>n_estimators:1200</p>
 <p>The model gave a mean_absolute_error of ≈590 Thousand Naira on the data I tested it on</p>

<h6>Challenges</h6>
 <p>Data collection: There were different features used to describe the cars in the different sites I got the data from, only about 6 were common among them, the mileage, the car's year of production, the location of the seller of the car, the car's make, transmission and the car's model</p>
