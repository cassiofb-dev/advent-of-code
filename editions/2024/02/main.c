#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 1024

typedef struct node
{
    int value;
    int index;
    struct node *next;
    struct node *previous;
} node;

typedef struct linked_list
{
    node *head;
    node *tail;
} linked_list;

linked_list *create_linked_list()
{
    linked_list *list = (linked_list *)malloc(sizeof(linked_list));
    list->head = NULL;
    list->tail = NULL;
    return list;
}

void add_to_linked_list(linked_list *list, int value)
{
    node *new_node = (node *)malloc(sizeof(node));
    new_node->value = value;
    new_node->next = NULL;
    new_node->previous = NULL;

    if (!list->head)
    {
        new_node->index = 0;
        list->head = new_node;
        list->tail = new_node;
    }
    else
    {
        new_node->index = list->tail->index + 1;
        new_node->previous = list->tail;
        list->tail->next = new_node;
        list->tail = new_node;
    }
}

void remove_from_linked_list(linked_list *list, node *node)
{
    if (node->previous)
    {
        node->previous->next = node->next;
    }

    if (node->next)
    {
        node->next->previous = node->previous;
    }

    if (list->head == node)
    {
        list->head = node->next;
    }

    if (list->tail == node)
    {
        list->tail = node->previous;
    }

    free(node);
}

void remove_from_linked_list_by_index(linked_list *list, int index)
{
    node *current = list->head;

    if (index < 0)
    {
        return;
    }

    while (current)
    {
        if (current->index == index)
        {
            remove_from_linked_list(list, current);
            break;
        }

        current = current->next;
    }
}

linked_list *copy_linked_list(linked_list *list)
{
    linked_list *new_list = create_linked_list();
    node *current = list->head;
    while (current)
    {
        add_to_linked_list(new_list, current->value);
        current = current->next;
    }

    return new_list;
}

void free_linked_list(linked_list *list)
{
    node *current = list->head;
    while (current)
    {
        node *next = current->next;
        free(current);
        current = next;
    }

    free(list);
}

void print_linked_list(linked_list *list)
{
    node *current = list->head;
    while (current)
    {
        printf("(%d)->", current->value);
        current = current->next;
    }
    printf("\n");
}

int main(int argc, char const *argv[])
{
    FILE *file = fopen("editions/2024/02/input.txt", "r");
    if (!file)
    {
        printf("Error opening file\n");
        return EXIT_FAILURE;
    }

    int safe_reports = 0;
    int fixed_reports = 0;
    char line[MAX_LINE_LENGTH] = {0};
    while (fgets(line, sizeof(line), file))
    {
        line[strcspn(line, "\r\n")] = 0;

        linked_list *list = create_linked_list();
        char *value = strtok(line, " ");
        while (value)
        {
            add_to_linked_list(list, atoi(value));
            value = strtok(NULL, " ");
        }

        for (int remove_index = -1; remove_index <= list->tail->index; remove_index++)
        {
            linked_list *aux_list = copy_linked_list(list);
            remove_from_linked_list_by_index(aux_list, remove_index);

            int is_report_safe = 1;
            node *current = aux_list->head;
            while (current->next)
            {
                node *next = current->next;
                int delta = next->value - current->value;

                if (delta == 0 || abs(delta) > 3)
                {
                    is_report_safe = 0;
                    break;
                }

                if (current->previous)
                {
                    node *previous = current->previous;
                    int previous_delta = current->value - previous->value;
                    if (delta * previous_delta < 0)
                    {
                        is_report_safe = 0;
                        break;
                    }
                }

                current = next;
            }

            free_linked_list(aux_list);
            if (is_report_safe)
            {
                if (remove_index == -1)
                {
                    safe_reports++;
                }
                else
                {
                    fixed_reports++;
                }
                break;
            }
        }

        free_linked_list(list);
    }

    fclose(file);

    printf("Part 01: %d\n", safe_reports);
    printf("Part 02: %d\n", safe_reports + fixed_reports);

    return 0;
}
