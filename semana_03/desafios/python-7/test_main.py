from main import get_temperature
from unittest import mock
import pytest

temperaturas = [(60, 15), (80, 26), (70, 21), (50, 10), (46, 7), (-2, -18)]


@pytest.mark.parametrize("faren, celsius", temperaturas)
def test_get_temperature_by_lat_lng(faren, celsius):
    mock_patch = "main.requests.get"

    with mock.patch(mock_patch) as mp:
        mp.return_value.json.return_value = {'currently': {'temperature': faren}}
        resultado = get_temperature(64.1405435, -21.951502)

    assert resultado == celsius