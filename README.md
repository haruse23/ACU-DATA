Credits for gentlegiantJGC for the `decompress_.py` and `resources`

https://github.com/gentlegiantJGC/ACExplorer/blob/master/pyUbiForge/misc/decompress_.py

Decompression Code can run on AC1 if Chunk Count is read as 2 bytes instead of 4, like this:

`Chunk_Count = struct.unpack_from("<H", f.read(2), 0x00)[0]`
