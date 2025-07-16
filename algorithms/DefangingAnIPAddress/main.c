char *defangIPaddr(char *address)
{
    char *result;
    int i, count = 0;

    for (i = 0; address[i] != '\0'; i++)
    {
        if (strstr(&address[i], ".") == &address[i])
        {
            count++;
            i += strlen(".") - 1;
        }
    }

    result = (char *)malloc(i + count * (strlen("[.]") - strlen(".")) + 1);

    i = 0;
    while (*address)
    {
        if (strstr(address, ".") == address)
        {
            strcpy(&result[i], "[.]");
            i += strlen("[.]");
            address += strlen(".");
        }
        else
            result[i++] = *address++;
    }

    result[i] = '\0';
    return result;
}
