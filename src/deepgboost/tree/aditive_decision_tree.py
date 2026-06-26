from __future__ import annotations

import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.utils import check_array
from sklearn.utils.validation import check_is_fitted


class AditiveDecisionTree(DecisionTreeRegressor):
    """
    DecisionTreeRegressor extended with additive per-feature contribution decomposition.

    Each prediction decomposes as:
        predict(X)[i] ≈ bias + contributions[i].sum()

    where ``bias`` is the root-node value and ``contributions[i, j]`` is the
    total value shift attributed to feature ``j`` along sample ``i``'s path:
    at every split, ``value[child] - value[parent]`` is credited to the
    feature used at that split.
    """

    def feature_contributions(
        self,
        X: np.ndarray,
    ) -> tuple[float, np.ndarray]:
        """
        Decompose predictions into a scalar bias and per-feature contributions.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)

        Returns
        -------
        bias : float
            Root-node prediction value (weighted mean of training targets).
        contributions : ndarray of shape (n_samples, n_features)
            ``contributions[i, j]`` is the additive contribution of feature
            ``j`` to the prediction for sample ``i``.
        """
        check_is_fitted(self)
        X = check_array(X, order="C", accept_sparse=False)

        tree = self.tree_
        split_features = tree.feature
        node_values = tree.value[:, 0, 0]
        children_left = tree.children_left
        children_right = tree.children_right

        # Precompute parent index for every node in O(n_nodes).
        # Root has no parent → stays -1.
        n_nodes = tree.node_count
        parent = np.full(n_nodes, -1, dtype=np.intp)
        for node in range(n_nodes):
            left = children_left[node]
            if left != -1:  # internal node
                parent[left] = node
                parent[children_right[node]] = node

        bias = float(node_values[0])

        indicator = super().decision_path(
            X,
        )  # CSR sparse matrix (n_samples, n_nodes)

        n_samples = X.shape[0]
        contributions = np.zeros(
            (n_samples, self.n_features_in_),
            dtype=np.float64,
        )

        for i in range(n_samples):
            nodes = indicator.indices[
                indicator.indptr[i] : indicator.indptr[i + 1]
            ]
            for node_idx in nodes[
                1:
            ]:  # skip root; its delta is already in bias
                p = parent[node_idx]
                feat = split_features[p]
                contributions[i, feat] += node_values[node_idx] - node_values[p]

        return bias, contributions
