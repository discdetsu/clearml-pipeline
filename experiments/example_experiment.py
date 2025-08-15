#!/usr/bin/env python3
"""
Example ClearML experiment script
This demonstrates basic ClearML functionality for experiment tracking
"""

from clearml import Task, Logger
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def main():
    # Initialize ClearML task
    task = Task.init(
        project_name="ClearML Pipeline Demo",
        task_name="Random Forest Classification Example"
    )
    
    # Get logger for metrics and plots
    logger = Logger.current_logger()
    
    # Hyperparameters
    params = {
        'n_samples': 1000,
        'n_features': 20,
        'n_informative': 10,
        'n_redundant': 10,
        'n_clusters_per_class': 1,
        'random_state': 42,
        'n_estimators': 100,
        'max_depth': 10,
        'test_size': 0.2
    }
    
    # Connect parameters to ClearML
    task.connect(params)
    
    print("Generating synthetic dataset...")
    # Generate synthetic dataset
    X, y = make_classification(
        n_samples=params['n_samples'],
        n_features=params['n_features'],
        n_informative=params['n_informative'],
        n_redundant=params['n_redundant'],
        n_clusters_per_class=params['n_clusters_per_class'],
        random_state=params['random_state']
    )
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=params['test_size'], random_state=params['random_state']
    )
    
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Test set size: {X_test.shape[0]}")
    
    # Train model
    print("Training Random Forest model...")
    model = RandomForestClassifier(
        n_estimators=params['n_estimators'],
        max_depth=params['max_depth'],
        random_state=params['random_state']
    )
    
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")
    
    # Log metrics to ClearML
    logger.report_scalar("Performance", "Accuracy", value=accuracy, iteration=0)
    
    # Feature importance plot
    feature_importance = model.feature_importances_
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(feature_importance)), feature_importance)
    plt.title('Feature Importance')
    plt.xlabel('Feature Index')
    plt.ylabel('Importance')
    
    # Report plot to ClearML
    logger.report_matplotlib_figure(
        title="Feature Importance",
        series="Random Forest",
        figure=plt.gcf(),
        iteration=0
    )
    
    # Log classification report
    report = classification_report(y_test, y_pred)
    print("Classification Report:")
    print(report)
    
    # Save model artifact (ClearML will automatically track this)
    print("Experiment completed successfully!")
    print(f"View results at: http://localhost:8080")

if __name__ == "__main__":
    main()