
import json


def __create_Dlib_Cluster(config,shape) :
    import dlib
    data = json.loads(config)
    threshod = data.get('threshod') if data.get('threshod') else 0.5
    labels = dlib.chinese_whispers_clustering(shape[0], threshod)
    return len(set(labels)), labels


def create_model(model_type,shaper,config=None):
    if model_type == 'DLIB Cluster':
        __create_Dlib_Cluster(config,shaper)