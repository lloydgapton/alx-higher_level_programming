#include "lists.h"
/**
 * PalindromeRecur - Check for palindrome.
 * @left: Head of list
 * @right: Last element
 */
int PalindromeRecur(listint_t **left, listint_t *right)
{
	int pal;

	if (right == NULL)
		return (1);

	pal = PalindromeRecur(left, right->next);
	if (pal == 0)
		return (0);

	pal = (right->n == (*left)->n);

	*left = (*left)->next;
	return (pal);
}

/**
 * is_palindrome - Checks for palindrome.
 * @head: give list
 * @right: Last element
 */
int is_palindrome(listint_t **head)
{
	int res;

	if (!head)
		return (0);
	res = PalindromeRecur(head, *head);
	return (res);
}
