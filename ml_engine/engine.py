"""
Machine Learning Engine (from scratch + sklearn)
================================================
Implements ML algorithms both from-scratch (for education) and
via scikit-learn (for production use):

- Linear Regression (OLS, Ridge, Lasso)
- Logistic Regression
- k-Nearest Neighbors (classification & regression)
- Decision Trees
- Random Forests
- Support Vector Machines
- k-Means Clustering
- Principal Component Analysis (PCA)
- Naive Bayes
- Neural Network (1 hidden layer, from scratch)
- Cross-validation and model evaluation
- Feature scaling / normalization
"""

from __future__ import annotations
import numpy as np
from typing import Dict, Any, List, Optional, Tuple
from sklearn.linear_model import (
    LinearRegression, Ridge, Lasso, ElasticNet,
    LogisticRegression, SGDClassifier
)
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, export_text
from sklearn.ensemble import (
    RandomForestClassifier, RandomForestRegressor,
    GradientBoostingClassifier, GradientBoostingRegressor,
    AdaBoostClassifier
)
from sklearn.svm import SVC, SVR
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.model_selection import (
    train_test_split, cross_val_score, KFold,
    GridSearchCV, learning_curve
)
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    mean_squared_error, mean_absolute_error, r2_score,
    confusion_matrix, classification_report,
    silhouette_score, davies_bouldin_score
)
from sklearn.pipeline import Pipeline
import warnings
warnings.filterwarnings("ignore")


