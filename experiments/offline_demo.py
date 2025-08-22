#!/usr/bin/env python3
"""
ClearML offline demo - runs without requiring API credentials
This will create local files and help us test the setup
"""

import os
import tempfile

def main():
    # Set ClearML to offline mode
    os.environ['CLEARML_API_HOST'] = ''
    os.environ['CLEARML_WEB_HOST'] = ''
    os.environ['CLEARML_FILES_HOST'] = ''
    
    from clearml import Task
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    
    print("🚀 Starting ClearML offline demo...")
    
    # Initialize ClearML task (will work offline)
    task = Task.init(
        project_name="Offline Demo",
        task_name="Random Forest Test",
        output_uri=tempfile.gettempdir()  # Save locally
    )
    
    print("✅ ClearML task initialized successfully!")
    
    # Create simple experiment
    print("📊 Running experiment...")
    X, y = make_classification(n_samples=500, n_features=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"🎯 Model accuracy: {accuracy:.2%}")
    
    # Log to ClearML
    task.get_logger().report_scalar("metrics", "accuracy", value=accuracy, iteration=0)
    
    print("✅ Experiment completed successfully!")
    print("📁 Check the temp directory for generated files")
    
    task.close()

if __name__ == "__main__":
    main()