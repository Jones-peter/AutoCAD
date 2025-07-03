import time

from AutoCAD import AutoCAD, APoint

acad = AutoCAD()
time.sleep(1)
acad.open_file("D:/jones/Jones/USTS_WHEELSENSOR_SHEET.DWG")
time.sleep(1)
# Collect all block references
blocks = list(acad.iter_objects("AcDbBlockReference"))

# Print details about the blocks
for block in blocks:
    print(f"Block Name: {block.Name}, Insertion Point: {block.InsertionPoint}")
    time.sleep(2)
    if not block.Name == "A$C625fddc0":
        acad.move_object(block, APoint(0, 0, 0))