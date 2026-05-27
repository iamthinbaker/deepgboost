# CHANGELOG


## v0.3.4 (2026-05-27)

### Bug Fixes

- Fix wrong tagging and configure semantic release
  ([`776fb6f`](https://github.com/iamthinbaker/deepgboost/commit/776fb6f70de12dca0451001542ceb7d398364d62))


## v0.3.2 (2026-05-27)

### Chores

- **#2**: Update experiments
  ([`6c0d713`](https://github.com/iamthinbaker/deepgboost/commit/6c0d71391a69f9f1543dab4057181492d092ca69))

Added Classification experiment: ClassificationBootstrapTest is added alongside the existing
  BootstrapModelTest for regression. Configuration is split into RegressionModels and
  ClassificationModels

New model XGBoost: : Added XGBoost Regressor and classifier to the benchmark

Model Adapters: Created a model abstract interface and the wrapper implementation for all the
  models: GradientBoosting, RandomForest, XGBoost, and DeepGBoost.

New datasets: Abalone, Adult, BankMarketing, CaliforniaHousing and Penguins are added (regression
  and classification). Obsolete datasets removed (Cargo2000, Obesity, Parkinson, Superconductor,
  Temperature, Wine).

- **#4**: Run benchmark
  ([`220b613`](https://github.com/iamthinbaker/deepgboost/commit/220b613ea4637638b57446d4eca76201d82bc1e9))

* chore changed experiment result format to jsonl

* add benchmar generator

* update github action filter

### Features

- Deepgboostmulticlassifier, benchmark fixes, ablation config, std from CV folds
  ([`c02e76f`](https://github.com/iamthinbaker/deepgboost/commit/c02e76fa40affd36adf8b5b4064b7976ae4e4a31))

- Add DeepGBoostMultiClassifier with native softmax multiclass (DGBFMultiOutputModel, per-class
  single-output trees, hessian-weighted NNLS) - Rename gbm/ → dgbf/ module structure - Fix
  CrossValidationModelTest std: store per-fold scores (not per-run averages) - Fix
  BenchmarkGenerator to read *_cross_validation_test.json and strip both bootstrap/cv suffixes -
  Integrate ablation support into config.json + ExperimentRunner (Ablations: [] section, no-op by
  default) - Delete standalone run_ablation.py; ablations now run via run_experiments.py - Fix
  quickstart.ipynb import path after dgbf/ rename - Add COM812 trailing commas across all source
  files (ruff compliance) - Remove 6 redundant/tautological tests (134 → 128 passing tests)

- **#1**: Create python project
  ([`7613924`](https://github.com/iamthinbaker/deepgboost/commit/76139242de9c7492c1ca1227a9ec78ce07d6e793))

Summary New Python package deepgboost: full implementation of the DGBF (Distributed Gradient
  Boosting Forest) algorithm, including regressor, classifier (binary and multiclass), low-level
  functional API (DeepGBoostBooster), callback system, and plotting utilities.

Test suite: coverage of all core modules — booster, regressor, classifier, metrics, objectives,
  callbacks, and training.

Reproducible benchmark: scripts to compare DGBF against RandomForest and GradientBoosting on 9 UCI
  regression datasets, with pre-generated results (CSV, PNG). DGBF outperforms both in 7 out of 9
  datasets.

Example notebooks: quickstart, classifier, regressor, and serialization — all executable and
  validated with nbmake.

CI/CD: GitHub Actions workflows for multi-version testing (3.10–3.13), linting with ruff, coverage
  reporting via Codecov, notebook execution, automated PR review with Claude, and PyPI publishing
  via OIDC Trusted Publishing on v*.. tags.

README: documentation with algorithm description, equations, figures, and benchmark results.

- **#5**: Add hessian residuals
  ([`03797f0`](https://github.com/iamthinbaker/deepgboost/commit/03797f06bd13b7b3840119ce99569ff0138850e0))

* Added hessian residuals: Improve the leraning process using the second order derivative from the
  Taylor expansion (hessian). This is equivalent to use the newton raphsody optimization process.
  The difference may be noticed mainly in classifier

* Improve default params: After many iteration improved the default params from both, classifier and
  regressor models

* Added agents and skills: Included expertise agents and skills in the project scope to improve the
  learning process. As well as a mcp connection to github not used in this PR because today the api
  is falling :(

* Rerun benchmark results: Still the best model out of the four but it makes me mad not winning in
  all the datasets. DeepGBoost is a more general model than RandomForest and XGBoost. It should
  always win.
