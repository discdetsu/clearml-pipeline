#!/usr/bin/env python3
"""
Simple ClearML demo without authentication
This creates a minimal experiment to test the setup
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def main():
    print("🚀 Running simple ML demo...")
    
    # Generate synthetic dataset
    print("📊 Generating synthetic dataset...")
    X, y = make_classification(
        n_samples=1000,
        n_features=20,
        n_informative=10,
        n_redundant=10,
        n_clusters_per_class=1,
        random_state=42
    )
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Test set size: {X_test.shape[0]}")
    
    # Train model
    print("🤖 Training Random Forest model...")
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    print(f"✅ Accuracy: {accuracy:.4f}")
    
    # Create feature importance plot
    feature_importance = model.feature_importances_
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(feature_importance)), feature_importance)
    plt.title('Feature Importance')
    plt.xlabel('Feature Index')
    plt.ylabel('Importance')
    
    # Save plot
    plot_path = "feature_importance.png"
    plt.savefig(plot_path)
    print(f"📈 Feature importance plot saved to: {plot_path}")
    plt.close()
    
    print("🎉 Demo completed successfully!")
    print(f"📊 Model accuracy: {accuracy:.2%}")
    print("\n💡 Next steps:")
    print("1. Generate API credentials in the ClearML web UI")
    print("2. Configure credentials in .env file")
    print("3. Run the full ClearML example with tracking")

if __name__ == "__main__":
    main()