import numpy as np


class Regressor(object):
    """
    Base class for regressors
    """

    def ml(self, X, t):
        """
        maximum likelihood estimation of the parameters

        Parameters
        ----------
        X : (sample_size, n_features) np.ndarray
            training data input
        t : (sample_size,) np.ndarray
            training data target
        """
        self._check_input(X)
        self._check_target(t)
        if hasattr(self, "_ml"):
            self._ml(X, t)
        else:
            raise NotImplementedError

    def map(self, X, t):
        """
        maximum a posteriori estimation of the parameters

        Parameters
        ----------
        X : (sample_size, n_features) np.ndarray
            training data input
        t : (sample_size,) np.ndarray
            training data target
        """
        self._check_input(X)
        self._check_target(t)
        if hasattr(self, "_map"):
            self._map(X, t)
        else:
            raise NotImplementedError

    def bayes(self, X, t):
        """
        bayesian estimation of the parameters

        Parameters
        ----------
        X : (sample_size, n_features) np.ndarray
            training data input
        t : (sample_size,) np.ndarray
            training data target
        """
        self._check_input(X)
        self._check_target(t)
        if hasattr(self, "_bayes"):
            self._bayes(X, t)
        else:
            raise NotImplementedError

    def empirical_bayes(self, X, t, **kwargs):
        """
        emprical bayesian estimation of the hyperparameters,
        aka evidence approximation, type 2 maximum likelihood,
        and generalized maximum likelihood

        Parameters
        ----------
        X : (sample_size, n_features) np.ndarray
            training data input
        t : (sample_size,) np.ndarray
            training data target
        """
        self._check_input(X)
        self._check_target(t)
        if hasattr(self, "_empirical_bayes"):
            self._empirical_bayes(X, t, **kwargs)
        else:
            raise NotImplementedError

    def predict(self, X, **kwargs):
        """
        predict outputs of the model

        Parameters
        ----------
        X : (sample_size, n_features) np.ndarray
            samples to predict their output

        Returns
        -------
        y : (sample_size,) np.ndarray
            prediction of each sample
        """
        self._check_input(X)
        if hasattr(self, "_predict"):
            return self._predict(X, **kwargs)
        else:
            raise NotImplementedError

    def _check_input(self, X):
        if not isinstance(X, np.ndarray):
            raise ValueError("X(input) is not np.ndarray")
        if X.ndim != 2:
            raise ValueError("X(input) is not two dimensional array")
        if hasattr(self, "n_features") and self.n_features != np.size(X, 1):
            raise ValueError(
                "mismatch in dimension 1 of X(input) "
                "(size {} is different from {})"
                .format(np.size(X, 1), self.n_features)
            )

    def _check_target(self, t):
        if not isinstance(t, np.ndarray):
            raise ValueError("t(target) must be np.ndarray")
        if t.ndim != 1:
            raise ValueError("t(target) must be one dimenional array")
