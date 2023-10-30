#include "lists.h"
/**
 * check_cycle - check for cyclic linked list
 * @list: linked list
 * Return: 1 if true, 0 if false
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;

	if (current->next != NULL)
	{
		current = current->next;
	}
	else
	{
		return (0);
	}
	while (current != list)
	{
		if (current->next == NULL)
		{
			return (0);
		}
		current = current->next;
	}
	return (1);
}
