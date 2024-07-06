def One_Hot_Encoding(df, cat_columns):
    # Создаем dummy-переменные для категориальных признаков
    one_hot = pd.get_dummies(df[cat_columns])

    # Преобразуем логические значения (тип bool) в целые числа (тип int) в dummy-переменных
    bool_columns = one_hot.select_dtypes(include=[bool]).columns
    if not bool_columns.empty:
        one_hot[bool_columns] = one_hot[bool_columns].astype(int)

    # Удаляем оригинальные категориальные признаки из исходного датафрейма
    df = df.drop(cat_columns, axis=1)

    # Объединяем исходный df с dummy-переменными
    df = pd.concat([df, one_hot], axis=1)

    return df