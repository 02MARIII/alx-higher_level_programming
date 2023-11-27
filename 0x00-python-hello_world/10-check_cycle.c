#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - Entry point
 * @h: const pointer for listint_t
 * Return: n
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current = h;
	size_t n = 0;

	while (current)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint - Entry point
 * @head: double pointer for listint_t
 * @n: const param for int
 * Return: listint_t
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 * free_listint - Entry point
 * @head: pointer param for listint_t
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
