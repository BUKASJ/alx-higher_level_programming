#include <Python.h>

/**
 * print_python_list - Prints information about a Python list
 * @p: Pointer to a PyObject representing a Python list
 */

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid PyListObject\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)p)->ob_size);

	setbuf(stdout, NULL);

	for (Py_ssize_t i = 0; i < ((PyVarObject *)p)->ob_size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to a PyObject representing a Python bytes object
 */

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid PyBytesObject\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_GET_SIZE(p));

	setbuf(stdout, NULL);

	printf("  trying string: %s\n", PyBytes_AS_STRING(p));
	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < PyBytes_GET_SIZE(p) && i < 10; ++i)
	{
		printf("%02hhx", PyBytes_AS_STRING(p)[i]);
		if (i < 9)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: Pointer to a PyObject representing a Python float object
 */

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Invalid PyFloatObject\n");
		return;
	}

	printf("[.] float object info\n");

	setbuf(stdout, NULL);

	printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
