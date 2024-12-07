#define PY_SSIZE_T_CLEAN
#include <python3.12/Python.h>
#include <stdlib.h>
#include <string.h>


static void matrix_multiplication(size_t n, double arr1[n][n], double arr2[n][n], double arr_result[n][n]) {
  for (size_t i = 0; i < n; i++) {
    for (size_t j = 0; j < n; j++) {
      arr_result[i][j] = 0.0;
      for (size_t t = 0; t < n; t++) {
        arr_result[i][j] += arr1[i][t] * arr2[t][j];
      }
    }
  }
}


static PyObject *foreign_matrix_power(PyObject *self, PyObject *args) {
    PyObject *matrix_obj;
    int power;

    if (!PyArg_ParseTuple(args, "O!i", &PyList_Type, &matrix_obj, &power)) {
        return NULL;
    }


    Py_ssize_t n = PyList_Size(matrix_obj);

    double(*matrix)[n] = malloc(n * n * sizeof(double));
    double(*result)[n] = malloc(n * n * sizeof(double));
    double(*temp)[n] = malloc(n * n * sizeof(double));

    for (Py_ssize_t i = 0; i < n; i++) {
        PyObject *row = PyList_GetItem(matrix_obj, i);
        for (Py_ssize_t j = 0; j < n; j++) {
            matrix[i][j] = PyFloat_AsDouble(PyList_GetItem(row, j));
        }
    }

    for (Py_ssize_t i = 0; i < n; i++) {
        for (Py_ssize_t j = 0; j < n; j++) {
            result[i][j] = (i == j) ? 1.0 : 0.0;
        }
    }

    while (power > 0) {
        if (power % 2 == 1) {
            matrix_multiplication(n, result, matrix, temp);
            memcpy(result, temp, n * n * sizeof(double));
        }
        matrix_multiplication(n, matrix, matrix, temp);
        memcpy(matrix, temp, n * n * sizeof(double));
        power /= 2;
    }

    PyObject *result_list = PyList_New(n);
    for (Py_ssize_t i = 0; i < n; i++) {
        PyObject *row = PyList_New(n);
        for (Py_ssize_t j = 0; j < n; j++) {
            PyList_SetItem(row, j, PyFloat_FromDouble(result[i][j]));
        }
        PyList_SetItem(result_list, i, row);
    }

    free(matrix);
    free(result);
    free(temp);

    return result_list;
}


static PyMethodDef MatrixMethods[] = {
    {"foreign_matrix_power",
     foreign_matrix_power, METH_VARARGS,
     "Raise a square matrix to a power."
    },
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef matrixmodule = {
    PyModuleDef_HEAD_INIT,
    "matrix_power",
    NULL,
    -1,

    MatrixMethods
};


PyMODINIT_FUNC PyInit_matrix_power(void) {
    return PyModule_Create(&matrixmodule);
}
