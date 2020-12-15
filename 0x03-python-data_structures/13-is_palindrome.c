#include "lists.h"

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

	if (*head == NULL)
		return (1);
	arr = malloc(sizeof(int) * 1024);

	while (temp)
	{
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
