# Binary Search

This directory contains an implementation of the binary search algorithm.

## Implementation

*   `binary_search.py`: This file contains an implementation of the binary search algorithm.

---

## Algorithm Explanation

### English

**History:**
Binary search is a search algorithm that finds the position of a target value within a sorted array. It compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the array.

**Use Cases:**
*   **Large Datasets:** It is very efficient for searching in large, sorted datasets.
*   **Finding the position of an element:** It is used to find the position of an element in a sorted array.

**Complexity:**
*   **Best Case:** O(1) - The target is the middle element.
*   **Average Case:** O(log n) - The target is somewhere in the array.
*   **Worst Case:** O(log n) - The target is not in the array.

### Arabic

**تاريخ الخوارزمية:**
البحث الثنائي هو خوارزمية بحث تجد موضع القيمة المستهدفة داخل مصفوفة مرتبة. يقارن القيمة المستهدفة بالعنصر الأوسط من المصفوفة. إذا لم تكن متساوية، يتم التخلص من النصف الذي لا يمكن أن تقع فيه القيمة المستهدفة ويستمر البحث في النصف المتبقي، مع أخذ العنصر الأوسط مرة أخرى لمقارنته بالقيمة المستهدفة، وتكرار ذلك حتى يتم العثور على القيمة المستهدفة. إذا انتهى البحث بنصف متبقٍ فارغ، فإن الهدف غير موجود في المصفوفة.

**حالات الاستخدام:**
*   **مجموعات البيانات الكبيرة:** إنه فعال للغاية للبحث في مجموعات البيانات الكبيرة والمرتبة.
*   **إيجاد موضع عنصر:** يتم استخدامه للعثور على موضع عنصر في مصفوفة مرتبة.

**التعقيد:**
*   **أفضل حالة:** O(1) - يكون الهدف هو العنصر الأوسط.
*   **الحالة المتوسطة:** O(log n) - يكون الهدف في مكان ما في المصفوفة.
*   **أسوأ حالة:** O(log n) - الهدف غير موجود في المصفوفة.
