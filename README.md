# Real-Estate-Estimator

פרויקט לחיזוי מחירי דירות ומחירי שכר הדירות בשוק הנדל"ן בישראל.

מטרת הפרויקט היא למצוא איפה הכי כדאי לקנות דירה להשקעה. עשיתי זאת באמצעות חישוב פרמטר חשוב: Cap Rate, שזה בגדול שיעור התשואה של הדירה.

תהליך יצירת הפרויקט:
-🔍 אספתי נתונים מהאתרים yad2.co.il ו ad.co.il בעזרת scraping
- 📊 ביצעתי Preprocessing לסט הנתונים וביצעתי EDA למחירי דירות ולמחירי שכר דירות והסקתי מסקנות
- 💻 יצרתי שני מודלים - מודל שחוזה מחיר דירה ומודל שחוזה מחיר שכר דירה עם טכניקות של רגרסיה
- 📈 חישבתי את ה-cap rate עבור כל דירה בסט הנתונים וכך מצאתי באיזה ערים הכי כדאי להשקיע.

מסתבר שבאר שבע היא בין הערים שכדאי לרכוש בהם דירה להשקעה עם אחוז תשואה ממוצע של 3.47%, לעומת ערים כמו תל אביב עם אחוז תשואה ממוצע של 2.54% (כמובן שזה לא מדויק וזה למטרות לימוד בלבד).

Links:
Streamlit App: https://real-estate-estimator.streamlit.app

Sales EDA: https://nbviewer.org/github/noams24/Real-Estate-Estimator/blob/master/notebook/sale_eda.ipynb

Rent price EDA: https://nbviewer.org/github/noams24/Real-Estate-Estimator/blob/master/notebook/rent_eda.ipynb

Short EDA about the cap rates: https://nbviewer.org/github/noams24/Real-Estate-Estimator/blob/master/notebook/final_eda.ipynb
