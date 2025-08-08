
# Binomial, Normal Distribution, and Continuity Correction

_Engineering Probability and Statistics – University of Tehran_

In this project, we explore the **Binomial Distribution**, its approximation using the **Normal Distribution**, and the application of **Continuity Correction**. The project is implemented using **R** and focuses on calculating probabilities for a product launch event.

The problem is based on the number of positive responses received from 1000 technology influencers invited to an event. The goal is to calculate the probability that no more than 430 people will attend, both using the Binomial Distribution and its Normal approximation.

## Objectives

- Use the **Binomial Distribution** to calculate the probability of receiving responses from 430 or fewer attendees.
- Approximate the probability using the **Normal Distribution** and compare it with the exact value.
- Apply **Continuity Correction** to improve the Normal approximation for discrete events.
- Calculate and analyze the relative error between the Binomial and Normal approximations.
- Determine the computational strategy for calculating CDF based on efficiency and error costs.

## Tasks

1. **Binomial CDF Calculation**:
   - Calculate the cumulative probability of 430 or fewer responses using the Binomial distribution.

2. **Normal Approximation**:
   - Approximate the probability using the Normal distribution and compute the relative error with respect to the Binomial result.

3. **Continuity Correction**:
   - Apply continuity correction to the Normal distribution to improve the approximation and compare the results.

4. **Graphical Comparison**:
   - Plot the cumulative distribution functions (CDF) for both the Binomial and Normal distributions, with and without continuity correction.

5. **Time Complexity Analysis**:
   - Analyze the computational time for calculating CDFs using both methods and identify the more efficient approach.

6. **Cost-Based Strategy**:
   - Given limited computational resources, determine a strategy for deciding when to use the **Binomial Distribution** and when to use the **Normal Distribution with Continuity Correction**. The strategy is based on the following:
     - **Computational cost**: 100 units per second for time.
     - **Error cost**: 106 units per unit error.
   - Calculate the time and error costs for calculating CDF for values of X in the range of 400 to 600, and determine the most cost-effective method for each case. 
   - Implement a function to find the first value of X for which the **Normal Distribution** becomes more efficient than the **Binomial Distribution**.

7. **Cost Comparison Graph**:
   - Plot the final cost differences (time vs error) for values of X in the range [400, 600] and identify the strategy to minimize computational cost while maintaining acceptable error rates.

## License

This project is licensed under the **MIT License**.

## Acknowledgements

Developed under the supervision of **Dr. Tavassolipour**, **Dr. Vahabi**  
Designed by **Soroush Esfahaniyan**  
Supervisor: **Mehdi Jamalkhah**

