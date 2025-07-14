.. AutoCAD Python Library documentation master file.

################################
AutoCAD Python Library
################################

.. raw:: html

   <p align="center">
     <img src="https://i.postimg.cc/xjBy2P1f/acadlib.png" alt="acadlib.png" width="400"/>
   </p>

Welcome to the official documentation for the AutoCAD Python Library. This library provides a powerful and intuitive interface for automating Autodesk AutoCAD from your Python applications. By leveraging the COM interface, it allows for the programmatic creation, manipulation, and management of AutoCAD drawings and objects with ease.

.. raw:: html

    <p align="center">
        <a href="https://pypi.org/project/AutoCAD/" target="_blank"><img alt="PyPI version" src="https://img.shields.io/pypi/v/AutoCAD?style=for-the-badge&logo=pypi&color=blue"></a>
        <a href="https://pepy.tech/project/AutoCAD" target="_blank"><img alt="Downloads" src="https://static.pepy.tech/badge/AutoCAD?style=for-the-badge&logo=pypi&color=green"></a>
        <a href="https://github.com/Jones-peter/AutoCAD/blob/master/LICENSE" target="_blank"><img alt="License" src="https://img.shields.io/github/license/Jones-peter/AutoCAD?style=for-the-badge&color=lightgrey"></a>
    </p>
    <p align="center">
        <a href="https://github.com/Jones-peter" target="_blank"><img src="https://img.shields.io/badge/GitHub-Jones--peter-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
        <a href="https://www.instagram.com/jones_peter__/" target="_blank"><img src="https://img.shields.io/badge/Instagram-jones__peter__-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"></a>
        <a href="https://www.linkedin.com/in/jones-peter-121157221/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-Jones--Peter-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
        <a href="https://jonespeter.site" target="_blank"><img src="https://img.shields.io/badge/Website-jonespeter.site-0078D4?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website"></a>
    </p>


.. toctree::
   :maxdepth: 2
   :caption: Documentation Contents

   self
   getting_started
   api_reference
   contributing

.. _getting_started:

***************
Getting Started
***************

Installation
============

To get started, install the library using pip:

.. code-block:: bash

   pip install AutoCAD

.. note::
   This library requires a local installation of Autodesk AutoCAD to function, as it communicates directly with the AutoCAD application.

Basic Initialization
====================

Begin by importing and initializing the main ``AutoCAD`` class. This will establish a connection with the running AutoCAD instance or launch a new one.

.. code-block:: python

   from AutoCAD import AutoCAD, APoint

   # Connect to AutoCAD
   cad = AutoCAD()

   # You can now access the application, document, and model space
   print(f"Connected to: {cad.app.Name}")
   print(f"Active Document: {cad.doc.Name}")


.. _api_reference:

*************
API Reference
*************

This section provides a detailed overview of the library's features and functionalities.

Object Creation 🪄
==================

Create various 2D objects in the model space.

.. code-block:: python

   # Add a Circle
   center_pt = APoint(10, 10)
   circle = cad.add_circle(center_pt, radius=5)

   # Add a Line
   start_pt = APoint(0, 0)
   end_pt = APoint(20, 0)
   line = cad.add_line(start_pt, end_pt)

   # Add a Rectangle
   lower_left = APoint(0, 0)
   upper_right = APoint(10, 5)
   rectangle = cad.add_rectangle(lower_left, upper_right)

   # Add an Ellipse
   ellipse_center = APoint(5, 5)
   major_axis_pt = APoint(10, 0) # This defines the direction and length of the major axis
   ellipse = cad.add_ellipse(ellipse_center, major_axis_pt, ratio=0.5)

   # Add Text and MText
   from AutoCAD import Text
   text_obj = Text("Hello, AutoCAD!", APoint(5, 5), 2.5)
   cad.add_text(text_obj)

   # Add a Polyline
   points = [APoint(0, 0), APoint(5, 5), APoint(10, 0)]
   polyline = cad.add_polyline(points)

   # Add a Spline
   spline_points = [APoint(0, 5), APoint(5, 10), APoint(10, 5)]
   spline = cad.add_spline(spline_points)

   # Add an Arc
   arc_center = APoint(15, 15)
   arc = cad.add_arc(arc_center, radius=5, start_angle=0, end_angle=180)

   # Add a Table
   from AutoCAD import Table, Alignment
   data = [
       ["Row 1, Col 1", "Row 1, Col 2"],
       ["Row 2, Col 1", "Row 2, Col 2"]
   ]
   headers = ["Header 1", "Header 2"]
   table = Table(
       insertion_point=APoint(30, 30),
       data=data,
       headers=headers,
       title="My Custom Table",
       col_widths=[30, 30],
       text_height=2.0,
       alignment=Alignment.CENTER
   )
   cad.add_table(table)


