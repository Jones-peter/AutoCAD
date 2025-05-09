
![Banner](./images/banner.png)

# AutoCAD Module

[![GitHub](https://img.shields.io/badge/GitHub-Jones--peter-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Jones-peter)  [![Instagram](https://img.shields.io/badge/Instagram-jones__peter__-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/jones_peter__/)  [![LinkedIn](https://img.shields.io/badge/LinkedIn-Jones--Peter-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jones-peter-121157221/)  [![Website](https://img.shields.io/badge/Website-jonespeter.site-0078D4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://jonespeter.site)



<table>
  <tr>
    <td>
      <img src="https://i.postimg.cc/8C07zdcr/upi-1.png" alt="UPI QR Code" width="120"/>
      <p style="text-align: center;"><b>Scan to Pay</b></p>
    </td>
    <td style="padding-left: 20px; vertical-align: middle;">
      <a href="https://www.paypal.me/jonespeter22">
        <img src="https://img.shields.io/badge/jonespeter22-PayPal-blue?logo=paypal&logoColor=white" alt="Donate with PayPal"/>
      </a><br><br>
      <p>If you like this project and want to support me, consider making a donation.</p>
    </td>
  </tr>
</table>

## Overview

The `AutoCAD` module provides a comprehensive interface for interacting with AutoCAD through Python. It leverages the COM client to automate tasks within AutoCAD, allowing for efficient manipulation of drawings and objects.

## Features

- **Object Creation**: Create circles, lines, rectangles, ellipses, text objects, dimensions, points, polylines, splines, arcs, and more.
- **Layer Management**: Create, delete, lock/unlock, and modify layers.
- **Block Operations**: Insert, export, and modify blocks and their attributes.
- **Group Management**: Create, add to, remove from, and select groups of objects.
- **User Interaction**: Request point, string, and integer inputs from the user.
- **Error Handling**: Custom exception handling for AutoCAD-related errors.

## Installation

Ensure you have Python installed along with the necessary packages:

```bash
pip install AutoCAD
```

## Usage

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

- **add_rectangle(lower_left, upper_right)**: Adds a rectangle to the model space.

  ```python
  lower_left = APoint(0, 0, 0)
  upper_right = APoint(10, 5, 0)
  rectangle = cad.add_rectangle(lower_left, upper_right)
  ```

- **add_ellipse(center, major_axis, ratio)**: Adds an ellipse to the model space.

  ```python
  center = APoint(5, 5, 0)
  major_axis = APoint(10, 0, 0)
  ratio = 0.5
  ellipse = cad.add_ellipse(center, major_axis, ratio)
  ```

- **add_text(text)**: Adds a text object to the model space.

  ```python
  text = Text("Hello, AutoCAD!", APoint(5, 5, 0), 2.5)
  text_obj = cad.add_text(text)
  ```

- **add_dimension(dimension)**: Adds a dimension to the model space.

  ```python
  dimension = Dimension(APoint(0, 0, 0), APoint(10, 0, 0), APoint(5, -2, 0), DimensionType.ALIGNED)
  dimension_obj = cad.add_dimension(dimension)
  ```

- **add_point(point)**: Adds a point to the model space.

  ```python
  point = APoint(5, 5, 0)
  point_obj = cad.add_point(point)
  ```

- **add_polyline(points)**: Adds a polyline to the model space.

  ```python
  points = [APoint(0, 0, 0), APoint(5, 5, 0), APoint(10, 0, 0)]
  polyline = cad.add_polyline(points)
  ```

- **add_spline(points)**: Adds a spline to the model space.

  ```python
  points = [APoint(0, 0, 0), APoint(5, 5, 0), APoint(10, 0, 0)]
  spline = cad.add_spline(points)
  ```

- **add_arc(center, radius, start_angle, end_angle)**: Adds an arc to the model space.

  ```python
  center = APoint(5, 5, 0)
  radius = 5
  start_angle = 0
  end_angle = 180
  arc = cad.add_arc(center, radius, start_angle, end_angle)
  ```

### Layer Management

- **create_layer(layer)**: Creates a new layer.

  ```python
  layer = Layer("MyLayer", Color.RED)
  new_layer = cad.create_layer(layer)
  ```

- **set_active_layer(layer_name)**: Sets the active layer.

  ```python
  cad.set_active_layer("MyLayer")
  ```

- **set_layer_visibility(layer_name, visible=True)**: Sets the visibility of a layer.

  ```python
  cad.set_layer_visibility("MyLayer", visible=False)
  ```

- **lock_layer(layer_name, lock=True)**: Locks or unlocks a layer.

  ```python
  cad.lock_layer("MyLayer", lock=True)
  ```

- **delete_layer(layer_name)**: Deletes a layer.

  ```python
  cad.delete_layer("MyLayer")
  ```

- **change_layer_color(layer_name, color)**: Changes the color of a layer.

  ```python
  cad.change_layer_color("MyLayer", Color.BLUE)
  ```

- **set_layer_linetype(layer_name, linetype_name)**: Sets the linetype of a layer.

  ```python
  cad.set_layer_linetype("MyLayer", "Dashed")
  ```

### Block Operations

- **insert_block(block)**: Inserts a block into the model space.

  ```python
  block = BlockReference("BlockName", APoint(5, 5, 0))
  block_ref = cad.insert_block(block)
  ```

- **get_block_extents(block_name)**: Gets the maximum extents of a block.

  ```python
  min_point, max_point = cad.get_block_extents("BlockName")
  ```

- **get_block_coordinates(block_name)**: Gets the insertion coordinates of a specific block.

  ```python
  block_coords = cad.get_block_coordinates("BlockName")
  ```

- **insert_block_from_file(file_path, insertion_point, scale=1.0, rotation=0.0)**: Inserts a block from a file.

  ```python
  block_ref = cad.insert_block_from_file("path/to/block.dwg", APoint(5, 5, 0))
  ```

- **export_block_to_file(block_name, file_path)**: Exports a block to a file.

  ```python
  cad.export_block_to_file("BlockName", "path/to/export.dwg")
  ```

- **modify_block_attribute(block_ref, tag, new_value)**: Modifies a block attribute.

  ```python
  cad.modify_block_attribute(block_ref, "TagName", "NewValue")
  ```

- **modify_block_attribute_by_old_value(block_ref, tag, old_value, new_value)**: Modifies a block attribute by old value.

  ```python
  cad.modify_block_attribute_by_old_value(block_ref, "TagName", "OldValue", "NewValue")
  ```

- **delete_block_attribute(block_ref, tag)**: Deletes a block attribute.

  ```python
  cad.delete_block_attribute(block_ref, "TagName")
  ```

### Group Management

- **create_group(group_name, objects)**: Creates a group of objects.

  ```python
  group = cad.create_group("MyGroup", [circle, line])
  ```

- **add_to_group(group_name, objects)**: Adds objects to a group.

  ```python
  cad.add_to_group("MyGroup", [rectangle])
  ```

- **remove_from_group(group_name, objects)**: Removes objects from a group.

  ```python
  cad.remove_from_group("MyGroup", [line])
  ```

- **select_group(group_name)**: Selects a group of objects.

  ```python
  group_items = cad.select_group("MyGroup")
  ```

### User Interaction

- **get_user_input_point(prompt="Select a point")**: Requests point input from the user.

  ```python
  user_point = cad.get_user_input_point("Select a point")
  ```

- **get_user_input_string(prompt="Enter a string")**: Requests string input from the user.

  ```python
  user_string = cad.get_user_input_string("Enter a string")
  ```

- **get_user_input_integer(prompt="Enter an integer")**: Requests integer input from the user.

  ```python
  user_integer = cad.get_user_input_integer("Enter an integer")
  ```

- **show_message(message)**: Displays a message to the user.

  ```python
  cad.show_message("Operation completed successfully.")
  ```

### Document Management

- **purge()**: Purges all unused elements in the active document.

  ```python
  cad.purge()
  ```

- **save_as(file_path)**: Saves the document with a new name.

  ```python
  cad.save_as("path/to/save.dwg")
  ```

- **save()**: Saves the active document.

  ```python
  cad.save()
  ```

- **close(save_changes=True)**: Closes the active document, optionally saving changes.

  ```python
  cad.close(save_changes=True)
  ```

- **open_file(file_path)**: Opens an existing file.

  ```python
  cad.open_file("path/to/open.dwg")
  ```

### Object Manipulation

- **explode_object(obj)**: Explodes an object or a set of joined objects.

  ```python
  exploded_items = cad.explode_object(circle)
  ```

- **delete_object(obj)**: Deletes an object.

  ```python
  cad.delete_object(circle)
  ```

- **clone_object(obj, new_insertion_point)**: Clones an object.

  ```python
  cloned_obj = cad.clone_object(circle, APoint(15, 15, 0))
  ```

- **modify_object_property(obj, property_name, new_value)**: Modifies a property of an object.

  ```python
  cad.modify_object_property(circle, "Radius", 10)
  ```

- **repeat_block_horizontally(block_name, total_length, block_length, insertion_point)**: Repeats a block horizontally until a specified length is reached.

  ```python
  cad.repeat_block_horizontally("BlockName", 100, 10, APoint(0, 0, 0))
  ```

- **move_object(obj, new_insertion_point)**: Moves an object.

  ```python
  cad.move_object(circle, APoint(20, 20, 0))
  ```

- **scale_object(obj, base_point, scale_factor)**: Scales an object.

  ```python
  cad.scale_object(circle, APoint(5, 5, 0), 2)
  ```

- **rotate_object(obj, base_point, rotation_angle)**: Rotates an object.

  ```python
  cad.rotate_object(circle, APoint(5, 5, 0), 90)
  ```

- **align_objects(objects, alignment=Alignment.LEFT)**: Aligns objects based on the specified alignment.

  ```python
  cad.align_objects([circle, line], Alignment.LEFT)
  ```

- **distribute_objects(objects, spacing)**: Distributes objects with specified spacing.

  ```python
  cad.distribute_objects([circle, line, rectangle], 5)
  ```

### Error Handling

The module includes custom error handling through the `CADException` class, which provides detailed error messages for AutoCAD-related operations.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License.

## Contact

For any questions or support, please contact [jonespetersoftware@gmail.com].

## Credits

This project was inspired by and builds upon the work from the following repositories:

- [AutoCAD by manufino](https://github.com/manufino/AutoCAD)
- [pyautocad by reclosedev](https://github.com/reclosedev/pyautocad)

> **Note**: This project is not affiliated with Autodesk AutoCAD in any way.