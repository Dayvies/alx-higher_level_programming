#include "lists.h"
/**
 * is_palindrome - check if list is palindrome
 * @head: first node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int count = 1, i, j, *b, *bnew;

	current = *head;
	if (current == NULL || current->next == NULL)
		return (1);
	b = malloc(1000 * sizeof(int));
	b[0] = current->n;
	while (current->next)
	{
		current = current->next;
		b[count] = current->n;
		count += 1;
	}
	bnew = realloc(b, sizeof(int) * count);
	j = count - 1;
	for (i = 0; i < count / 2; i++)
	{
		if (bnew[i] != bnew[j])
		{
			free(bnew);
			return (0);
		}
		j--;
	}
	free(bnew);
	return (1);
}
