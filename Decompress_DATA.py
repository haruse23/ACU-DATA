import struct
import os
import sys
import lzo

from decompress_ import decompress


if len(sys.argv) < 2:
    print("Drag and drop a .data file onto this script or pass the path as an argument.")
    sys.exit(1)

path = sys.argv[1]
script_dir = os.path.dirname(os.path.abspath(__file__))

base_name = os.path.basename(path).split('.')[0]
out_dir = os.path.join(script_dir, base_name)


with open(path, "rb") as f:

    for i in range (2):
        ID = f.read(8)

        f.seek(2, 1)

        CompressionType = f.read(1)

        f.seek(3, 1)
        
        Version = f.read(1)

        Chunk_Count = struct.unpack_from("<I", f.read(4), 0x00)[0]

        Chunk_Header = []
        for j in range (Chunk_Count):
            Uncompressed_Size = struct.unpack_from("<H", f.read(2), 0x00)[0]

            Compressed_Size = struct.unpack_from("<H", f.read(2), 0x00)[0]

            Chunk_Header.append((Uncompressed_Size, Compressed_Size))

        compression_map = {
            b'\x01': 1,
            b'\x02': 2,
            b'\x05': 5
        }

        mode = compression_map.get(CompressionType)
        if mode is None:
            raise Exception(f"Unknown compression type: {CompressionType}")

        Chunks = []
        
        for Uncompressed_Size, Compressed_Size in Chunk_Header:
            f.seek(4, 1)  # skip the 4-byte hash
            Compressed_Chunk = f.read(Compressed_Size)

            Decompressed_Chunk = decompress(mode, Compressed_Chunk, Uncompressed_Size)
            Chunks.append(Decompressed_Chunk)

        Decompressed_File = b''.join(Chunks)

file_name = os.path.basename(path).split('.')[0]
file_name = file_name + ".decompressed"
file_path = os.path.join(out_dir, file_name)


os.makedirs(out_dir, exist_ok=True)


with open(file_path, "wb") as out_file:
    out_file.write(Decompressed_File)

print(f"Decompressed file saved as: {file_path}")



