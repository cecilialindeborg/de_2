import time
import ray
from ray import tune
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier

X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

rf_default = RandomForestClassifier(n_estimators=5)
print("Default params:", rf_default.get_params())

default_scores = cross_val_score(rf_default, X_train, y_train, cv=2)
print("Default CV:", default_scores.mean())

def train_rf(config):
    model = RandomForestClassifier(
        max_depth=config["max_depth"],
        n_estimators=config["n_estimators"],
        ccp_alpha=config["ccp_alpha"],
    )
    scores = cross_val_score(model, X_train, y_train, cv=2)
    tune.report({"mean_accuracy": scores.mean()})

search_space = {
    "max_depth": tune.grid_search([5, 10]),
    "n_estimators": tune.grid_search([5, 10]),
    "ccp_alpha": tune.grid_search([0.0, 0.001]),
}

ray.init()

start = time.time()

tuner = tune.Tuner(train_rf, param_space=search_space)
results = tuner.fit()

print("Time:", time.time() - start)

best = results.get_best_result(metric="mean_accuracy", mode="max")
print("Best config:", best.config)
print("Best score:", best.metrics["mean_accuracy"])