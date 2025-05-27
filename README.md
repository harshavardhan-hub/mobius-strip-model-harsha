# Mobius Strip Modeling Assignment

## 🔷 Description

This Python script models a Mobius strip using parametric equations. It numerically estimates:

- The **surface area** using cross product integration
- The **edge length** by summing distances between edge points
- A **3D plot** visualizing the strip

## 📌 Parametric Equations Used

x(u,v) = (R + v * cos(u/2)) * cos(u)

y(u,v) = (R + v * cos(u/2)) * sin(u)

z(u,v) = v * sin(u/2)


## 🔧 How to Run

1. Make sure you have Python and the required libraries:
    ```bash
    pip install numpy matplotlib
    ```

2. Run the script:
    ```bash
    python mobius_strip.py
    ```

3. Output:
    - Surface Area printed
    - Edge Length printed
    - 3D Möbius strip displayed

## 📊 Outputs

- Example Output:
Estimated Surface Area: 1.8845
Estimated Edge Length: 12.6340


- A 3D visualization will also appear in a new window.

## ✍️ Author
Harsha Vardhan Yanakandla (Assignment)
