import numpy as np

# דוגמאות שימוש לפונקציה normalize_array
import numpy as np

# מקרה רגיל
array1 = np.array([1, 2, 3, 4, 5])
normalized1 = normalize_array(array1)
print(f"מערך מקורי 1: {array1}")
print(f"מערך מנורמל 1: {normalized1}\n")

# מקרה עם ערכים שליליים
array2 = np.array([-10, 0, 10, 20])
normalized2 = normalize_array(array2)
print(f"מערך מקורי 2: {array2}")
print(f"מערך מנורמל 2: {normalized2}\n")

# מקרה שבו כל הערכים שווים (לדוגמה, אפסים)
array3 = np.array([0, 0, 0, 0])
normalized3 = normalize_array(array3)
print(f"מערך מקורי 3 (אפסים): {array3}")
print(f"מערך מנורמל 3 (אפסים): {normalized3}\n")

# מקרה שבו כל הערכים שווים (לדוגמה, מספר אחר)
array4 = np.array([5, 5, 5, 5])
normalized4 = normalize_array(array4)
print(f"מערך מקורי 4 (ערכים שווים): {array4}")
print(f"מערך מנורמל 4 (ערכים שווים): {normalized4}")

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