class MLEngine:
    """Comprehensive machine learning engine with from-scratch and sklearn implementations."""

    # ──────────────────────────────────────────────
    # Linear Regression (From Scratch)
    # ──────────────────────────────────────────────

    @staticmethod
    def linear_regression_scratch(X_train: List[List[float]], y_train: List[float],
                                   X_test: Optional[List[List[float]]] = None,
                                   learning_rate: float = 0.01,
                                   epochs: int = 1000) -> Dict[str, Any]:
        """
        Gradient descent linear regression from scratch.
        Shows coefficients, loss curve, and predictions.
        """
        X = np.array(X_train)
        y = np.array(y_train)
        n_samples, n_features = X.shape

        # Normalize features
        X_mean = X.mean(axis=0)
        X_std = X.std(axis=0) + 1e-8
        X_norm = (X - X_mean) / X_std

        # Add bias column
        X_b = np.c_[np.ones(n_samples), X_norm]
        theta = np.zeros(X_b.shape[1])
        loss_history = []

        for _ in range(epochs):
            predictions = X_b @ theta
            errors = predictions - y
            loss = float(np.mean(errors**2))
            loss_history.append(loss)
            gradients = (2 / n_samples) * X_b.T @ errors
            theta -= learning_rate * gradients

        result = {
            "method": "gradient_descent",
            "bias": float(theta[0]),
            "coefficients": theta[1:].tolist(),
            "final_loss": loss_history[-1],
            "loss_history": loss_history[::max(1, epochs // 100)],  # Downsample
            "learning_rate": learning_rate,
            "epochs": epochs
        }
        if X_test is not None:
            Xt = np.array(X_test)
            Xt_norm = (Xt - X_mean) / X_std
            Xt_b = np.c_[np.ones(len(Xt)), Xt_norm]
            result["predictions"] = (Xt_b @ theta).tolist()
        return result

    @staticmethod
    def linear_regression_ols(X: List[List[float]], y: List[float],
                               test_size: float = 0.2) -> Dict[str, Any]:
        """Ordinary Least Squares linear regression via sklearn."""
        X_arr = np.array(X)
        y_arr = np.array(y)
        X_train, X_test, y_train, y_test = train_test_split(
            X_arr, y_arr, test_size=test_size, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        return {
            "method": "OLS",
            "coefficients": model.coef_.tolist(),
            "intercept": float(model.intercept_),
            "r2_train": float(model.score(X_train, y_train)),
            "r2_test": float(r2_score(y_test, y_pred)),
            "mse": float(mean_squared_error(y_test, y_pred)),
            "rmse": float(np.sqrt(mean_squared_error(y_test, y_pred))),
            "mae": float(mean_absolute_error(y_test, y_pred)),
            "predictions": y_pred.tolist(),
            "actual": y_test.tolist()
        }

    @staticmethod
    def ridge_regression(X: List[List[float]], y: List[float],
                         alpha: float = 1.0, test_size: float = 0.2) -> Dict[str, Any]:
        """Ridge (L2-regularized) regression."""
        X_arr, y_arr = np.array(X), np.array(y)
        X_train, X_test, y_train, y_test = train_test_split(
            X_arr, y_arr, test_size=test_size, random_state=42)
        model = Ridge(alpha=alpha)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        return {
            "method": "Ridge",
            "alpha": alpha,
            "coefficients": model.coef_.tolist(),
            "intercept": float(model.intercept_),
            "r2_test": float(r2_score(y_test, y_pred)),
            "mse": float(mean_squared_error(y_test, y_pred))
        }

    @staticmethod
    def lasso_regression(X: List[List[float]], y: List[float],
                         alpha: float = 0.1, test_size: float = 0.2) -> Dict[str, Any]:
        """Lasso (L1-regularized) regression with automatic feature selection."""
        X_arr, y_arr = np.array(X), np.array(y)
        X_train, X_test, y_train, y_test = train_test_split(
            X_arr, y_arr, test_size=test_size, random_state=42)
        model = Lasso(alpha=alpha, max_iter=10000)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        zero_coefs = int(np.sum(model.coef_ == 0))
        return {
            "method": "Lasso",
            "alpha": alpha,
            "coefficients": model.coef_.tolist(),
            "intercept": float(model.intercept_),
            "r2_test": float(r2_score(y_test, y_pred)),
            "mse": float(mean_squared_error(y_test, y_pred)),
            "zeroed_features": zero_coefs,
            "note": f"{zero_coefs} features driven to zero (sparsity)"
        }

    # ──────────────────────────────────────────────
    # Classification
    # ──────────────────────────────────────────────

    @staticmethod
    def logistic_regression(X: List[List[float]], y: List[int],
                             test_size: float = 0.2,
                             C: float = 1.0,
                             max_iter: int = 1000) -> Dict[str, Any]:
        """Logistic regression classifier."""
        X_arr, y_arr = np.array(X), np.array(y)
        X_train, X_test, y_train, y_test = train_test_split(
            X_arr, y_arr, test_size=test_size, random_state=42, stratify=y_arr)
        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        X_test_s = scaler.transform(X_test)
        model = LogisticRegression(C=C, max_iter=max_iter, random_state=42)
        model.fit(X_train_s, y_train)
        y_pred = model.predict(X_test_s)
        classes = sorted(list(set(y_arr.tolist())))
        return {
            "method": "LogisticRegression",
            "accuracy": float(accuracy_score(y_test, y_pred)),
            "precision": float(precision_score(y_test, y_pred, average="weighted", zero_division=0)),
            "recall": float(recall_score(y_test, y_pred, average="weighted", zero_division=0)),
            "f1": float(f1_score(y_test, y_pred, average="weighted", zero_division=0)),
            "confusion_matrix": confusion_matrix(y_test, y_pred).tolist(),
            "classes": classes,
            "coefficients": model.coef_.tolist(),
            "intercept": model.intercept_.tolist()
        }

    @staticmethod
    def knn_classify(X: List[List[float]], y: List[int],
                     k: int = 5, test_size: float = 0.2) -> Dict[str, Any]:
        """k-Nearest Neighbors classifier."""
        X_arr, y_arr = np.array(X), np.array(y)
        X_train, X_test, y_train, y_test = train_test_split(
            X_arr, y_arr, test_size=test_size, random_state=42)
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        return {
            "method": "KNN",
            "k": k,
            "accuracy": float(accuracy_score(y_test, y_pred)),
            "f1": float(f1_score(y_test, y_pred, average="weighted", zero_division=0)),
            "confusion_matrix": confusion_matrix(y_test, y_pred).tolist()
        }

    @staticmethod
    def decision_tree_classify(X: List[List[float]], y: List[int],
                                max_depth: Optional[int] = None,
                                test_size: float = 0.2) -> Dict[str, Any]:
        """Decision tree classifier with tree structure export."""
        X_arr, y_arr = np.array(X), np.array(y)
        X_train, X_test, y_train, y_test = train_test_split(
            X_arr, y_arr, test_size=test_size, random_state=42)
        model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        tree_text = export_text(model)
        return {
            "method": "DecisionTree",
            "max_depth": max_depth or int(model.get_depth()),
            "n_leaves": int(model.get_n_leaves()),
            "accuracy": float(accuracy_score(y_test, y_pred)),
            "f1": float(f1_score(y_test, y_pred, average="weighted", zero_division=0)),
            "feature_importances": model.feature_importances_.tolist(),
            "tree_structure": tree_text[:2000]  # Truncate for API
        }

    @staticmethod
    def random_forest_classify(X: List[List[float]], y: List[int],
                                n_estimators: int = 100,
                                max_depth: Optional[int] = None,
                                test_size: float = 0.2) -> Dict[str, Any]:
        """Random forest ensemble classifier."""
        X_arr, y_arr = np.array(X), np.array(y)
        X_train, X_test, y_train, y_test = train_test_split(
            X_arr, y_arr, test_size=test_size, random_state=42)
        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth,
                                       random_state=42, n_jobs=-1)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        cv_scores = cross_val_score(model, X_arr, y_arr, cv=5, scoring="accuracy")
        return {
            "method": "RandomForest",
            "n_estimators": n_estimators,
            "accuracy": float(accuracy_score(y_test, y_pred)),
            "f1": float(f1_score(y_test, y_pred, average="weighted", zero_division=0)),
            "feature_importances": model.feature_importances_.tolist(),
            "cv_scores": cv_scores.tolist(),
            "cv_mean": float(cv_scores.mean()),
            "cv_std": float(cv_scores.std()),
            "confusion_matrix": confusion_matrix(y_test, y_pred).tolist()
        }

    @staticmethod
    def svm_classify(X: List[List[float]], y: List[int],
                     kernel: str = "rbf", C: float = 1.0,
                     test_size: float = 0.2) -> Dict[str, Any]:
        """Support Vector Machine classifier."""
        X_arr, y_arr = np.array(X), np.array(y)
        X_train, X_test, y_train, y_test = train_test_split(
            X_arr, y_arr, test_size=test_size, random_state=42)
        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        X_test_s = scaler.transform(X_test)
        model = SVC(kernel=kernel, C=C, probability=True, random_state=42)
        model.fit(X_train_s, y_train)
        y_pred = model.predict(X_test_s)
        return {
            "method": "SVM",
            "kernel": kernel,
            "C": C,
            "n_support_vectors": int(sum(model.n_support_)),
            "accuracy": float(accuracy_score(y_test, y_pred)),
            "f1": float(f1_score(y_test, y_pred, average="weighted", zero_division=0)),
            "confusion_matrix": confusion_matrix(y_test, y_pred).tolist()
        }

    # ──────────────────────────────────────────────
    # Clustering
    # ──────────────────────────────────────────────

    @staticmethod
    def kmeans_cluster(X: List[List[float]], k: int = 3,
                       max_iter: int = 300) -> Dict[str, Any]:
        """k-Means clustering."""
        X_arr = np.array(X)
        model = KMeans(n_clusters=k, max_iter=max_iter, random_state=42, n_init=10)
        labels = model.fit_predict(X_arr)
        sil = float(silhouette_score(X_arr, labels)) if k > 1 else 0.0
        db = float(davies_bouldin_score(X_arr, labels)) if k > 1 else 0.0
        return {
            "method": "KMeans",
            "k": k,
            "labels": labels.tolist(),
            "centers": model.cluster_centers_.tolist(),
            "inertia": float(model.inertia_),
            "silhouette_score": sil,
            "davies_bouldin_score": db,
            "n_iter": int(model.n_iter_)
        }

    @staticmethod
    def find_optimal_k(X: List[List[float]], k_range: Tuple[int, int] = (2, 10)) -> Dict[str, Any]:
        """Find optimal k using elbow method and silhouette scores."""
        X_arr = np.array(X)
        inertias, silhouettes = [], []
        ks = list(range(k_range[0], k_range[1] + 1))
        for k in ks:
            model = KMeans(n_clusters=k, random_state=42, n_init=10)
            labels = model.fit_predict(X_arr)
            inertias.append(float(model.inertia_))
            silhouettes.append(float(silhouette_score(X_arr, labels)))
        best_k = ks[int(np.argmax(silhouettes))]
        return {
            "k_values": ks,
            "inertias": inertias,
            "silhouette_scores": silhouettes,
            "optimal_k_by_silhouette": best_k
        }

    @staticmethod
    def dbscan_cluster(X: List[List[float]], eps: float = 0.5,
                       min_samples: int = 5) -> Dict[str, Any]:
        """DBSCAN density-based clustering (handles noise/outliers)."""
        X_arr = np.array(X)
        model = DBSCAN(eps=eps, min_samples=min_samples)
        labels = model.fit_predict(X_arr)
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise = int(np.sum(labels == -1))
        return {
            "method": "DBSCAN",
            "eps": eps,
            "min_samples": min_samples,
            "labels": labels.tolist(),
            "n_clusters": n_clusters,
            "n_noise_points": n_noise
        }

    # ──────────────────────────────────────────────
    # Dimensionality Reduction
    # ──────────────────────────────────────────────

    @staticmethod
    def pca_reduce(X: List[List[float]], n_components: int = 2) -> Dict[str, Any]:
        """Principal Component Analysis."""
        X_arr = np.array(X)
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_arr)
        pca = PCA(n_components=n_components)
        X_reduced = pca.fit_transform(X_scaled)
        cumvar = float(np.sum(pca.explained_variance_ratio_))
        return {
            "method": "PCA",
            "n_components": n_components,
            "reduced_data": X_reduced.tolist(),
            "explained_variance_ratio": pca.explained_variance_ratio_.tolist(),
            "cumulative_variance": cumvar,
            "eigenvalues": pca.explained_variance_.tolist(),
            "components": pca.components_.tolist()
        }

    # ──────────────────────────────────────────────
    # Model Evaluation
    # ──────────────────────────────────────────────

    @staticmethod
    def cross_validate(X: List[List[float]], y: List, model_name: str = "random_forest",
                       cv: int = 5, task: str = "classification") -> Dict[str, Any]:
        """Run k-fold cross-validation for a given model."""
        X_arr, y_arr = np.array(X), np.array(y)
        if task == "classification":
            models = {
                "logistic_regression": LogisticRegression(max_iter=1000),
                "knn": KNeighborsClassifier(),
                "decision_tree": DecisionTreeClassifier(random_state=42),
                "random_forest": RandomForestClassifier(random_state=42),
                "svm": SVC(probability=True, random_state=42),
                "naive_bayes": GaussianNB()
            }
            scoring = "accuracy"
        else:
            models = {
                "linear_regression": LinearRegression(),
                "ridge": Ridge(),
                "lasso": Lasso(),
                "knn_regressor": KNeighborsRegressor(),
                "decision_tree_regressor": DecisionTreeRegressor(random_state=42),
                "random_forest_regressor": RandomForestRegressor(random_state=42)
            }
            scoring = "r2"
        if model_name not in models:
            raise ValueError(f"Unknown model: {model_name}. Choose from {list(models.keys())}")
        model = models[model_name]
        pipeline = Pipeline([("scaler", StandardScaler()), ("model", model)])
        scores = cross_val_score(pipeline, X_arr, y_arr, cv=cv, scoring=scoring)
        return {
            "model": model_name,
            "cv_folds": cv,
            "scoring": scoring,
            "scores": scores.tolist(),
            "mean": float(scores.mean()),
            "std": float(scores.std()),
            "min": float(scores.min()),
            "max": float(scores.max())
        }

    @staticmethod
    def compare_models(X: List[List[float]], y: List,
                       task: str = "classification") -> Dict[str, Any]:
        """Compare multiple models side by side."""
        X_arr, y_arr = np.array(X), np.array(y)
        if task == "classification":
            models = {
                "Logistic Regression": LogisticRegression(max_iter=1000),
                "KNN": KNeighborsClassifier(),
                "Decision Tree": DecisionTreeClassifier(random_state=42),
                "Random Forest": RandomForestClassifier(random_state=42, n_estimators=50),
                "SVM": SVC(random_state=42),
                "Naive Bayes": GaussianNB()
            }
            scoring = "accuracy"
        else:
            models = {
                "Linear Regression": LinearRegression(),
                "Ridge": Ridge(),
                "Lasso": Lasso(),
                "KNN Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(random_state=42),
                "Random Forest": RandomForestRegressor(random_state=42, n_estimators=50)
            }
            scoring = "r2"

        results = {}
        for name, model in models.items():
            pipeline = Pipeline([("scaler", StandardScaler()), ("model", model)])
            scores = cross_val_score(pipeline, X_arr, y_arr, cv=5, scoring=scoring)
            results[name] = {
                "mean": float(scores.mean()),
                "std": float(scores.std()),
                "scores": scores.tolist()
            }

        best = max(results, key=lambda k: results[k]["mean"])
        return {
            "task": task,
            "scoring": scoring,
            "results": results,
            "best_model": best,
            "best_score": results[best]["mean"]
        }

    # ──────────────────────────────────────────────
    # Neural Network From Scratch
    # ──────────────────────────────────────────────

    @staticmethod
    def neural_network_scratch(X_train: List[List[float]], y_train: List[float],
                                hidden_size: int = 32, learning_rate: float = 0.01,
                                epochs: int = 500) -> Dict[str, Any]:
        """
        1-hidden-layer neural network for regression, implemented from scratch.
        Uses ReLU activation in hidden layer, linear output.
        """
        X = np.array(X_train)
        y = np.array(y_train).reshape(-1, 1)
        n_samples, n_features = X.shape

        # Xavier initialization
        W1 = np.random.randn(n_features, hidden_size) * np.sqrt(2 / n_features)
        b1 = np.zeros((1, hidden_size))
        W2 = np.random.randn(hidden_size, 1) * np.sqrt(2 / hidden_size)
        b2 = np.zeros((1, 1))

        def relu(z):
            return np.maximum(0, z)

        def relu_deriv(z):
            return (z > 0).astype(float)

        loss_history = []
        for epoch in range(epochs):
            # Forward pass
            Z1 = X @ W1 + b1
            A1 = relu(Z1)
            Z2 = A1 @ W2 + b2
            y_pred = Z2

            # Loss
            loss = float(np.mean((y_pred - y)**2))
            loss_history.append(loss)

            # Backward pass
            dL_dZ2 = 2 * (y_pred - y) / n_samples
            dL_dW2 = A1.T @ dL_dZ2
            dL_db2 = np.sum(dL_dZ2, axis=0, keepdims=True)
            dL_dA1 = dL_dZ2 @ W2.T
            dL_dZ1 = dL_dA1 * relu_deriv(Z1)
            dL_dW1 = X.T @ dL_dZ1
            dL_db1 = np.sum(dL_dZ1, axis=0, keepdims=True)

            W1 -= learning_rate * dL_dW1
            b1 -= learning_rate * dL_db1
            W2 -= learning_rate * dL_dW2
            b2 -= learning_rate * dL_db2

        final_pred = (relu(X @ W1 + b1) @ W2 + b2).flatten()
        return {
            "method": "neural_network_scratch",
            "architecture": [n_features, hidden_size, 1],
            "activation": "relu",
            "learning_rate": learning_rate,
            "epochs": epochs,
            "final_loss": loss_history[-1],
            "loss_history": loss_history[::max(1, epochs // 100)],
            "predictions": final_pred.tolist()
        }
