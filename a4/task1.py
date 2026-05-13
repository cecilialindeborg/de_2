from sklearn.datasets import fetch_covtype
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import ray
from ray import tune
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

print("Starting task1.py")
X, y = fetch_covtype(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

rf = RandomForestClassifier(random_state=42)
params = rf.get_params()
print("Parameters:", params)

rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

acc = accuracy_score(y_test, y_pred)

print("Accuracy: ", acc)

scores = cross_val_score(
    rf, X_train, y_train, cv=3
)

print("CV Scores:", scores)
print("Mean CV Score:", scores.mean())

# ray.shutdown()
# ray.init(address="auto")

# X_train_ref = ray.put(X_train)
# y_train_ref = ray.put(y_train)

# def train_rf(config):
#     X_train_local = ray.get(X_train_ref)
#     y_train_local = ray.get(y_train_ref)

#     model = RandomForestClassifier(
#         max_depth=config["max_depth"],
#         n_estimators=config["n_estimators"],
#         ccp_alpha=config["ccp_alpha"],
#         n_jobs=1
#     )

#     scores = cross_val_score(
#         model, X_train_local, y_train_local, cv=3, n_jobs=1
#     )

#     tune.report(cv_score=scores.mean())

# search_space = {
#     "max_depth": tune.grid_search([10, 20]),
#     "n_estimators": tune.grid_search([50, 100]),
#     "ccp_alpha": tune.grid_search([0.0])
# }

# tuner = tune.Tuner(
#     train_rf,
#     param_space=search_space
# )

# results = tuner.fit()
# best_result = results.get_best_result(metric="cv_score", mode="max")

# print("Best config", best_result.config)
# print(best_result.metrics["cv_score"])