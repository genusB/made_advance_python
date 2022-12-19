import pytest

from predict_message_mood import predict_message_mood
from some_model import SomeModel
from mock_predict_funcs import mock_predict_high, mock_predict_medium, mock_predict_low


@pytest.mark.parametrize("good_threshold, bad_threshold, expected_result", [(1.0, 0.0, 'норм'),
                                                                            (0.8, 0.7, 'отл'),
                                                                            (0.99, 0.95, 'неуд'),
                                                                            (0.9, 0.8, 'норм'),
                                                                            (1.0, 0.9, 'норм'),
                                                                            (0.9, 0.9, 'норм')])
def test_with_thresholds_for_high_score(monkeypatch, good_threshold, bad_threshold, expected_result):
    monkeypatch.setattr('some_model.SomeModel.predict', mock_predict_high)

    model = SomeModel()

    assert predict_message_mood('message', model, bad_threshold, good_threshold) == expected_result


@pytest.mark.parametrize("good_threshold, bad_threshold, expected_result", [(0.9, 0.3, 'норм'),
                                                                            (0.3, 0.2, 'отл'),
                                                                            (0.9, 0.6, 'неуд'),
                                                                            (0.5, 0.4, 'норм'),
                                                                            (1.0, 0.5, 'норм'),
                                                                            (0.5, 0.5, 'норм')])
def test_with_thresholds_for_medium_score(monkeypatch, good_threshold, bad_threshold, expected_result):
    monkeypatch.setattr('some_model.SomeModel.predict', mock_predict_medium)

    model = SomeModel()

    assert predict_message_mood('message', model, bad_threshold, good_threshold) == expected_result


@pytest.mark.parametrize("good_threshold, bad_threshold, expected_result", [(0.4, 0.0, 'норм'),
                                                                            (0.05, 0.0, 'отл'),
                                                                            (0.9, 0.6, 'неуд'),
                                                                            (0.1, 0.0, 'норм'),
                                                                            (1.0, 0.1, 'норм'),
                                                                            (0.1, 0.1, 'норм')])
def test_with_thresholds_for_low_score(monkeypatch, good_threshold, bad_threshold, expected_result):
    monkeypatch.setattr('some_model.SomeModel.predict', mock_predict_low)

    model = SomeModel()

    assert predict_message_mood('message', model, bad_threshold, good_threshold) == expected_result


@pytest.mark.parametrize("good_threshold, bad_threshold", [(10.0, 0.0),
                                                           (-0.05, 0.0),
                                                           (0.0, -12.0),
                                                           (0.0, 10.0)])
def test_thresholds_out_of_bounds(monkeypatch, good_threshold, bad_threshold):
    monkeypatch.setattr('some_model.SomeModel.predict', mock_predict_medium)

    model = SomeModel()

    with pytest.raises(ValueError):
        predict_message_mood('message', model, bad_threshold, good_threshold)


@pytest.mark.parametrize("good_threshold, bad_threshold", [(0.3, 0.5),
                                                           (0.7, 0.9)])
def test_thresholds_out_of_bounds(monkeypatch, good_threshold, bad_threshold):
    monkeypatch.setattr('some_model.SomeModel.predict', mock_predict_medium)

    model = SomeModel()

    with pytest.raises(ValueError):
        predict_message_mood('message', model, bad_threshold, good_threshold)
