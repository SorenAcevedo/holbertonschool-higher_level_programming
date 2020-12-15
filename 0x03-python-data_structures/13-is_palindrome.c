#include "lists.h"
/**
 * is_palindrome - check if a list is palindrome
 * @head: pointer to head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i = 0, j;
	int *arr;

	temp = *head;

	while (temp)
	{
		temp = temp->next;
		i++;
	}
	temp = *head;
	j = i;
	i = 0;

	if (i == 0 || i == 1)
		return (1);
	arr = malloc(sizeof(int) * i);

	while (temp)
	{
		arr[i] = temp->n;
		temp = temp->next;
		i++;
	}
	for (i = 0; i < j / 2; i++, j--)
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
