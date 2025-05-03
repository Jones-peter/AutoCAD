.. AutoCAD Module documentation master file

AutoCAD Python Module
=====================

.. image:: https://img.shields.io/github/stars/YOUR_GITHUB_HANDLE/AutoCAD
   :target: https://github.com/YOUR_GITHUB_HANDLE/AutoCAD
.. image:: https://img.shields.io/github/followers/YOUR_GITHUB_HANDLE?label=Follow&style=social
   :target: https://github.com/YOUR_GITHUB_HANDLE

GitHub | Instagram | LinkedIn
------------------------------

.. image:: upi_qr_code.png
   :width: 200px
   :align: center

**Donate with PayPal or UPI**

If you like this project and want to support me, consider making a donation.

Overview
--------

The AutoCAD module provides a comprehensive interface for interacting with AutoCAD through Python. It leverages the COM client to automate tasks within AutoCAD, allowing for efficient manipulation of drawings and objects.

Features
--------

- Object Creation: Circles, lines, rectangles, ellipses, text, dimensions, points, polylines, splines, arcs, etc.
- Layer Management: Create, delete, lock/unlock, and modify layers.
- Block Operations: Insert, export, and modify blocks and their attributes.
- Group Management: Manage object groups with ease.
- User Interaction: Input points, strings, and integers from users.
- Error Handling: Custom exception handling for AutoCAD-related errors.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install AutoCAD

Usage
-----

**Initialization**

.. code-block:: python

   from AutoCAD import AutoCAD
   cad = AutoCAD()

**Object Creation Examples**

.. code-block:: python

   center = APoint(10, 10, 0)
   circle = cad.add_circle(center, 5)

   line = cad.add_line(APoint(0, 0, 0), APoint(10, 0, 0))

   rectangle = cad.add_rectangle(APoint(0, 0, 0), APoint(10, 5, 0))

   ellipse = cad.add_ellipse(APoint(5, 5, 0), APoint(10, 0, 0), 0.5)

   text = Text("Hello, AutoCAD!", APoint(5, 5, 0), 2.5)
   cad.add_text(text)

   dimension = Dimension(APoint(0, 0, 0), APoint(10, 0, 0), APoint(5, -2, 0), DimensionType.ALIGNED)
   cad.add_dimension(dimension)

   polyline = cad.add_polyline([APoint(0, 0, 0), APoint(5, 5, 0), APoint(10, 0, 0)])

   arc = cad.add_arc(APoint(5, 5, 0), 5, 0, 180)

**Layer Management**

.. code-block:: python

   layer = Layer("MyLayer", Color.RED)
   cad.create_layer(layer)
   cad.set_active_layer("MyLayer")
   cad.set_layer_visibility("MyLayer", visible=False)
   cad.lock_layer("MyLayer", True)
   cad.change_layer_color("MyLayer", Color.BLUE)
   cad.set_layer_linetype("MyLayer", "Dashed")

**Block Operations**

.. code-block:: python

   block = BlockReference("BlockName", APoint(5, 5, 0))
   cad.insert_block(block)

   cad.modify_block_attribute(block, "TagName", "NewValue")

   cad.export_block_to_file("BlockName", "path/to/export.dwg")

**Group Management**

.. code-block:: python

   group = cad.create_group("MyGroup", [circle, line])
   cad.add_to_group("MyGroup", [rectangle])

**User Interaction**

.. code-block:: python

   user_point = cad.get_user_input_point("Pick a point")
   cad.show_message("Operation completed!")

**Document Management**

.. code-block:: python

   cad.save_as("drawing.dwg")
   cad.open_file("drawing.dwg")
   cad.close(save_changes=True)

**Object Manipulation**

.. code-block:: python

   cad.move_object(circle, APoint(20, 20, 0))
   cad.rotate_object(circle, APoint(5, 5, 0), 90)

Error Handling
--------------

All methods raise `CADException` on errors with helpful messages.

Contributing
------------

Contributions are welcome! Fork the repo and submit a pull request.

License
-------

This project is licensed under the **MIT License**.

Contact
-------

For support or inquiries, email: **jonespetersoftware@gmail.com**

Credits
-------

- Based on ideas from `manufino/AutoCAD`
- Uses principles from `reclosedev/pyautocad`

