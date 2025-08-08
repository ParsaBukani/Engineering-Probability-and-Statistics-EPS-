
# Sample Means & the Central Limit Theorem

_Engineering Probability and Statistics – University of Tehran_

Empirically examine the **CLT** using three parents: Poisson$(\lambda=10)$, Exponential$(\lambda=\tfrac12)$, Geometric$(p=\tfrac15)$.

## Objectives
- Compare sampling distributions of $\bar X$ to normal overlays.
- Track how $E[\bar X]$ and $\mathrm{SE}(\bar X)=\sigma/\sqrt{n}$ evolve with $n$.
- Test a **mixture** setting where the parent distribution varies per replication.

## Tasks
1. **Theory** — Report each parent’s mean/variance (note your geometric parameterization).  
2. **Sampling** — For each parent and $n\in\{30,300,3000\}$, run 1000 samples; histogram $\bar X$ with a common bin width.  
3. **Summaries** — For each case, report empirical $E[\bar X]$ and $\mathrm{SE}(\bar X)$; compare to $E[\bar X]=\mu$, $\mathrm{SE}=\sigma/\sqrt{n}$.  
4. **Normal overlay** — Add $\mathcal N(\mu,\sigma/\sqrt{n})$ curves to the histograms and comment on fit vs. $n$.  
5. **Mixture** — At each replication, randomly choose one parent, sample size $n$, record $\bar X$; repeat for the three $n$’s, plot histograms, and report $E[\bar X]$, $\mathrm{SE}(\bar X)$. 

## License
This project is licensed under the **MIT License**.

## Acknowledgements
Developed under the supervision of **Dr. Tavassolipour**, **Dr. Vahabi**  
Designed by **Matin Bezrafshan**  
Supervisor: **Mehdi Jamalkhah**

