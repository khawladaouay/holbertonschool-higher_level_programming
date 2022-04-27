#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: number of nodes
 */
int check_cycle(listint_t *list)
{
listint_t *fast = list;
listint_t *slow = list;
while (slow && fast && fast->next)
{
	slow = slow->next;
	fast = fast->next->next;
	if (slow == fast)
	{
		return (1);
	}
	}
	return (0);
}
