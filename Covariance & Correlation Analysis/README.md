
# Covariance & Correlation Analysis — Energy Consumption

_Engineering Probability and Statistics – University of Tehran_

Analyze hourly electricity consumption across selected U.S. states (2004–2018) to explore dispersion, seasonality, and linear dependence. Then examine whether correlation implies causation using an auxiliary dataset.

## Objectives
- Parse and enrich datetime fields (year, month, hour) and visualize dispersion with boxplots.
- Quantify correlations for targeted time windows and seasons.
- Interpret correlations in context and evaluate causality claims on a separate dataset.



## Tasks
1. **Datetime prep** — Convert `Datetime` to a datetime type; add **Year**, **Month**, **Hour** columns.
2. **Boxplots** — Plot consumption by **Year**, **Hour**, **Month**. From the yearly plot, state whether variance in **2004** exceeds **2005** (justify briefly).
3. **Targeted correlations** — Compute **Pearson correlation ($r$)**:
   - `consumption` vs **Hour** for hours **4–13** (inclusive); compare with the hourly boxplot.
   - `consumption` vs **Month** for **2–4** and for **10–12** (each subset separately); interpret sign and magnitude relative to seasons.
4. **Correlation ≠ causation** — Load `Physician_LE_TV`, compute a numeric correlation matrix, note any high $|r|$ pairs, and explain why these do **not** imply causality.



## License
This project is licensed under the **MIT License**.

## Acknowledgements

Developed under the supervision of **Dr. Tavassolipour**, **Dr. Vahabi**   
Designed by **Shahriar Attar**   
Supervisor: **Mehdi Jamalkhah**
