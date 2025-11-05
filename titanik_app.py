import streamlit as st				# Загрузка бибилотек
import pandas as pd

st.image("/home/iceman/PycharmProjects/PythonProject/titanik.png",
         caption="Титаник",
         use_container_width=True)

st.subheader("Вычислить среднюю стоимость билета")

df = pd.read_csv("titanic_train.csv")

st.subheader("Выбор порта посадки")

embark_port_mapping = {
    'C': "Шербур (Cherbourg)",
    'Q': "Квинстаун (Queenstown)",
    'S': "Саутгемптон (Southampton)"
}

selected_port_key = st.selectbox(
    "Выберите порт посадки:",
    options=list(embark_port_mapping.keys()),
    format_func=lambda x: embark_port_mapping[x],
    index=0
)

st.write(f"Выбран порт: **{embark_port_mapping[selected_port_key]}**")

if 'Embarked' in df.columns:
    filtered_df = df[df['Embarked'] == selected_port_key]
else:
    st.warning("Столбец 'Embarked' не найден в данных. Показываю все данные.")
    filtered_df = df

st.subheader("Средняя стоимость билета по статусу выживания")

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

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Средняя стоимость билета (Выжившие)",
        value=f"${avg_survived_fare:.2f}",
        delta=f"{survived_count} пассажиров"
    )

with col2:
    st.metric(
        label="Средняя стоимость билета (Погибшие)",
        value=f"${avg_dead_fare:.2f}",
        delta=f"{dead_count} пассажиров",
        delta_color="inverse"
    )

st.subheader("Детальная статистика")
st.write(f"Всего пассажиров из {embark_port_mapping[selected_port_key]}: {len(filtered_df)}")
st.write(f"Выживших пассажиров: {survived_count}")
st.write(f"Погибших пассажиров: {dead_count}")
st.write(f"Общая сумма билетов выживших: ${survived_sum:.2f}")
st.write(f"Общая сумма билетов погибших: ${dead_sum:.2f}")
