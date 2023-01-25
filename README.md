# Brief Summary of the project.
>This project is basically created to calculate the import duty of motor vehicles in Kenya. It computes and returns a complete breakdown of each cost involved in importing a motor vehiccle in the country.

## What problem does the problem adsress?
>Different taxes and duties are involved when it comes to importation of motor vehicles in any country. The mathematics and calculations involved can be fairly to get right especially for people who daily activities doent revolve around accounts and finance.
>
>Even to guys working in accounts and finance departments, it would be hectic to compute for the taxes and levies using a pen, book and calculator as it also increases the margin of error significantly moreso when a large number of cars is involved.
>
>The app seeks to helps potential car owners compute for expected import duty if they seek to import a car listed on the websites of overseas car dealers. Potential car owners often find themselves having to contact finance specialists to compute them what it would cost if they were to import a certain car. The app will also make work easier and efficient for financial experts in the car industry.

## How does the app work?
>The image below is what comes up as the front page once the app is opened.
>
![image](https://user-images.githubusercontent.com/121600705/214526083-1a3cacdd-cbbd-4c4e-b126-a8a2a996841b.PNG)
>On the sidebar, the user will thereby eneter the price of the vehicle (CIF) in USD and its engine size in cc.
The app will first convert the CIF from USD to KES using real time exchange rates from an exchange rate API.
It will tereafter compute for all other taxes and levies included then return every one of them plus a row for total taxes and the last one for CIF plus total taxes as shown below.
>
![image 2](https://user-images.githubusercontent.com/121600705/214528698-2745919e-4477-4364-821c-ecf1fe2b742d.PNG)
## Visualization
After the calculations, the app will display an horizontal bar chart comparing the total cost + duties to CIF and duties of importing the vehicle as shown. This provides the user with a visual and numeric representation the total amount of importing the car and how much of it will go to taxes.
>
![image3](https://user-images.githubusercontent.com/121600705/214530335-7755b035-4a6a-43ba-816d-a103909aedf1.PNG)

