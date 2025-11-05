import pandas as pd				#загрузка библиотек
import numpy as np
import pytest


def test_fare_calculations():
    """Тест правильности расчетов стоимости билетов по статусу выживания"""

    test_data = {
        'Survived': [1, 0, 1, 0, 1],
        'Fare': [50.0, 30.0, 70.0, 20.0, 60.0],
        'Embarked': ['S', 'S', 'S', 'S', 'S']
    }
    df = pd.DataFrame(test_data)


    filtered_df = df[df['Embarked'] == 'S']


    survived_sum = 0
    survived_count = 0
    dead_sum = 0
    dead_count = 0

    for index, passenger in filtered_df.iterrows():
        fare = passenger["Fare"]
        if pd.isna(fare):
            continue
        if passenger["Survived"] == 1:
            survived_sum += fare
            survived_count += 1
        else:
            dead_sum += fare
            dead_count += 1

    avg_survived_fare = survived_sum / survived_count if survived_count else 0
    avg_dead_fare = dead_sum / dead_count if dead_count else 0

    assert survived_count == 3
    assert dead_count == 2
    assert survived_sum == 180.0
    assert dead_sum == 50.0
    assert avg_survived_fare == 60.0
    assert avg_dead_fare == 25.0


def test_missing_values_handling():
    """Тест обработки пропущенных значений в стоимости билетов"""

    test_data = {
        'Survived': [1, 0, 1, 0],
        'Fare': [100.0, np.nan, 50.0, np.nan],
        'Embarked': ['C', 'C', 'C', 'C']
    }
    df = pd.DataFrame(test_data)

    filtered_df = df[df['Embarked'] == 'C']

    survived_sum = 0
    survived_count = 0
    dead_sum = 0
    dead_count = 0

    for index, passenger in filtered_df.iterrows():
        fare = passenger["Fare"]
        if pd.isna(fare):
            continue
        if passenger["Survived"] == 1:
            survived_sum += fare
            survived_count += 1
        else:
            dead_sum += fare
            dead_count += 1

    avg_survived_fare = survived_sum / survived_count if survived_count else 0
    avg_dead_fare = dead_sum / dead_count if dead_count else 0


    assert survived_count == 2
    assert dead_count == 0
    assert survived_sum == 150.0
    assert dead_sum == 0.0
    assert avg_survived_fare == 75.0
    assert avg_dead_fare == 0.0


def test_edge_cases():
    """Тест граничных условий и edge-cases"""

    test_data_empty = {
        'Survived': [1, 0],
        'Fare': [100.0, 50.0],
        'Embarked': ['Q', 'Q']
    }
    df_empty = pd.DataFrame(test_data_empty)
    filtered_df_empty = df_empty[df_empty['Embarked'] == 'S']

    survived_sum = 0
    survived_count = 0
    dead_sum = 0
    dead_count = 0

    for index, passenger in filtered_df_empty.iterrows():
        fare = passenger["Fare"]
        if pd.isna(fare):
            continue
        if passenger["Survived"] == 1:
            survived_sum += fare
            survived_count += 1
        else:
            dead_sum += fare
            dead_count += 1

    avg_survived_fare = survived_sum / survived_count if survived_count else 0
    avg_dead_fare = dead_sum / dead_count if dead_count else 0

    assert survived_count == 0
    assert dead_count == 0
    assert avg_survived_fare == 0
    assert avg_dead_fare == 0

    test_data_survived_only = {
        'Survived': [1, 1, 1],
        'Fare': [10.0, 20.0, 30.0],
        'Embarked': ['S', 'S', 'S']
    }
    df_survived_only = pd.DataFrame(test_data_survived_only)

    filtered_df_survived = df_survived_only[df_survived_only['Embarked'] == 'S']

    survived_sum = 0
    survived_count = 0
    dead_sum = 0
    dead_count = 0

    for index, passenger in filtered_df_survived.iterrows():
        fare = passenger["Fare"]
        if pd.isna(fare):
            continue
        if passenger["Survived"] == 1:
            survived_sum += fare
            survived_count += 1
        else:
            dead_sum += fare
            dead_count += 1

    avg_survived_fare = survived_sum / survived_count if survived_count else 0
    avg_dead_fare = dead_sum / dead_count if dead_count else 0

    assert survived_count == 3
    assert dead_count == 0
    assert survived_sum == 60.0
    assert avg_survived_fare == 20.0
    assert avg_dead_fare == 0.0
