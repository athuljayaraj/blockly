import json
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import svm

def create_model(model_type,config=None):
    if model_type == 'Gradient Boosting Regressor':
        random_state = 0
        if config :
            data = json.loads(config)
            random_state = data.get('random_state') if data.get('random_state') else 0

        model = MultiOutputRegressor(GradientBoostingRegressor(random_state=random_state))
        return model

    if model_type == "SVM Classification":
        '''
        Pros:
         It works really well with clear margin of separation
         It is effective in high dimensional spaces
         It is effective in cases where number of dimensions is greater than the number of samples.
         It uses a subset of training points in the decision function (called support vectors), so it is also memory efficient
        Cons :
         It doesnt perform well, when we have large data set because the required training time is higher.
         It also doesnt perform very well, when the data set has more noise i.e. target classes are overlapping.
         SVM doesn't directly provide probability estimates, these are calculated using an expensive five-fold cross validation. 
         It is related SVC method of Python scikit learn library
        '''
        return __create_svm_classifier__(config)

    if model_type == "SVM Regression" :
        return __create_svm_regressor__(config)
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
def __create_svm_classifier__(config):

    #(C=1.0, kernel='rbf', degree=3, gamma=0.0, coef0=0.0, shrinking=True, probability=False,tol=0.001, cache_size=200,
    # class_weight=None, verbose=False, max_iter=-1, random_state=None)

    # sample keranal  values "linear", "rbf","poly","sigmoid"
    data = json.loads(config)
    c = data.get('c') if data.get('c') else 1
    gamma = data.get('gamma') if data.get('gamma') else 1
    kernel = data.get('kernel') if data.get('kernel') else 'linear'
    model = svm.SVC(kernel=kernel, C=float(c), gamma=float(gamma))
    return model

def __create_svm_regressor__(config) :
    data = json.loads(config)
    c = data.get('c') if data.get('c') else 1
    gamma = data.get('gamma') if data.get('gamma') else 1
    kernel = data.get('kernel') if data.get('kernel') else 'linear'
    model = svm.SVR(kernel=kernel, verbose=True)
    return model
