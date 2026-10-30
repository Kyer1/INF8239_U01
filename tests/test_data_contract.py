import pytest

from inf8239_u01.data import DEFAULT_PATH, download_csv, load_data

TARGET = "Target"
REQUIRED = {TARGET, "Course", "Curricular units 1st sem (approved)"}


@pytest.fixture(scope="module")
def data():
    if not DEFAULT_PATH.exists():
        download_csv()
    return load_data()


def test_dataset_is_not_empty(data):
    assert not data.empty


def test_required_columns_exist(data):
    assert REQUIRED <= set(data.columns)


def test_target_has_no_missing_and_expected_classes(data):
    y = data[TARGET]
    assert y.notna().all()
    assert set(y.unique()) == {"Dropout", "Enrolled", "Graduate"}


def test_download_rejects_non_http_url():
    with pytest.raises(ValueError):
        download_csv("C:/Users/archivo.csv")