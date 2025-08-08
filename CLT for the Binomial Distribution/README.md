
# CLT for the Binomial Distribution

_Engineering Probability and Statistics – University of Tehran_

Use the **Central Limit Theorem** to approximate a Binomial distribution and compare exact vs. normal-based results.

## Objectives
- Visualize and standardize a Binomial distribution.
- Align a continuous normal curve with a discrete PMF using a Riemann-sum scale.
- Quantify approximation quality on point and interval probabilities.

## Tasks
1. **Exact PMF** — Plot Binomial with $n=270$, $p=0.3$ over all feasible $k$.
2. **Standardization** — Transform $x \mapsto z=\frac{x-np}{\sqrt{np(1-p)}}$ and re-plot the standardized PMF.
3. **Normal overlay** — Add $\mathcal N(0,1)$ to the standardized plot; comment on the visual fit.
4. **Why bars don’t sum to 1 in $z$-space?** — Compute the total of the standardized-bar heights and explain why it $\neq 1$.
5. **Riemann scaling** — Compute a scale factor via $\int_a^b f(x)\,dx \approx \tfrac{b-a}{N}\sum_{i=0}^{N} f(x_i)$ to align the normal curve with the discrete grid; report the factor and $\sqrt{np(1-p)}$. Re-plot Binomial and (scaled) Normal together; verify the fix.
6. **Point probability** — Estimate $P(X=55)$ using:  
   (i) exact Binomial, (ii) CLT-based Normal with your scaling. Compare.
7. **Interval probability** — Using the CLT result $\displaystyle \lim_{n\to\infty} P\!\left(a \le \frac{S_n-np}{\sqrt{np(1-p)}} \le b\right)=\int_a^b \phi(x)\,dx$, approximate $P(40\le X\le 60)$ and discuss accuracy.

## License
This project is licensed under the **MIT License**.

## Acknowledgements
Developed under the supervision of **Dr. Tavassolipour**, **Dr. Vahabi**  
Designed by **Matin Bezrafshan**  
Supervisor: **Mehdi Jamalkhah**

