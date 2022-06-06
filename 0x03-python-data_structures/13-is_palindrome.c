#include "lists.h"
/**
 * is_palindrome - check if list is palindrome
 * @head: first node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *p, *prev;
	listint_t *rev = malloc(sizeof(listint_t));

	current = *head;
	if (current == NULL || current->next == NULL)
	{
		free(rev);
		return (1);
	}
	rev->n = current->n;
	current = current->next;
	while (current != NULL)
	{
		p = malloc(sizeof(listint_t));
		p->next = rev;
		p->n = current->n;
		rev = p;
		current = current->next;
	}
	current = *head;
	prev = p;
	while (current != NULL)
	{
		if (current->n != p->n)
		{
			free_listint(prev);
			return (0);
		}
		current = current->next;
		p = p->next;
	}
	free_listint(prev);
	return (1);
}
