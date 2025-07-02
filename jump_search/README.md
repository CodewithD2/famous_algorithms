# Jump Search

This directory contains an implementation of the jump search algorithm.

## Implementation

*   `jump_search.py`: This file contains an implementation of the jump search algorithm.

---

## Algorithm Explanation

### English

**History:**
Jump search (or block search) is a search algorithm for sorted arrays. It works by jumping ahead by a fixed number of steps, and then performing a linear search in the block where the element might be present. The optimal step size is the square root of the array's length.

**Use Cases:**
*   **Sorted Arrays:** It is used for searching in sorted arrays.
*   **Better than Linear Search:** It is more efficient than linear search, but less efficient than binary search. It is useful in systems where binary search is not possible or is too costly.

**Complexity:**
*   **Best Case:** O(1) - The target is the first element.
*   **Average Case:** O(√n) - The target is somewhere in the array.
*   **Worst Case:** O(√n) - The target is not in the array.

### Arabic

**تاريخ الخوارزمية:**
بحث القفز (أو بحث الكتلة) هو خوارزمية بحث للمصفوفات المرتبة. يعمل عن طريق القفز إلى الأمام بعدد ثابت من الخطوات، ثم إجراء بحث خطي في الكتلة التي قد يكون العنصر موجودًا فيها. حجم الخطوة الأمثل هو الجذر التربيعي لطول المصفوفة.

**حالات الاستخدام:**
*   **المصفوفات المرتبة:** يتم استخدامه للبحث في المصفوفات المرتبة.
*   **أفضل من البحث الخطي:** إنه أكثر كفاءة من البحث الخطي، ولكنه أقل كفاءة من البحث الثنائي. إنه مفيد في الأنظمة التي لا يكون فيها البحث الثنائي ممكنًا أو مكلفًا للغاية.

**التعقيد:**
*   **أفضل حالة:** O(1) - يكون الهدف هو العنصر الأول.
*   **الحالة المتوسطة:** O(√n) - يكون الهدف في مكان ما في المصفوفة.
*   **أسوأ حالة:** O(√n) - الهدف غير موجود في المصفوفة.
