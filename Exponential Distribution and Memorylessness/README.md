# Exponential Distribution and Memorylessness

_Engineering Probability and Statistics – University of Tehran_

This project explores the **Exponential Distribution**, specifically focusing on its memoryless property. The project simulates customer arrival times in a store, based on the assumption that the time between arrivals follows an **Exponential Distribution**. The goal is to test whether the claim that "if no customers have arrived in the last 12 minutes, a new customer is likely to arrive soon" holds true.

The project is implemented in **R**, with a focus on simulation, hypothesis testing, and comparison of empirical and theoretical results.

## Objectives

- Simulate the time between customer arrivals using the **Exponential Distribution**.
- Implement functions to calculate the waiting times after a 12-minute gap and analyze the results.
- Compare the simulated results with the theoretical expectations based on the **memoryless property** of the Exponential Distribution.
- Test the validity of the claim that the likelihood of a customer arriving after 12 minutes is higher than expected.

## Tasks

1. **Simulate Exponential Distribution**:
   - Implement a function that generates exponential random variables given the rate parameter and the number of samples.
   - This function models the time between customer arrivals.

2. **Time After 12 Minutes**:
   - Implement a function to extract the times after a 12-minute gap from the simulated customer arrival times.
   - Ensure that the times are bounded by the store's working hours (8 hours per day).

3. **Histogram and Comparison**:
   - Plot the histogram of customer arrival times after 12 minutes and compare it with the histogram of the Exponential Distribution.
   - Calculate and visualize the means of both distributions.

4. **Hypothesis Testing**:
   - Based on the plotted histograms and the properties of the Exponential Distribution, discuss whether the claim about customer arrivals after 12 minutes is valid.

5. **Probability Calculation**:
   - Calculate the probability that, after 12 minutes, a new customer will arrive within the next 15 minutes using both simulation and theoretical approaches.

## License

This project is licensed under the **MIT License**.

## Acknowledgements

Developed under the supervision of **Dr. Tavassolipour**, **Dr. Vahabi**  
Designed by **Soroush Esfahaniyan**  
Supervisor: **Mehdi Jamalkhah**

