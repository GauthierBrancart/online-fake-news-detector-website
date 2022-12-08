def label(prediction_score, MODEL_TYPE='tensorflow'):
    if MODEL_TYPE == 'ml':
        if prediction_score[0] == 'True':
            if prediction_score[1] > 0.2:
                return 'This article is True'
            else:
                return 'This article is Probably true'
        if prediction_score[0] == 'False':
            if prediction_score[1] < -0.2:
                return 'This article is False'
            else:
                return 'This article is Probably False'

    if MODEL_TYPE == 'tensorflow':
        if prediction_score >= 0.92:
            return 'This article is True'
        if prediction_score >= 0.87 and prediction_score < 0.92:
            return 'This article is Probably True'
        if prediction_score >= 0.8 and prediction_score < 0.87:
            return 'This article is probably False'
        if prediction_score < 0.8:
            return 'This article is False'

    return 'Something went wrong'
