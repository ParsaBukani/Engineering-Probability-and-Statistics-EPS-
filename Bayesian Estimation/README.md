
  

# Bayesian Estimation — Beta–Bernoulli Updating

_Engineering Probability and Statistics – University of Tehran_

Estimate a coin’s head probability using Bayesian updating with a Beta prior and Bernoulli likelihood. Update the posterior after each toss, once with a **uniform prior** and again with **$  \text{Beta}(4,10) $**, then compare.
  

## Objectives

- Implement sequential posterior updates: prior $  \text{Beta}(\alpha,\beta) $, Bernoulli data.

- Report posterior mean, MAP, and a 95% credible interval at checkpoints.

- Compare the influence of priors as data accumulate.

  

## Tasks

1. **Model & Prior**: Define Bernoulli likelihood and start with $\mathrm{Beta}(1,1)$.
2. **Update Rule**: After each toss, $\alpha \leftarrow \alpha + \text{heads}$, $\beta \leftarrow \beta + \text{tails}$.
3. **Summaries**: At chosen steps, report $(\alpha,\beta)$, mean $\frac{\alpha}{\alpha+\beta}$, MAP $\frac{\alpha-1}{\alpha+\beta-2}$ (when valid), and a 95% CI.
4. **Alternative Prior**: Repeat using $\mathrm{Beta}(4,10)$; contrast trajectories and final estimates.
  

## License

This project is licensed under the **MIT License**.


## Acknowledgements

Developed under the supervision of **Dr. Tavassolipour**, **Dr. Vahabi**    
Designed by **Shahriar Attar**     
Supervisor: **Mehdi Jamalkhah**
