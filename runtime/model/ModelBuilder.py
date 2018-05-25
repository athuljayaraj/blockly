import json
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor


def create_model(model_type,config=None):
    if model_type == 'Gradient Boosting Regressor':
        random_state = 0
        if config :
            data = json.loads(config)
            random_state = data.get('random_state') if data.get('random_state') else 0

        model = MultiOutputRegressor(GradientBoostingRegressor(random_state=random_state))
        return model


def train_model(model,shaper, showResult = True):
    if model :
        model.fit(shaper[0], shaper[1])
    if showResult or showResult =='true' :
        result = model.score(shaper[2], shaper[3])
        print("Model accuracy",result * 100)
    return model


def predict_model(model,shaper):
    if model :
        result = model.predict(shaper[0])
        print ("Predicted value ", result)
        return result
