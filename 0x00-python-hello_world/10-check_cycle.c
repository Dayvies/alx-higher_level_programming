#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check if list has loop
 * @list : list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list, *second = list;

	if (!list)
		return (0);
	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (second == first)
			return (1);
	}
	return (0);
}
