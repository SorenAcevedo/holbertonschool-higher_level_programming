#include "lists.h"

/**
 * check_cycle - check if a list have a cycle
 * @list: head from the list
 * Return: 1 if is a cycle, 0 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t *liebre, *tortuga;

	liebre = list;
	tortuga = list;

	while (liebre && tortuga && liebre->next)
	{
		liebre = liebre->next->next;
		tortuga = tortuga->next;
		
		if (liebre == tortuga)
			return (1);
	}
	return (0);
}
