
# Mean Squared Error (MSE) — Applications

_Engineering Probability and Statistics – University of Tehran_

Use **mean squared error** to solve two classic estimation problems: fitting a **line** to data (linear regression) and finding a single **center point** for a 2D point cloud.

## Objectives
- Formulate MSE for a line $f(x)=ax+b$ and a center $c=(c_x,c_y)$.
- Derive the minimizers and verify them empirically.
- Visualize the fitted line and the estimated center.

## Tasks
1. **Define losses** — Write $\mathrm{MSE}_{\text{reg}}$ for the line and $\mathrm{MSE}_{\text{center}}$ for the point center.  
2. **Solve analytically** — Set gradients to zero to obtain $\hat a,\hat b$ and $\hat c=(\hat c_x,\hat c_y)$.  
3. **Implement & plot** — Compute the estimates in the notebook, plot data + fitted line, and points + center.  
4. **Quick checks** — Compare with a numerical optimizer and confirm $\hat c$ equals the coordinate-wise mean.

## License
This project is licensed under the **MIT License**.

## Acknowledgements
Developed under the supervision of **Dr. Tavassolipour**, **Dr. Vahabi**  
Designed by **Matin Bezrafshan**  
Supervisor: **Mehdi Jamalkhah**

