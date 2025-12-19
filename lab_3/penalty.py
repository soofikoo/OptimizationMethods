#import numpy as np
import numpy as np


class PenaltyFunction:
    def __init__(self, function, constraints, lam, eq_constraints = None):
        self.function = function
        self.constraints = constraints
        self.eq_constraints = eq_constraints
        self.lam = lam

    def __call__(self, x:np.ndarray)->float:
        if self.eq_constraints is None:
            penalty = 0.0
            for constraint in self.constraints:
                fi = constraint(x)
                penalty += self.lam / (-fi)
            return self.function(x) + penalty
        else:
            penalty = 0.0

            for constraint in self.constraints:
                fi = constraint(x)
                fi = max(0.0, fi)
                penalty += self.lam * fi ** 2

            for constraint in self.eq_constraints:
                psi = constraint(x)
                penalty += self.lam * psi ** 2

            return self.function(x) + penalty
