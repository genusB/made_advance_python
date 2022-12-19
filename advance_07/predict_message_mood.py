from some_model import SomeModel


def predict_message_mood(
        message: str,
        model: SomeModel,
        bad_thresholds: float = 0.3,
        good_thresholds: float = 0.8,
) -> str:
    score: float = model.predict(message)

    if good_thresholds > 1.0 or good_thresholds < 0.0:
        raise ValueError('good_thresholds must be in range [0.0 , 1.0]')

    if bad_thresholds > 1.0 or bad_thresholds < 0.0:
        raise ValueError('bad_thresholds must be in range [0.0 , 1.0]')

    if good_thresholds < bad_thresholds:
        raise ValueError('good_thresholds must be greater than bad_thresholds')

    if score < bad_thresholds:
        return 'неуд'
    elif score > good_thresholds:
        return 'отл'
    else:
        return 'норм'
