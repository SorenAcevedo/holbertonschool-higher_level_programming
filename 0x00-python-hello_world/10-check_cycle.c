#include "lists.h"

/**
 * check_cycle - check if a list have a cycle
 * @list: head from the list
 * Return: 1 if is a cycle, 0 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t liebre, tortuga;

	liebre = list->next;
	tortuga = list;

	while (liebre && tortuga && liebre->next)
	{
		if (liebre == tortuga)
			return (1);
		liebre = liebre->next->next;
		tortuga = tortuga->next;
	}
	return (0)
}
