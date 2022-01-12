import laspy
from laspy.file import File  # las文件读取
import numpy as np

def get_pcd_header(width, points, format=1):
    if format == 1:
        return '\n'.join(["VERSION 0.7",
        "FIELDS x y z intensity",
        "SIZE 8 8 8 8",
        "TYPE F F F F",
        "COUNT 1 1 1 1",
        "WIDTH %s" % (width),
        "HEIGHT 1",
        "VIEWPOINT 0.0 0.0 0.0 1.0 0.0 0.0 0.0",
        "POINTS %s" % (points),
        "DATA ascii\n"])

 # las读取转为 pcd的cloud形式，只保留 XYZI
def getCloud():
    file = r"D:/pcd/1001140020191217.las"
    f = File(file, mode='r')
    inFile = np.vstack((f.x, f.y, f.z, f.intensity)).transpose()
    # cloud = pcl.PointCloud_PointXYZI()
    # cloud.from_array(np.array(inFile, dtype=np.float32))
    f.close()

    # return cloud

def print_las_info(las_file):
    las = laspy.read(las_file)
    mins = las.header.mins
    maxs = las.header.maxs
    print("mins: ", mins[0], mins[1], mins[2])
    print("maxs", maxs[0], maxs[1], maxs[2])
    scales = las.header.scales
    offsets = las.header.offsets
    print("scales: ", scales)
    print("offsets: ", offsets)
    point_count = las.header.point_count
    print("point_count", point_count)
    point_format = las.point_format
    dim_names = point_format.dimension_names
    print("dim_names: ", list(dim_names))

def to_pcd(las_file, out_pcd_file):
    f = laspy.read(las_file)
    point_count = f.header.point_count
    header = get_pcd_header(point_count, point_count)
    pcd = open(out_pcd_file, 'w')
    pcd.write(header)
    xyz_array = f.xyz
    intensities = f.points.intensity
    points = np.column_stack((xyz_array, intensities))
    np.savetxt(pcd,points, fmt='%.2f %.2f %.2f %.2f')
    pcd.close()


if __name__ == '__main__':
    las_file = "/home/oscar/Music/20201201140942__Ground.las"
    out_pcd_file = '/home/oscar/Music/20201201140942__Ground.pcd'
    to_pcd(las_file, out_pcd_file)
    print('done')