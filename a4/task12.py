from sklearn.datasets import fetch_covtype
from sklearn.model_selection import train_test_split

X, y = fetch_covtype(return_X_y=True)
X = X[:5000]
y = y[:5000]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

rf = RandomForestClassifier(random_state=42)

rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

acc = accuracy_score(y_test, y_pred)

print("Accuracy: ", acc)

from sklearn.model_selection import cross_val_score

scores = cross_val_score(
    rf, X_train, y_train, cv=3
)

print("CV Scores:", scores)
print("Mean CV Score:", scores.mean())

import ray

ray.shutdown()
ray.init(ignore_reinit_error=True)

from ray import tune
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

def train_rf(config):

    model = RandomForestClassifier(
        max_depth=config["max_depth"],
        n_estimators=config["n_estimators"],
        ccp_alpha=config["ccp_alpha"],
    )

    scores = cross_val_score(
        model, X_train, y_train, cv=3
    )

    tune.report({"mean_accuracy": scores.mean()})

search_space = {
    "max_depth": tune.grid_search([10, 20]),
    "n_estimators": tune.grid_search([50, 100]),
    "ccp_alpha": tune.grid_search([0.0])
}

tuner = tune.Tuner(
    train_rf,
    param_space=search_space
)

results = tuner.fit()

best_result = results.get_best_result(metric="mean_accuracy", mode="max")

print("Best config", best_result.config)
print("Best acc.", best_result.metrics["mean_accuracy"])