import numpy as np

def normalized_array(data):
    """
    מנרמלת מערך נתונים לטווח של [0, 1] לפי שיטת Min-Max Scaling.
    
    הנוסחה לביצוע:
    x_norm = (x - min) / (max - min)
    
    פרמטרים:
    data (list or np.array): מערך של מספרים.
    
    מחזירה:
    np.array: מערך מנורמל. אם כל הערכים במערך זהים, יש להחזיר מערך של אפסים.
    """
    # המרת הקלט ל-numpy array לצורך חישובים וקטוריים
    data = np.array(data)
    
    # --- כיתבו את הקוד שלכם כאן ---
    def normalize_array(input_array):
  min_val = np.min(input_array)
  max_val = np.max(input_array)

  # Handle the case where all values are equal to avoid division by zero
  if max_val - min_val == 0:
    # Return an array of zeros with the same shape and type as the input
    return np.zeros_like(input_array, dtype=input_array.dtype)
  else:
    new_array = (input_array - min_val) / (max_val - min_val)
    return new_array
    pass
    # חשוב לזכור להחליף את pass ב- return

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
