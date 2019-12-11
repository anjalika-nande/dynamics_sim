from games.game import SymmetricNPlayerGame

class StochasticPD(SymmetricNPlayerGame):
    """
    
    """
    DEFAULT_PARAMS = dict(R=3, T=5, S=0, P=1, bias_strength=0)
    STRATEGY_LABELS = ('ALLD', 'ALLC', 'TFT')
    EQUILIBRIA_LABELS = ('Cooperative Equilibrium', 'Non Cooperative Equilibirum')

    def __init__(self, R, T, S, P, bias_strength):

        
        payoff_matrix = ((P, T, P),
                         (S, R, R),
                         (P, R, R))
        

        super(StochasticPD, self).__init__(payoff_matrix, 2,bias_strength)
        
    
    @classmethod
    def classify(cls, params, state, tolerance):
        
        R = getattr(params,"R")
        T = getattr(params,"T")
        S = getattr(params,"S")
        P = getattr(params,"P")
        
        tolerance = (R-P)/(T-R)

        if state[0][1] <= tolerance * state[0][2] :
            return 0#Cooperative Equilibrium
        elif state[0][1] > tolerance * state[0][2] :
            return 1#NonCooperative Equilibrium
        else:
            return super(StochasticPD, cls).classify(params, state, tolerance)
