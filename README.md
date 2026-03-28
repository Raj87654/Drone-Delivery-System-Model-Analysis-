# Intelligent Drone Delivery System

##  Project Overview

This project simulates an **AI-powered drone delivery system** that decides whether a delivery should be approved or rejected based on:

- Shortest route (Graph Algorithm)
- Battery consumption prediction (Machine Learning)
- Safety conditions (Machine Learning)
- Environmental & operational constraints

##  Key Features

### 1.  Shortest Path Optimization

- Uses **Dijkstra’s Algorithm**
- Finds the minimum distance between two locations

### 2. Battery Prediction Model

- Built using **Linear Regression**
- Predicts battery required based on:

  - Distance
  - Package weight
  - Wind conditions
  - Energy load (distance × weight)

### 3. Safety Classification Model

- Built using **Logistic Regression**
- Classifies delivery as:

  - Safe
  - Unsafe
- Based on:

  - Obstacle distance
  - Wind speed
  - Landing area size

### 4. Decision System

Combines all modules to make a final decision:

- Approves delivery if all conditions are satisfied
- Rejects delivery if:

  - Battery is insufficient
  - Unsafe landing conditions
  - High wind speed
  - Overweight package

## Technologies Used

- Python 
- NumPy
- Scikit-learn
- Heapq 
- Graph Algorithm

## Workflow

1. User inputs:

   - Start & End location
   - Package weight
   - Wind speed
   - Available battery
   - Obstacle distance
   - Area type

2. System performs:

   - Shortest path calculation
   - Battery prediction
   - Safety classification

3. Final Output:

   - Delivery Approved
   - Delivery Rejected 

## Example Output
DRONE DELIVERY ANALYSIS

Route: A → B → C
Distance: 8 km
Required Battery: 42.35 %
Available Battery: 60 %

FINAL RESULT:
Delivery Approved

##  How to Run

```bash
pip install numpy scikit-learn
python your_file_name.py
```

---

##  Future Enhancements

- Real-time map integration (Google Maps API)
- Live weather data integration
- Dynamic route optimization
- Web/App interface 
- Advanced AI models 


##  Author

**Rajkumar M**


