#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_listint - Entry point
 * @head: double pointer param for listint_t
 * Return: listint_t
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next = NULL;
    
    while (current) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return (prev);
}

/**
 * is_palindrome - entry point
 * @head: double pointer param for listint_t
 * Return: int
 */
int is_palindrome(listint_t **head)
{
    listint_t *tmp, *rev, *mid;
    size_t size = 0, i;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    tmp = *head;
    while (tmp)
    {
        size++;
        tmp = tmp->next;
    }

    tmp = *head;
    for (i = 0; i < (size / 2) - 1; i++)
        tmp = tmp->next;

    if ((size % 2) == 0 && tmp->n != tmp->next->n)
        return (0);

    tmp = tmp->next->next;
    rev = reverse_listint(&tmp);
    mid = rev;

    tmp = *head;
    while (rev)
    {
        if (tmp->n != rev->n)
            return (0);
        tmp = tmp->next;
        rev = rev->next;
    }

    reverse_listint(&mid);
    return (1);
}
