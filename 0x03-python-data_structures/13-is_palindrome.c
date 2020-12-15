#include "lists.h"

/**
 * is_palindrome - check if a list is palindrome
 * @head: pointer to head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int i, j = 0, k;
	int arr[1024];

	if (!*head)
		return (1);
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
			return (0);
	}
	return (1);
}
