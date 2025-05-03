
.. AutoCAD Module Documentation

Welcome to the AutoCAD Module documentation. This module provides a comprehensive interface for automating tasks within AutoCAD through Python, leveraging the COM client for seamless interaction.

.. image:: https://i.postimg.cc/8C07zdcr/upi-1.png
   :alt: UPI QR Code
   :align: center
   :width: 120px

.. table:: Support

   ================================  =======================================================
   **GitHub**                      | `Jones-peter <https://github.com/Jones-peter>`_
   **Instagram**                    | `@jones_peter__ <https://www.instagram.com/jones_peter__/`
   **LinkedIn**                     | `Jones-Peter <https://www.linkedin.com/in/jones-peter-121157221/>`
   ================================  =======================================================
   
   .. raw:: html

      <table>
        <tr>
          <td style="padding-left: 20px; vertical-align: middle;">
            <a href="https://www.paypal.me/jonespeter22">
              <img src="https://img.shields.io/badge/jonespeter22-PayPal-blue?logo=paypal&logoColor=white" alt="Donate with PayPal"/>
            </a><br><br>
            <p>If you like this project and want to support me, consider making a donation.</p>
          </td>
        </tr>
      </table>

Contents:

- **Overview**
- **Features**
- **Installation**
- **Usage**
  - Initialization
  - Object Creation
  - Layer Management
  - Block Operations
  - Group Management
  - User Interaction
  - Document Management
  - Object Manipulation
  - Error Handling
- **Contributing**
- **License**
- **Credits**
- **Contact**

Overview
========

The `AutoCAD` module provides an interface to automate tasks within AutoCAD, allowing users to create and manipulate AutoCAD objects through Python. 

Features
========

- **Object Creation**: Create circles, lines, rectangles, ellipses, text objects, dimensions, points, polylines, splines, arcs, and more.
- **Layer Management**: Create, delete, lock/unlock, and modify layers.
- **Block Operations**: Insert, export, and modify blocks and their attributes.
- **Group Management**: Manage groups of objects.
- **User Interaction**: Request point, string, and integer inputs from the user.
- **Error Handling**: Custom exception handling for AutoCAD-related errors.

Installation
============

To install the `AutoCAD` module, ensure you have Python installed along with the necessary packages:

```bash
pip install AutoCAD
```

Usage
======

### Initialization

To start using the module, initialize the `AutoCAD` class:

```python
from AutoCAD import AutoCAD

cad = AutoCAD()
```

### Object Creation

- **add_circle(center, radius)**: Adds a circle to the model space.

```python
center = APoint(10, 10, 0)
radius = 5
circle = cad.add_circle(center, radius)
```

- **add_line(start_point, end_point)**: Adds a line to the model space.

```python
start_point = APoint(0, 0, 0)
end_point = APoint(10, 0, 0)
line = cad.add_line(start_point, end_point)
```

Refer to the full documentation for all object creation methods like `add_rectangle()`, `add_ellipse()`, `add_text()`, etc.

### Layer Management

The module allows you to manage layers with functions like `create_layer()`, `delete_layer()`, and `set_layer_visibility()`. You can create layers, set visibility, change color, and more.

### Block Operations

You can insert, export, and modify AutoCAD blocks with functions like `insert_block()`, `export_block_to_file()`, and `modify_block_attribute()`.

### User Interaction

Request inputs from users for points, strings, and integers with methods like `get_user_input_point()`, `get_user_input_string()`, and `get_user_input_integer()`.

### Document Management

Functions such as `save_as()`, `open_file()`, and `close()` help manage AutoCAD documents.

Contributing
============

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

License
=======

This project is licensed under the MIT License.

Credits
=======

This project is inspired by and builds upon the work from the following repositories:

- [AutoCAD by manufino](https://github.com/manufino/AutoCAD)
- [pyautocad by reclosedev](https://github.com/reclosedev/pyautocad)

Contact
=======

For any questions or support, please contact [jonespetersoftware@gmail.com](mailto:jonespetersoftware@gmail.com).
