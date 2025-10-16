from mathx.probability.distribution.continuous import Continuous as ContinousDistribution
from mathx.probability.covariance_matrix import CovarianceMatrix
from mathx.linalg.vec.vec import Vec


class Distribution(ContinousDistribution):
    def __init__(self, mu:Vec, cov_matrix:CovarianceMatrix):
        self._mu = mu
        self._cov_matrix = cov_matrix

    def get_mu(self) -> Vec:
        return self._mu

    def get_cov_matrix(self) -> CovarianceMatrix:
        return self._cov_matrix