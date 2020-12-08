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

	if (!*head)
	{
		*head = malloc(sizeof(listint_t));
		if (*head == NULL)
			return (NULL);
		(*head)->n = number;
		(*head)->next = NULL;
		return (*head);
	}

	temp = *head;

	while (temp)
	{
		if (number > temp->next->n && number > temp->n)
			temp = temp->next;
		else
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
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
