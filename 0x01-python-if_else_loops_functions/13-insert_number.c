#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - insert node
 * @head: head of the list
 * @number: number of the node
 * Return: The address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	temp = *head;
	while (temp)
	{
		if (temp->next == NULL)
		{
			temp->next = new;
			new->next = NULL;
			return (new);
		}
		if (number > temp->next->n)
			temp = temp->next;
		else
		{
			if (temp == *head)
			{
				new->next = temp;
				*head = new;
			}
			else
			{
				new->next = temp->next;
				temp->next = new;
			}
			return (new);
		}
	}
	return (NULL);
}
