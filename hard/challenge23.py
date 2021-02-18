from typing import List, Optional, Any


class ListNode:
    def __init__(self, val: int = 0, next: Optional[Any] = None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 812 ms, faster than 13.43% of Python3 online submissions for Merge k Sorted Lists.
    Memory Usage: 420.5 MB, less than 5.03% of Python3 online submissions for Merge k Sorted Lists.
    """
    def node_to_list(self, node: ListNode, my_list: List = []) -> List:
        my_list.append(node.val)
        if node.next:
            return self.node_to_list(node.next, my_list)
        return my_list

    def list_to_node(self, my_list: List, node: Optional[ListNode] = None) -> ListNode:
        if my_list:
            return self.list_to_node(my_list[1:], ListNode(my_list[0], node))
        return node

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        merged = []
        for x in lists:
            if not x:
                continue
            merged = self.node_to_list(x, merged)
        merged.sort(reverse=True)
        return self.list_to_node(merged)


if __name__ == '__main__':
    input = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6))
    ]
    response = Solution().mergeKLists(input)
    print("Output: {}".format(Solution().node_to_list(response)))
