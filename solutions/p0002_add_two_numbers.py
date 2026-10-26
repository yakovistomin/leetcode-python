class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:  # noqa: A002
        self.val = val
        self.next = next


def build_linked_list(values: list[int]) -> ListNode | None:
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def linked_list_to_list(value: ListNode | None) -> list[int]:
    result = []

    while value is not None:
        result.append(value.val)
        value = value.next

    return result


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy_node = ListNode()
        current_node = dummy_node

        carry = 0
        while l1 or l2 or carry:
            value = carry

            if l1:
                value += l1.val
                l1 = l1.next

            if l2:
                value += l2.val
                l2 = l2.next

            carry, digit = divmod(value, 10)

            current_node.next = ListNode(val=digit)
            current_node = current_node.next

        return dummy_node.next
