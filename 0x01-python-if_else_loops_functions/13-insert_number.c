#include "lists.h"
/**
 * insert_node - Entry Point
 * @head: double pointer param for listint_t
 * @number: param for int
 * Return: listint_t
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = NULL;
    listint_t *current = *head;
    listint_t *prev = NULL;

    if (head == NULL)
        return (NULL);

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;
    while (current != NULL && current->n < number)
    {
        prev = current;
        current = current->next;
    }
    new_node->next = current;

    if (prev != NULL)
        prev->next = new_node;
    else
        *head = new_node;

    return (new_node);
}
