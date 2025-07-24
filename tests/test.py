import time

from AutoCAD import AutoCAD, APoint

acad = AutoCAD()
time.sleep(1)
acad.open_file("D:/jones/Jones/test.DWG")
time.sleep(1)
# Collect all block references
blocks = list(acad.iter_objects("AcDbBlockReference"))

# Print details about the blocks
for block in blocks:
    print(f"Block Name: {block.Name}, Insertion Point: {block.InsertionPoint}")
    time.sleep(1)
    if not block.Name == "A$C625fddc0":
        acad.move_object(block, APoint(150, 150, 0))
        time.sleep(1)
        min_point, max_point = acad.get_block_extents(block.Name)
        print(f"min : {min_point} max : {max_point}")
        acad.add_rectangle(max_point, min_point)
        acad.add_overall_dimensions(block)
        acad.zoom_to_object(block)
