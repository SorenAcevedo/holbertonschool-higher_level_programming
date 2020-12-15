#include "lists.h"
/**
 * is_palindrome - check if a list is palindrome
 * @head: pointer to head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i = 0, j = 0;
	int *arr;

	temp = *head;

	while (temp)
	{
		temp = temp->next;
		i++;
	}
	temp = *head;

	if (i == 0 || i == 1)
		return (1);
	arr = malloc(sizeof(int) * i);

	while (temp)
	{
		arr[j] = temp->n;
		temp = temp->next;
		j++;
	}
	j--;
	for (i = 0; arr[i + 1]; i++, j--)
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
