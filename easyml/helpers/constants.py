PLOT_FEATURE_CAP = 8

class COLUMN_TYPE:
    IGNORE = 0
    INPUT = 1
    TARGET = 2

class ALGORITHM:
    LINEAR_REGRESSION = 1
    LOGISTIC_REGRESSION = 2
    LINEAR_DISCRIMINANT_ANALYSIS = 3
    DECISION_TREE_REGRESSOR = 4
    GAUSSIAN_NAIVE_BAYES = 5
    RANDOM_FOREST_CLASSIFIER = 6
    RANDOM_FOREST_REGRESSOR = 7
    K_NEAREST_NEIGHBORS_CLASSIFIER = 8
    K_NEAREST_NEIGHBORS_REGRESSOR = 9
    SUPPORT_VECTOR_MACHINE_CLASSIFIER = 10
    SUPPORT_VECTOR_MACHINE_REGRESSOR = 11
    NEAREST_CENTROID = 12


ALGORITHM_NAME_MAP = {
    ALGORITHM.LINEAR_REGRESSION: 'Linear Regression',
    ALGORITHM.LOGISTIC_REGRESSION: 'Logistic Regression',
    ALGORITHM.LINEAR_DISCRIMINANT_ANALYSIS: 'Linear Discriminant Analysis',
    ALGORITHM.DECISION_TREE_REGRESSOR: 'Decision Tree Regressor',
    ALGORITHM.GAUSSIAN_NAIVE_BAYES: 'Gaussian Naive Bayes',
    ALGORITHM.RANDOM_FOREST_CLASSIFIER: 'Random Forest Classifier',
    ALGORITHM.RANDOM_FOREST_REGRESSOR: 'Random Forest Regressor',
    ALGORITHM.K_NEAREST_NEIGHBORS_CLASSIFIER: 'K Nearest Neighbors Classifier',
    ALGORITHM.K_NEAREST_NEIGHBORS_REGRESSOR: 'K Nearest Neighbors Regressor',
    ALGORITHM.SUPPORT_VECTOR_MACHINE_CLASSIFIER: 'Support Vector Machine Classifier',
    ALGORITHM.SUPPORT_VECTOR_MACHINE_REGRESSOR: 'Support Vector Machine Regressor',
    ALGORITHM.NEAREST_CENTROID: 'Nearest Centroid',
}

ALGORITHM_PARAM_MAP = {
    ALGORITHM.LINEAR_REGRESSION: ['linreg_normalize', 'linreg_fit_intercept'],
    ALGORITHM.LOGISTIC_REGRESSION: ['logreg_fit_intercept', 'logreg_C', 'logreg_C_select', 'logreg_penalty'],
    ALGORITHM.LINEAR_DISCRIMINANT_ANALYSIS: ['lda_solver'],
    ALGORITHM.DECISION_TREE_REGRESSOR: ['dtr_criterion', 'dtr_presort', 'dtr_max_depth', 'dtr_custom_depth'],
    ALGORITHM.GAUSSIAN_NAIVE_BAYES: [],
    ALGORITHM.RANDOM_FOREST_CLASSIFIER: ['rfc_criterion', 'rfc_n_estimators', 'rfc_max_depth', 'rfc_custom_depth'],
    ALGORITHM.RANDOM_FOREST_REGRESSOR: ['rfr_criterion', 'rfr_n_estimators', 'rfr_max_depth', 'rfr_custom_depth'],
    ALGORITHM.K_NEAREST_NEIGHBORS_CLASSIFIER: ['nnc_weights', 'nnc_algorithm', 'nnc_k', 'nnc_p'],
    ALGORITHM.K_NEAREST_NEIGHBORS_REGRESSOR: ['nnr_weights', 'nnr_algorithm', 'nnr_k', 'nnr_p'],
    ALGORITHM.SUPPORT_VECTOR_MACHINE_CLASSIFIER: ['svc_degree', 'svc_C', 'svc_kernel'],
    ALGORITHM.SUPPORT_VECTOR_MACHINE_REGRESSOR: ['svr_degree', 'svr_kernel'],
    ALGORITHM.NEAREST_CENTROID: [],
}
