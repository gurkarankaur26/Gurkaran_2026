def are_lines_touching_or_overlapping(start1, end1, start2, end2):
    if (start1 <= start2 and start2 <= end1 and end1 <= end2) or (start1 <= start2 and start2 <=end1 and end1 <=end2):#overlap
        return True
    elif end1 == start2: #touch
        return True
    elif start1 < end1 and start2 < end2 and end1 != start1:
        return False
    
