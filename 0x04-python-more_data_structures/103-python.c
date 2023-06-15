#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: Pointer to the PyObject representing the list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;

	if (!PyList_Check(p))
	{
		printf("Invalid Python list object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the list = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to the PyObject representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	char *bytes_str;

	if (!PyBytes_Check(p))
	{
		printf("Invalid Python bytes object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  Size: %ld\n", size);
	printf("  Trying string: %s\n", PyBytes_AsString(p));

	if (size > 10)
	{
		size = 10;
	}

	bytes_str = PyBytes_AsString(p);
	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes_str[i]);
		if (i != size - 1)
		{
			printf(" ");
		}
	}
	printf("\n");
}