Layer Management 🧩
====================

Full control over document layers.

.. code-block:: python

   from AutoCAD import Layer, Color

   # Create a new layer
   new_layer = Layer("MyLayer", Color.RED)
   cad.create_layer(new_layer)

   # Set the new layer as active
   cad.set_active_layer("MyLayer")

   # Lock a layer
   cad.lock_layer("MyLayer", lock=True)

   # Change layer color
   cad.change_layer_color("MyLayer", Color.BLUE)

   # Delete a layer
   cad.delete_layer("MyLayer")


Block Operations 🧱
==================

Work with blocks and their attributes.

.. code-block:: python

   from AutoCAD import BlockReference

   # Insert a block that already exists in the drawing
   block = BlockReference("MyBlockName", APoint(5, 5))
   block_ref = cad.insert_block(block)

   # Insert a block from an external .dwg file
   block_from_file = cad.insert_block_from_file("C:/path/to/your/block.dwg", APoint(15, 15))

   # Modify a block attribute
   cad.modify_block_attribute(block_ref, "ATTRIBUTE_TAG", "New Value")

   # Export an internal block to a file
   cad.export_block_to_file("MyBlockName", "C:/path/to/export.dwg")


Object Manipulation 🛠️
=======================

Modify, move, and transform existing objects.

.. code-block:: python

   # Move an object
   cad.move_object(circle, APoint(20, 20))

   # Scale an object
   base_point = APoint(5, 5)
   cad.scale_object(circle, base_point, scale_factor=2.0)

   # Rotate an object (angle in degrees)
   cad.rotate_object(line, base_point, rotation_angle=45)

   # Explode a complex object into simpler entities
   exploded_items = cad.explode_object(rectangle)

   # Delete an object
   cad.delete_object(circle)


User Interaction 🧑‍💻
====================

Prompt the user for input directly within AutoCAD.

.. code-block:: python

   # Get a point from the user
   user_point = cad.get_user_input_point("Select a location for the new circle")
   if user_point:
       cad.add_circle(user_point, 5)

   # Get a string from the user
   user_string = cad.get_user_input_string("Enter a label for the object")

   # Show a message to the user
   cad.show_message("Operation completed successfully!")


Document Management 📃
========================

Control the drawing file itself.

.. code-block:: python

   # Purge all unused elements (layers, blocks, etc.)
   cad.purge()

   # Save the current document
   cad.save()

   # Save the document with a new name
   cad.save_as("C:/drawings/MyNewDrawing.dwg")

   # Open an existing file
   cad.open_file("C:/drawings/AnotherDrawing.dwg")

   # Close the current document
   cad.close(save_changes=True)


View Management 🔍
===================

Control the camera and zoom.

.. code-block:: python

   # Zoom to show all objects in the drawing
   cad.zoom_extents()

   # Zoom to a specific object
   cad.zoom_to_object(line)


Error Handling ❌
=================

The library uses a custom ``CADException`` for handling errors gracefully. It's recommended to wrap your calls in a try...except block.

.. code-block:: python

   try:
       # This will fail if the layer doesn't exist
       cad.set_active_layer("NonExistentLayer")
   except Exception as e:
       print(f"An error occurred: {e}")


.. _contributing:

*****************
Contributing
*****************

Contributions are welcome! Whether you're fixing a bug, adding a feature, or improving documentation, your help is appreciated.

Reporting Bugs 🪲
================

If you find a bug, please `open an issue on GitHub <https://github.com/Jones-peter/AutoCAD/issues>`_.
Please include:

* Your version of AutoCAD.
* A clear description of the bug.
* Steps to reproduce the behavior.
* A minimal, reproducible code snippet.

Suggesting Enhancements 💭
=========================

Have an idea for a new feature? Feel free to `open an issue <https://github.com/Jones-peter/AutoCAD/issues>`_ to start a discussion.

License 🔒
=========

This project is licensed under the MIT License. See the `LICENSE <https://github.com/Jones-peter/AutoCAD/blob/master/LICENSE>`_ file for details.

Contact & Credits
=================

For questions or support, please contact `jonespetersoftware@gmail.com <mailto:jonespetersoftware@gmail.com>`_.
my web page `jonespeter.site <https://jonespeter.site/>`_.

.. seealso::
   This project was inspired by the excellent work in the `pyautocad <https://github.com/reclosedev/pyautocad>`_ and `AutoCAD <https://github.com/manufino/AutoCAD>`_ repositories.

.. note::
   This project is independently developed and is not affiliated with, authorized, maintained, sponsored, or endorsed by Autodesk, Inc.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
