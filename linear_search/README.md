# Linear Search

This directory contains implementations of the linear search algorithm.

## Implementations

*   `linear_search.py`: This file contains two implementations of the linear search algorithm:
    1.  `linear_search_simple(arr, target)`: A basic linear search that iterates from the beginning of the list.
    2.  `linear_search_bidirectional(arr, target)`: A linear search that simultaneously searches from both ends of the list.

---

## Algorithm Explanation

### English

**History:**
Linear search is the simplest search algorithm. It is a sequential search that checks every element in a list until the target value is found or the end of the list is reached. While the concept is ancient, it's a fundamental building block in computer science.

**Use Cases:**
*   **Small Datasets:** It's efficient for small lists or arrays.
*   **Unsorted Data:** It works well when the data is not in any particular order.
*   **Simplicity:** When a simple, easy-to-implement search is needed without the overhead of more complex algorithms.

**Complexity:**
*   **Best Case:** O(1) - The target is the first element.
*   **Average Case:** O(n) - The target is somewhere in the middle of the list.
*   **Worst Case:** O(n) - The target is the last element or not in the list.

### Arabic

**تاريخ الخوارزمية:**
البحث الخطي هو أبسط خوارزمية بحث. إنه بحث تسلسلي يفحص كل عنصر في القائمة حتى يتم العثور على القيمة المستهدفة أو الوصول إلى نهاية القائمة. في حين أن المفهوم قديم، إلا أنه لبنة أساسية في علوم الكمبيوتر.

**حالات الاستخدام:**
*   **مجموعات البيانات الصغيرة:** إنه فعال للقوائم أو المصفوفات الصغيرة.
*   **البيانات غير المصنفة:** يعمل بشكل جيد عندما لا تكون البيانات في أي ترتيب معين.
*   **البساطة:** عند الحاجة إلى بحث بسيط وسهل التنفيذ دون الحاجة إلى تعقيدات الخوارزميات الأكثر تعقيدًا.

**التعقيد:**
*   **أفضل حالة:** O(1) - يكون الهدف هو العنصر الأول.
*   **الحالة المتوسطة:** O(n) - يكون الهدف في مكان ما في منتصف القائمة.
*   **أسوأ حالة:** O(n) - يكون الهدف هو العنصر الأخير أو غير موجود في القائمة.