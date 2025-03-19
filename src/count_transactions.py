from collections import Counter
from typing import List, Dict


def count_transactions_by_category(transactions: List[dict], categories: List[str]) -> Dict[str, int]:
    """Функция для подсчета количества банковских операций по категориям."""
    total_num_operations = 0
    category_counter = Counter()

    for transaction in transactions:
        if "description" in transaction:
            description = transaction["description"]
            category_counter[description] += 1
            total_num_operations += 1

    print(f"Всего банковских операций в выборке: {total_num_operations}")
    counted_transactions = {category: category_counter[category] for category in categories}

    return counted_transactions




#transaction_counts = count_transactions_by_category(transactions, categories)
#print(transaction_counts)