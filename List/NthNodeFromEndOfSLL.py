"""
     * <pre>
     * !Program for Nth node from the end of a Linked List
     * Given a Linked List of M nodes and a number N,
     * find the value at the Nth node from the end of the Linked List.
     * If there is no Nth node from the end, print -1.
     *
     * @param Examples:
     * Input: 1 -> 2 -> 3 -> 4, N = 3
     * Output: 2
     * Explanation: Node 2 is the third node from the end of the linked list.
     *
     * Input: 35 -> 15 -> 4 -> 20, N = 4
     * Output: 35
     * Explanation: Node 35 is the fourth node from the end of the linked list.
     *
     * !Approach: By Finding the length of list - Two Pass - O(M) Time and O(1) Space
     * The idea is to count the number of nodes in linked list in the first pass, say len.
     * In the second pass, return the (len - n + 1)th nodes from beginning of the Linked List.
     * </pre>
"""

