# Water Potability Prediction

## Problem Statement
Access to safe drinking water is essential for health, recognized as a basic human right and a key element in effective public health policy. Safe water can help reduce health care costs and promote economic benefits by lowering adverse health effects. This project aims to predict if water is safe for human consumption based on various chemical and physical properties.

## Project Goal
The goal of this project is to develop a predictive model to determine if water is safe (potable) or not based on specific water quality indicators.

## Features Used
The dataset includes the following features:
1. **pH**: pH level of the water (ranges from 0 to 14).
2. **Hardness**: Capacity of water to precipitate soap, measured in mg/L.
3. **Solids**: Total dissolved solids in ppm (parts per million).
4. **Chloramines**: Amount of chloramines in ppm.
5. **Sulfate**: Amount of sulfates dissolved in mg/L.
6. **Conductivity**: Electrical conductivity of water in µS/cm.
7. **Organic Carbon**: Amount of organic carbon in ppm.
8. **Trihalomethanes**: Amount of trihalomethanes in µg/L.
9. **Turbidity**: Measure of light-emitting property of water in NTU.
10. **Potability**: Label indicating if the water is safe for consumption (1 = Potable, 0 = Not Potable).

## Tasks
### Task 1: Predict Water Potability
Using the dataset features, this project aims to predict the potability of water. The outcome variable, `Potability`, is a binary label where:
- **1** indicates potable (safe for drinking),
- **0** indicates non-potable.

## Installation
To run this project, you’ll need to install the following libraries:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```
## Usage
1. **Clone the repository:**
```bash
git clone https://github.com/saivarshith123/water-potability-prediction.git
```
2. **Navigate to the project directory:**
```bash
cd water-potability-prediction
```
3. **Run the main script:**
```bash
python app.py
```
## Data Exploration & Visualization

The project includes data exploration steps to analyze the distribution and relationships among the features. Visualizations are provided to help understand patterns in potable vs. non-potable water.

## Model Training

Different machine learning models are trained and evaluated to predict water potability, including:

 - Logistic Regression
 - Decision Tree Classifier
 - Random Forest Classifier
 - Support Vector Machine (SVM)

The performance of each model is evaluated based on metrics such as accuracy, precision, recall, and F1-score.

# Results
The results are presented in terms of model accuracy, feature importance, and performance metrics for each model.

## Conclusion
The project demonstrates the potential for using data-driven approaches to assess water quality and predict its safety for consumption. Future work can focus on gathering more data and exploring additional features that may enhance prediction accuracy.

## License
This project is licensed under the MIT License.
