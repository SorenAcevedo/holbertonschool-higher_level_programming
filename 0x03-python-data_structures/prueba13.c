#include "lists.h"

/**
 * len_list - calculate len of list
 * @head: head
 * Return: len
 */
int len_list(listint_t **head)
{
	listint_t *temp = *head;
	int i = 0;

	while (temp)
	{
		temp = temp->next;
		i++;
	}
	return (i);
}

/**
 * is_palindrome - check if a list is palindrome
 * @head: pointer to head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int i = 0, j = 0, k;
	int *arr;


	i = len_list(head);
	if (i == 0 || i == 1)
		return (1);
	arr = malloc(sizeof(int) * i);

	while (temp)
	{
		if (j < i)
			arr[j] = temp->n;
		temp = temp->next;
		j++;
	}
	k = j--;
	for (i = 0; j > k / 2; i++, j--)
	{
		if (arr[i] != arr[j])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
