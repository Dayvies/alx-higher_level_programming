#include "lists.h"
/**
 * insert_node - insert in sorted listint_t
 * @head : head
 * @number : number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *temp;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	while (current->next != NULL)
	{
		temp = current;
		current = current->next;
		if (number < current->n)
		{
			temp->next = new;
			new->next = current;
			return (new);
		}
	}
	current->next = new;
	return (new);
}
