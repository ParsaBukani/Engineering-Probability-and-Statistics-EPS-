# Joint & Conditional Distributions — Queue System Simulation

_Engineering Probability and Statistics – University of Tehran_

This project analyzes a single-server queue where arrivals and services are **Poisson** (so inter-arrival and service times are **exponential**). Using the provided simulation output, you will study **marginal**, **joint**, and **conditional** behavior of key time variables and quantify linear dependence via correlation.

## Objectives
- Inspect the empirical distributions of `times_wait`, `times_arrival`, and `times_service`.
- Explore joint behavior with bivariate plots; interpret dependence vs. correlation.
- Form the derived variable `times_total` and explain its distributional shape.
- Compare conditional distributions to their marginals under an arrival-time constraint.

## Tasks
1. **Marginals**  
   Plot the distributions of `times_wait`, `times_arrival`, and `times_service` (e.g., `seaborn.histplot`). Explain what the **KDE** option (kernel density estimate) does and compare plots as you toggle/adjust it.

2. **Joint: `times_arrival` vs. `times_service`**  
   Use a joint plot (e.g., `seaborn.jointplot`) to visualize their joint distribution and comment on any apparent relationship.

3. **Joint: `times_wait` vs. `times_arrival`**  
   Repeat the joint analysis. From the plot alone, can you claim high correlation? Explain the limitation of visual judgment.

4. **Scatter & Correlation**  
   Draw a scatter plot for `times_wait` vs. `times_arrival` and compute the correlation coefficient; interpret its magnitude and sign.

5. **Derived Variable**  
   Compute `times_total` (e.g., `times_wait + times_service`) and analyze its distribution. Justify the observed shape using queueing intuition.

6. **Conditioning**  
   Obtain the distributions of `times_total` and `times_wait` **given** `times_arrival < 50` and compare them to the unconditional distributions.


## License
This project is licensed under the **MIT License**.

## Acknowledgements
Developed under the supervision of **Dr. Tavassolipour**, **Dr. Vahabi**  
Designed by **Shahriar Attar**  
Supervisor: **Mehdi Jamalkhah**

